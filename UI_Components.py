# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ChillZam.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QToolButton, QVBoxLayout, QWidget)
import Resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(523, 563)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(523, 563))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.album_art_label = QLabel(self.groupBox)
        self.album_art_label.setObjectName(u"album_art_label")
        self.album_art_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.album_art_label)

        self.widget = QWidget(self.groupBox)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(0, 140))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.twitch_icon_label = QLabel(self.widget_4)
        self.twitch_icon_label.setObjectName(u"twitch_icon_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.twitch_icon_label.sizePolicy().hasHeightForWidth())
        self.twitch_icon_label.setSizePolicy(sizePolicy2)
        self.twitch_icon_label.setMinimumSize(QSize(40, 0))
        self.twitch_icon_label.setPixmap(QPixmap(u":/resources/files/icons/twitch.svg"))

        self.horizontalLayout_4.addWidget(self.twitch_icon_label)

        self.twitch_channel_label = QLabel(self.widget_4)
        self.twitch_channel_label.setObjectName(u"twitch_channel_label")
        font = QFont()
        font.setPointSize(14)
        self.twitch_channel_label.setFont(font)

        self.horizontalLayout_4.addWidget(self.twitch_channel_label)


        self.verticalLayout_3.addWidget(self.widget_4)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.song_icon_label = QLabel(self.widget_2)
        self.song_icon_label.setObjectName(u"song_icon_label")
        sizePolicy2.setHeightForWidth(self.song_icon_label.sizePolicy().hasHeightForWidth())
        self.song_icon_label.setSizePolicy(sizePolicy2)
        self.song_icon_label.setMinimumSize(QSize(40, 0))
        self.song_icon_label.setPixmap(QPixmap(u":/resources/files/icons/music.svg"))

        self.horizontalLayout_2.addWidget(self.song_icon_label)

        self.song_title_label = QLabel(self.widget_2)
        self.song_title_label.setObjectName(u"song_title_label")
        self.song_title_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.song_title_label)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.artist_icon_label = QLabel(self.widget_3)
        self.artist_icon_label.setObjectName(u"artist_icon_label")
        sizePolicy2.setHeightForWidth(self.artist_icon_label.sizePolicy().hasHeightForWidth())
        self.artist_icon_label.setSizePolicy(sizePolicy2)
        self.artist_icon_label.setMinimumSize(QSize(40, 0))
        self.artist_icon_label.setPixmap(QPixmap(u":/resources/files/icons/users.svg"))

        self.horizontalLayout_3.addWidget(self.artist_icon_label)

        self.song_artist_label = QLabel(self.widget_3)
        self.song_artist_label.setObjectName(u"song_artist_label")
        self.song_artist_label.setFont(font)

        self.horizontalLayout_3.addWidget(self.song_artist_label)


        self.verticalLayout_3.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy1.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy1)
        self.groupBox_2.setMinimumSize(QSize(0, 80))
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.settings_button = QToolButton(self.groupBox_2)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setMinimumSize(QSize(0, 40))
        icon = QIcon()
        icon.addFile(u":/resources/files/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon)
        self.settings_button.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.settings_button)

        self.help_button = QToolButton(self.groupBox_2)
        self.help_button.setObjectName(u"help_button")
        self.help_button.setMinimumSize(QSize(0, 40))
        icon1 = QIcon()
        icon1.addFile(u":/resources/files/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.help_button.setIcon(icon1)
        self.help_button.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.help_button)

        self.horizontalSpacer = QSpacerItem(170, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.chillzam_button = QPushButton(self.groupBox_2)
        self.chillzam_button.setObjectName(u"chillzam_button")
        self.chillzam_button.setMinimumSize(QSize(200, 40))
        self.chillzam_button.setFont(font)

        self.horizontalLayout.addWidget(self.chillzam_button)


        self.verticalLayout.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setStyleSheet(u"")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Current Song", None))
        self.album_art_label.setText("")
        self.twitch_icon_label.setText("")
        self.twitch_channel_label.setText("")
        self.song_icon_label.setText("")
        self.song_title_label.setText("")
        self.artist_icon_label.setText("")
        self.song_artist_label.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Controls", None))
        self.settings_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.help_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.chillzam_button.setText(QCoreApplication.translate("MainWindow", u"What Song Is This?", None))
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QToolButton,
    QWidget)
import Resources_rc

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(373, 216)
        self.cancel_button = QPushButton(SettingsDialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(270, 180, 75, 24))
        self.save_button = QPushButton(SettingsDialog)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(170, 180, 75, 24))
        self.dark_mode_checkbox = QCheckBox(SettingsDialog)
        self.dark_mode_checkbox.setObjectName(u"dark_mode_checkbox")
        self.dark_mode_checkbox.setGeometry(QRect(240, 140, 111, 20))
        self.channel_line_edit = QLineEdit(SettingsDialog)
        self.channel_line_edit.setObjectName(u"channel_line_edit")
        self.channel_line_edit.setGeometry(QRect(120, 20, 201, 22))
        self.channel_line_edit.setStyleSheet(u"padding-left: 3px; padding-right: 3px; ")
        self.label_2 = QLabel(SettingsDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 60, 111, 21))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.channel_help_button = QToolButton(SettingsDialog)
        self.channel_help_button.setObjectName(u"channel_help_button")
        self.channel_help_button.setGeometry(QRect(330, 20, 22, 22))
        icon = QIcon()
        icon.addFile(u":/resources/files/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.channel_help_button.setIcon(icon)
        self.label = QLabel(SettingsDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 20, 111, 21))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.twitch_token_line_edit = QLineEdit(SettingsDialog)
        self.twitch_token_line_edit.setObjectName(u"twitch_token_line_edit")
        self.twitch_token_line_edit.setGeometry(QRect(120, 60, 201, 22))
        self.twitch_token_line_edit.setStyleSheet(u"padding-left: 3px; padding-right: 3px; ")
        self.shazam_api_line_edit = QLineEdit(SettingsDialog)
        self.shazam_api_line_edit.setObjectName(u"shazam_api_line_edit")
        self.shazam_api_line_edit.setGeometry(QRect(120, 100, 201, 22))
        self.shazam_api_line_edit.setStyleSheet(u"padding-left: 3px; padding-right: 3px; ")
        self.label_3 = QLabel(SettingsDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 100, 111, 21))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.shazam_help_button = QToolButton(SettingsDialog)
        self.shazam_help_button.setObjectName(u"shazam_help_button")
        self.shazam_help_button.setGeometry(QRect(330, 100, 22, 22))
        self.shazam_help_button.setIcon(icon)
        self.token_help_button = QToolButton(SettingsDialog)
        self.token_help_button.setObjectName(u"token_help_button")
        self.token_help_button.setGeometry(QRect(330, 60, 22, 22))
        self.token_help_button.setIcon(icon)

        self.retranslateUi(SettingsDialog)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.cancel_button.setText(QCoreApplication.translate("SettingsDialog", u"Cancel", None))
        self.save_button.setText(QCoreApplication.translate("SettingsDialog", u"Save", None))
        self.dark_mode_checkbox.setText(QCoreApplication.translate("SettingsDialog", u"Dark Mode", None))
        self.channel_line_edit.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"test", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"Twitch GQL Token:", None))
        self.channel_help_button.setText("")
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"Twitch Channel:", None))
        self.twitch_token_line_edit.setText("")
        self.shazam_api_line_edit.setText("")
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"Shazam API Key:", None))
        self.shazam_help_button.setText("")
        self.token_help_button.setText("")
    # retranslateUi



