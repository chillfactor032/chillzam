# Python Imports
import sys
import json
import os
from enum import Enum

# PySide6 Imports
from PySide6.QtWidgets import QApplication, QMainWindow, QStyle, QDialog, QMessageBox
from PySide6.QtCore import Qt, QSettings, QFile, QTextStream, QStandardPaths, QUrl
from PySide6.QtGui import QPixmap, QIcon, QDesktopServices

#Project Imports
import Resources_rc
from UI_Components import Ui_MainWindow, Ui_SettingsDialog

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

        #Load Settings
        self.config_dir = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        if not os.path.isdir(self.config_dir):
            os.mkdir(self.config_dir)
        self.ini_path = os.path.join(self.config_dir, f"{self.project_name}.ini").replace("\\", "/")
        self.settings = QSettings(self.ini_path, QSettings.IniFormat)

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
        geometry = self.settings.value(f"{self.project_name}/geometry")
        window_state = self.settings.value(f"{self.project_name}/windowState")
        if(geometry and window_state):
            self.restoreGeometry(geometry) 
            self.restoreState(window_state)
        self.show()

    def show_settings(self):
        dialog = SettingsDialog(self.settings, parent=self)
        dialog.exec()

    def show_help(self):
        url = "https://github.com/chillfactor032/chillzam#gui-help"
        response = QMessageBox.information(self, "ChillZam!", "Would you like to view the README file for detailed help?", QMessageBox.Ok | QMessageBox.Cancel)
        if response == QMessageBox.Ok:
            QDesktopServices.openUrl(QUrl(url))

    def chillzam(self):
        pass

    # App is closing, cleanup
    def closeEvent(self, evt):
        # Remember the size and position of the GUI
        self.settings.setValue(f"{self.project_name}/geometry", self.saveGeometry())
        self.settings.setValue(f"{self.project_name}/windowState", self.saveState())
        self.settings.sync()
        evt.accept()

class SettingsDialog(QDialog):

    def __init__(self, settings, parent=None):
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
    
    def help_token(self):
        help_str = """
            This is the Twitch GPL Auth-Token. You can find this in your browser's cookies.\n\nWould you like to see instructions on how to get this value? 
        """.strip()
        response = QMessageBox.information(self, "ChillZam!", help_str, QMessageBox.Ok | QMessageBox.Cancel)
        if response == QMessageBox.Ok:
            QDesktopServices.openUrl(QUrl("https://www.twitchapps.com/tmi/"))
    
    def help_channel(self):
        help_str = """
            This is the Twitch channel name you wish to listen to. \n\nFor example, for https://twitch.tv/shroud, the channel name would just be "shroud". 
        """.strip()
        QMessageBox.information(self, "ChillZam!", help_str)
    
    def help_shazam(self):
        help_str = """
            This is the Shazam API Token. You will have to generate this yourself.\n\nWould you like to see instructions on how to do this? 
        """.strip()
        QMessageBox.information(self, "ChillZam!", help_str, QMessageBox.Ok | QMessageBox.Cancel)
    
    def save(self):
        channel = self.ui.channel_line_edit.text()
        token = self.ui.twitch_token_line_edit.text()
        api_key = self.ui.shazam_api_line_edit.text()
        self.settings.setValue(f"{self.project_name}/TwitchChannel", channel)
        self.settings.setValue(f"{self.project_name}/TwitchGPLToken", token)
        self.settings.setValue(f"{self.project_name}/ShazamAPIKey", api_key)
        self.settings.sync()
        self.accept()

    def cancel(self):
        self.reject()

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