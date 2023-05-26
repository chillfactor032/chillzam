# Python Imports
import sys
import json
import os
import platform
import hashlib
import stat
from threading import Thread
from enum import Enum

# PySide6 Imports
from PySide6.QtWidgets import QApplication, QMainWindow, QStyle, QDialog, QMessageBox
from PySide6.QtCore import Qt, QSettings, QFile, QTextStream, QStandardPaths, QUrl, Signal, QObject
from PySide6.QtGui import QPixmap, QIcon, QDesktopServices, QResizeEvent, QMovie

#Project Imports
import requests
import Resources_rc
from UI_Components import Ui_MainWindow, Ui_SettingsDialog
from chillzam import ChillZam

#Log Levels
class LogLevel(Enum):
    INFO = 0
    ERROR = 10
    DEBUG = 20
    
    @staticmethod
    def get(value):
        for level in LogLevel:
            if(value == level.value):
                return level
        return LogLevel.INFO


class MainWindow(QMainWindow, Ui_MainWindow):
    
    # App Vars
        

        

    def __init__(self):
        super(MainWindow, self).__init__()
        #Load UI Components
        self.setupUi(self)

        #Read Version File From Resources
        self.version_file = QFile(":version.json")
        self.version_file.open(QFile.ReadOnly)
        self.text_stream = QTextStream(self.version_file)
        self.version_file_text = self.text_stream.readAll()
        self.version_dict = json.loads(self.version_file_text)
        self.app_name = self.version_dict["product_name"]
        self.version = self.version_dict["version"]
        self.project_name = self.app_name.title().replace(" ", "")
        self.setWindowTitle(f"{self.app_name} {self.version}")

        # Dark Mode Stuff
        self.default_stylesheet = self.styleSheet()
        dark_css_file = QFile(":resources/files/dark-mode.css")
        dark_css_file.open(QFile.ReadOnly)
        dark_css_text_stream =  QTextStream(dark_css_file)
        self.dark_mode_stylesheet = dark_css_text_stream.readAll()
        self.twitch_light_pixmap = QPixmap(":resources/files/icons/twitch.svg")
        self.twitch_dark_pixmap = QPixmap(":resources/files/icons/twitch-dark.svg")
        self.song_light_pixmap = QPixmap(":resources/files/icons/music.svg")
        self.song_dark_pixmap = QPixmap(":resources/files/icons/music-dark.svg")
        self.artist_light_pixmap = QPixmap(":resources/files/icons/users.svg")
        self.artist_dark_pixmap = QPixmap(":resources/files/icons/users-dark.svg")

        #Load Settings
        self.config_dir = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        if not os.path.isdir(self.config_dir):
            os.mkdir(self.config_dir)
        self.ini_path = os.path.join(self.config_dir, f"{self.project_name}.ini").replace("\\", "/")
        self.settings = QSettings(self.ini_path, QSettings.IniFormat)

        ## Copy FFMPEG to Local Config Dir
        self.os = "win"
        ffmpeg_filename = "ffmpeg.exe"
        ffmpeg_file = QFile(f":resources/files/bin/win/{ffmpeg_filename}")
        if "macOS" in platform.platform(terse=1):
            #Mac Detected
            ffmpeg_filename = "ffmpeg"
            ffmpeg_file = QFile(f":resources/files/bin/mac/{ffmpeg_filename}")
            self.os = "mac"
        self.ffmpeg_path = os.path.join(self.config_dir, ffmpeg_filename).replace("\\", "/")
        self.ffmpeg_md5 = ""
        if(os.path.exists(self.ffmpeg_path)==False):
            ffmpeg_file.open(QFile.ReadOnly)
            data = ffmpeg_file.readAll()
            ffmpeg_bytes = data.data()
            with open(self.ffmpeg_path, "wb") as f:
                f.write(ffmpeg_bytes)
                self.ffmpeg_md5 = hashlib.md5(ffmpeg_bytes).hexdigest()
            if(os.path.exists(self.ffmpeg_path)==False):
                print("Failed to create FFMPEG Binary")
        else:
            with open(self.ffmpeg_path, 'rb') as f:
                ffmpeg_bytes = f.read()    
                self.ffmpeg_md5 = hashlib.md5(ffmpeg_bytes).hexdigest()

        #If OS not Windows, set ffmpeg binary as executable
        if self.os != "win":
            os.chmod(self.ffmpeg_path, stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)

        #Set window Icon
        default_icon_pixmap = QStyle.StandardPixmap.SP_FileDialogListView
        icon_pixmap = QPixmap(":resources/file/icon/icon.ico")
        icon = QIcon(icon_pixmap)
        default_icon = self.style().standardIcon(default_icon_pixmap)
        if icon:
            self.setWindowIcon(icon)
        else:
            self.setWindowIcon(default_icon)

        # Button/Menu Signals Go Here
        self.chillzam_button.clicked.connect(self.chillzam)
        self.settings_button.clicked.connect(self.show_settings)
        self.help_button.clicked.connect(self.show_help)

        #Finally, Show the UI
        self.album_art_pixmap = QPixmap()
        self.loading_movie = QMovie(":resources/files/icons/equalizer.gif")
        self.loading_movie.start()
        geometry = self.settings.value(f"{self.project_name}/geometry")
        window_state = self.settings.value(f"{self.project_name}/windowState")
        self.dark_mode = self.settings.value(f"{self.project_name}/DarkMode", "0") == "1"

        if self.dark_mode:
            self.toggle_dark_mode()

        if(geometry and window_state):
            self.restoreGeometry(geometry) 
            self.restoreState(window_state)
        self.show()

    def toggle_dark_mode(self):
        if self.dark_mode:
            #dark mode
            self.setStyleSheet(self.dark_mode_stylesheet)
            self.twitch_icon_label.setPixmap(self.twitch_dark_pixmap)
            self.song_icon_label.setPixmap(self.song_dark_pixmap)
            self.artist_icon_label.setPixmap(self.artist_dark_pixmap)
        else:
            #light mode
            self.setStyleSheet(self.default_stylesheet)
            self.twitch_icon_label.setPixmap(self.twitch_light_pixmap)
            self.song_icon_label.setPixmap(self.song_light_pixmap)
            self.artist_icon_label.setPixmap(self.artist_light_pixmap)

    def show_settings(self):
        dialog = SettingsDialog(self.settings, dark_stylesheet=self.dark_mode_stylesheet, parent=self)
        dialog.exec()
        #Check if dark mode changed
        self.dark_mode = self.settings.value(f"{self.project_name}/DarkMode", "0") == "1"
        self.toggle_dark_mode()

    def show_help(self):
        url = "https://github.com/chillfactor032/chillzam/blob/main/GUIHELP.md"
        response = QMessageBox.information(self, "ChillZam!", "Would you like to view the README file for detailed help?", QMessageBox.Ok | QMessageBox.Cancel)
        if response == QMessageBox.Ok:
            QDesktopServices.openUrl(QUrl(url))

    def status_update(self, msg, timeout=0):
        timeout = timeout*1000
        self.statusBar.showMessage(msg, timeout)

    def chillzam_done(self, result):
        self.hide_loading_gif()
        if len(result["error"]) == 0:
            self.song_artist_label.setText(result['artist'])
            self.song_title_label.setText(result['song'])
            album_art_fetcher = AlbumArtFetcher(result['album_art'])
            self.twitch_channel_label.setText(self.settings.value(f"{self.project_name}/TwitchChannel", ""))
            album_art_fetcher.signals.done.connect(self.set_album_art)
            album_art_fetcher.start()
            self.status_update(f"Requests remaining: {result['remaining']} / month", 20)
        else:
            self.status_update(f"Error: {result['error']}", 20)

    def set_album_art(self, pixmap:QPixmap):
        if pixmap is not None:
            # Save the original
            self.album_art_pixmap = pixmap
            h = self.album_art_label.height()
            w = self.album_art_label.width()
            self.album_art_label.setPixmap(pixmap.scaled(w, h, Qt.KeepAspectRatio))

    def chillzam(self):
        self.status_update("Detecting song...")
        self.album_art_label.setPixmap(QPixmap())
        self.show_loading_gif()
        self.album_art_pixmap = QPixmap()
        channel = self.settings.value(f"{self.project_name}/TwitchChannel", "")
        token = self.settings.value(f"{self.project_name}/TwitchGPLToken", "")
        api = self.settings.value(f"{self.project_name}/ShazamAPIKey", "")
        working_dir = "./test"
        cz = ChillZam(channel, token, api, self.config_dir, self.ffmpeg_path)
        cz.signals.status_update.connect(self.status_update)
        cz.signals.result.connect(self.chillzam_done)
        cz.start()
    
    def show_loading_gif(self):
        self.album_art_label.setMovie(self.loading_movie)
    
    def hide_loading_gif(self):
        self.album_art_label.setMovie(None)

    def resizeEvent(self, event: QResizeEvent) -> None:
        if not self.album_art_pixmap.isNull():
            h = self.album_art_label.height()
            w = self.album_art_label.width()
            self.album_art_label.setPixmap(self.album_art_pixmap.scaled(w, h, Qt.KeepAspectRatio))
        return super().resizeEvent(event)
    
    # App is closing, cleanup
    def closeEvent(self, evt):
        # Remember the size and position of the GUI
        self.settings.setValue(f"{self.project_name}/geometry", self.saveGeometry())
        self.settings.setValue(f"{self.project_name}/windowState", self.saveState())
        self.settings.sync()
        evt.accept()

