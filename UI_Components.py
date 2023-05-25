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
    QToolButton, QVBoxLayout, QWidget)
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
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
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
        self.widget.setMinimumSize(QSize(0, 100))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(40, 0))
        self.label_2.setPixmap(QPixmap(u":/resources/files/icons/music.svg"))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.song_title_label = QLabel(self.widget_2)
        self.song_title_label.setObjectName(u"song_title_label")

        self.horizontalLayout_2.addWidget(self.song_title_label)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)
        self.label_4.setMinimumSize(QSize(40, 0))
        self.label_4.setPixmap(QPixmap(u":/resources/files/icons/users.svg"))

        self.horizontalLayout_3.addWidget(self.label_4)

        self.song_artist_label = QLabel(self.widget_3)
        self.song_artist_label.setObjectName(u"song_artist_label")

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
        icon = QIcon()
        icon.addFile(u":/resources/files/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon)
        self.settings_button.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.settings_button)

        self.help_button = QToolButton(self.groupBox_2)
        self.help_button.setObjectName(u"help_button")
        icon1 = QIcon()
        icon1.addFile(u":/resources/files/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.help_button.setIcon(icon1)
        self.help_button.setIconSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.help_button)

        self.horizontalSpacer = QSpacerItem(170, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.chillzam_button = QPushButton(self.groupBox_2)
        self.chillzam_button.setObjectName(u"chillzam_button")
        self.chillzam_button.setMinimumSize(QSize(200, 40))
        font = QFont()
        font.setPointSize(14)
        self.chillzam_button.setFont(font)

        self.horizontalLayout.addWidget(self.chillzam_button)


        self.verticalLayout.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Current Song", None))
        self.album_art_label.setText("")
        self.label_2.setText("")
        self.song_title_label.setText("")
        self.label_4.setText("")
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QToolButton,
    QWidget)
import Resources_rc

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(400, 215)
        self.groupBox = QGroupBox(SettingsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 381, 161))
        self.shazam_api_line_edit = QLineEdit(self.groupBox)
        self.shazam_api_line_edit.setObjectName(u"shazam_api_line_edit")
        self.shazam_api_line_edit.setGeometry(QRect(140, 120, 201, 22))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 120, 111, 21))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.channel_line_edit = QLineEdit(self.groupBox)
        self.channel_line_edit.setObjectName(u"channel_line_edit")
        self.channel_line_edit.setGeometry(QRect(140, 20, 201, 22))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 111, 21))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 111, 21))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.twitch_token_line_edit = QLineEdit(self.groupBox)
        self.twitch_token_line_edit.setObjectName(u"twitch_token_line_edit")
        self.twitch_token_line_edit.setGeometry(QRect(140, 60, 201, 22))
        self.channel_help_button = QToolButton(self.groupBox)
        self.channel_help_button.setObjectName(u"channel_help_button")
        self.channel_help_button.setGeometry(QRect(350, 20, 22, 22))
        icon = QIcon()
        icon.addFile(u":/resources/files/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.channel_help_button.setIcon(icon)
        self.token_help_button = QToolButton(self.groupBox)
        self.token_help_button.setObjectName(u"token_help_button")
        self.token_help_button.setGeometry(QRect(350, 60, 22, 22))
        self.token_help_button.setIcon(icon)
        self.shazam_help_button = QToolButton(self.groupBox)
        self.shazam_help_button.setObjectName(u"shazam_help_button")
        self.shazam_help_button.setGeometry(QRect(350, 120, 22, 22))
        self.shazam_help_button.setIcon(icon)
        self.cancel_button = QPushButton(SettingsDialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(310, 180, 75, 24))
        self.save_button = QPushButton(SettingsDialog)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(210, 180, 75, 24))

        self.retranslateUi(SettingsDialog)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.shazam_api_line_edit.setText("")
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"Shazam API Key:", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"Twitch GQL Token:", None))
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"Twitch Channel:", None))
        self.twitch_token_line_edit.setText("")
        self.channel_help_button.setText("")
        self.token_help_button.setText("")
        self.shazam_help_button.setText("")
        self.cancel_button.setText(QCoreApplication.translate("SettingsDialog", u"Cancel", None))
        self.save_button.setText(QCoreApplication.translate("SettingsDialog", u"Save", None))
    # retranslateUi