class SettingsDialog(QDialog):

    def __init__(self, settings, dark_stylesheet=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_SettingsDialog()
        self.ui.setupUi(self)
        self.project_name = parent.project_name
        self.settings = settings
        self.ui.save_button.clicked.connect(self.save)
        self.ui.cancel_button.clicked.connect(self.cancel)
        self.ui.channel_help_button.clicked.connect(self.help_channel)
        self.ui.token_help_button.clicked.connect(self.help_token)
        self.ui.shazam_help_button.clicked.connect(self.help_shazam)
        self.ui.channel_line_edit.setText(self.settings.value(f"{self.project_name}/TwitchChannel", ""))
        self.ui.twitch_token_line_edit.setText(self.settings.value(f"{self.project_name}/TwitchGPLToken", ""))
        self.ui.shazam_api_line_edit.setText(self.settings.value(f"{self.project_name}/ShazamAPIKey", ""))
        self.ui.dark_mode_checkbox.setChecked(self.settings.value(f"{self.project_name}/DarkMode", "0")=="1")
        if self.settings.value(f"{self.project_name}/DarkMode", "0")=="1" and dark_stylesheet is not None:
            self.setStyleSheet(dark_stylesheet)

    def help_token(self):
        help_str = """
            This is the Twitch GPL Auth-Token. You can find this in your browser's cookies.\n\nWould you like to see instructions on how to get this value? 
        """.strip()
        url = "https://github.com/chillfactor032/chillzam/blob/main/GUIHELP.md"
        response = QMessageBox.information(self, "ChillZam!", help_str, QMessageBox.Ok | QMessageBox.Cancel)
        if response == QMessageBox.Ok:
            QDesktopServices.openUrl(QUrl(url))
    
    def help_channel(self):
        help_str = """
            This is the Twitch channel name you wish to listen to. \n\nFor example, for https://twitch.tv/shroud, the channel name would just be "shroud". 
        """.strip()
        QMessageBox.information(self, "ChillZam!", help_str)
    
    def help_shazam(self):
        help_str = """
            This is the Shazam API Token. You will have to generate this yourself.\n\nWould you like to see instructions on how to do this? 
        """.strip()
        url = "https://github.com/chillfactor032/chillzam/blob/main/GUIHELP.md"
        response = QMessageBox.information(self, "ChillZam!", help_str, QMessageBox.Ok | QMessageBox.Cancel)
        if response == QMessageBox.Ok:
            QDesktopServices.openUrl(QUrl(url))
    
    def save(self):
        channel = self.ui.channel_line_edit.text()
        token = self.ui.twitch_token_line_edit.text()
        api_key = self.ui.shazam_api_line_edit.text()
        self.settings.setValue(f"{self.project_name}/TwitchChannel", channel)
        self.settings.setValue(f"{self.project_name}/TwitchGPLToken", token)
        self.settings.setValue(f"{self.project_name}/ShazamAPIKey", api_key)
        if self.ui.dark_mode_checkbox.isChecked():
            self.settings.setValue(f"{self.project_name}/DarkMode", "1") 
        else:
            self.settings.setValue(f"{self.project_name}/DarkMode", "0") 
        self.settings.sync()
        self.accept()

    def cancel(self):
        self.reject()

class AlbumArtFetcher(Thread):

    class Signals(QObject):
        done = Signal(QPixmap)

    def __init__(self, img_url):
        Thread.__init__(self)
        self.img_url = img_url
        self.signals = AlbumArtFetcher.Signals()

    def run(self):
        pixmap = QPixmap()
        response = requests.get(self.img_url)
        if response.status_code == 200:
            pixmap.loadFromData(response.content)
        self.signals.done.emit(pixmap)

# Start the PySide6 App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    version_file = QFile(":version.json")
    version_file.open(QFile.ReadOnly)
    text_stream = QTextStream(version_file)
    version_file_text = text_stream.readAll()
    version_dict = json.loads(version_file_text)
    org_name = version_dict["company_name"]
    app_name = version_dict["product_name"]
    version = version_dict["version"]
    app.setOrganizationName(org_name)
    app.setApplicationName(app_name)
    app.setApplicationVersion(version)
    window = MainWindow()
    sys.exit(app.exec())