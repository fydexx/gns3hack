# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/n30x/Downloads/gns3-gui-2.0.3/gns3/ui/edit_project_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EditProjectDialog(object):
    def setupUi(self, EditProjectDialog):
        EditProjectDialog.setObjectName("EditProjectDialog")
        EditProjectDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        EditProjectDialog.resize(549, 276)
        EditProjectDialog.setStyleSheet("QWidget {\n"
"    background-color: #323232;\n"
"    color: #BAF73C;\n"
"}\n"
"\n"
"QToolBar {\n"
"    border:0px;\n"
"}\n"
"\n"
"QGraphicsView, QTextEdit, QPlainTextEdit, QTreeWidget, QListWidget, QLineEdit, QSpinBox, QComboBox {\n"
"    background-color: #282828;\n"
"}\n"
"\n"
"QLabel, QMenu, QStatusBar {\n"
"  color: #BAF73C;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    color: #f2f2f2;\n"
"    background-color: #383838;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: #383838;\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: #BAF73C;\n"
"    font: bold 12px;\n"
"    padding: 15px;\n"
"    border-style: none;\n"
"}\n"
"\n"
"QAbstractScrollArea::corner {\n"
"    background: #323232;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal, QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"  background: none;\n"
"}\n"
"\n"
"QComboBox {\n"
"    selection-color: #f2f2f2;\n"
"    selection-background-color: #323232;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #282828;\n"
"}\n"
"\n"
"QDockWidget, QMenuBar, QPushButton, QToolButton, QTabWidget, QHeaderView::section {\n"
"    color: #BAF73C;\n"
"    font: bold 11px;\n"
"}\n"
"\n"
"QTabBar {\n"
"    color: #BAF73C;\n"
"}\n"
"\n"
"QRadioButton, QCheckBox {\n"
"  color: #BAF73C;\n"
"}\n"
"\n"
"QRadioButton::disabled, QCheckBox::disabled {\n"
"  color: gray;\n"
"}\n"
"# bg-color=#282828\n"
"# fg-color=#BAF73C\n"
"# tool-bar=#323232\n"
"# selection-bg=#383838 \n"
"# selection-fg=#f2f2f2 ")
        EditProjectDialog.setModal(True)
        self.gridLayout = QtWidgets.QGridLayout(EditProjectDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.uiProjectNameLabel = QtWidgets.QLabel(EditProjectDialog)
        self.uiProjectNameLabel.setObjectName("uiProjectNameLabel")
        self.gridLayout.addWidget(self.uiProjectNameLabel, 0, 0, 1, 1)
        self.uiProjectNameLineEdit = QtWidgets.QLineEdit(EditProjectDialog)
        self.uiProjectNameLineEdit.setObjectName("uiProjectNameLineEdit")
        self.gridLayout.addWidget(self.uiProjectNameLineEdit, 0, 1, 1, 1)
        self.uiProjectAutoCloseCheckBox = QtWidgets.QCheckBox(EditProjectDialog)
        self.uiProjectAutoCloseCheckBox.setObjectName("uiProjectAutoCloseCheckBox")
        self.gridLayout.addWidget(self.uiProjectAutoCloseCheckBox, 5, 0, 1, 3)
        self.uiSceneHeightSpinBox = QtWidgets.QSpinBox(EditProjectDialog)
        self.uiSceneHeightSpinBox.setMinimum(500)
        self.uiSceneHeightSpinBox.setMaximum(1000000)
        self.uiSceneHeightSpinBox.setObjectName("uiSceneHeightSpinBox")
        self.gridLayout.addWidget(self.uiSceneHeightSpinBox, 2, 1, 1, 1)
        self.uiProjectAutoOpenCheckBox = QtWidgets.QCheckBox(EditProjectDialog)
        self.uiProjectAutoOpenCheckBox.setObjectName("uiProjectAutoOpenCheckBox")
        self.gridLayout.addWidget(self.uiProjectAutoOpenCheckBox, 3, 0, 1, 3)
        self.uiProjectAutoStartCheckBox = QtWidgets.QCheckBox(EditProjectDialog)
        self.uiProjectAutoStartCheckBox.setObjectName("uiProjectAutoStartCheckBox")
        self.gridLayout.addWidget(self.uiProjectAutoStartCheckBox, 4, 0, 1, 3)
        self.uiSceneWidthSpinBox = QtWidgets.QSpinBox(EditProjectDialog)
        self.uiSceneWidthSpinBox.setMinimum(500)
        self.uiSceneWidthSpinBox.setMaximum(1000000)
        self.uiSceneWidthSpinBox.setObjectName("uiSceneWidthSpinBox")
        self.gridLayout.addWidget(self.uiSceneWidthSpinBox, 1, 1, 1, 1)
        self.uiButtonBox = QtWidgets.QDialogButtonBox(EditProjectDialog)
        self.uiButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.uiButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.uiButtonBox.setObjectName("uiButtonBox")
        self.gridLayout.addWidget(self.uiButtonBox, 6, 0, 1, 3)
        self.uiSceneWidthLabel = QtWidgets.QLabel(EditProjectDialog)
        self.uiSceneWidthLabel.setObjectName("uiSceneWidthLabel")
        self.gridLayout.addWidget(self.uiSceneWidthLabel, 1, 0, 1, 1)
        self.uiSceneHeightLabel = QtWidgets.QLabel(EditProjectDialog)
        self.uiSceneHeightLabel.setObjectName("uiSceneHeightLabel")
        self.gridLayout.addWidget(self.uiSceneHeightLabel, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)

        self.retranslateUi(EditProjectDialog)
        self.uiButtonBox.accepted.connect(EditProjectDialog.accept)
        self.uiButtonBox.rejected.connect(EditProjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditProjectDialog)

    def retranslateUi(self, EditProjectDialog):
        _translate = QtCore.QCoreApplication.translate
        EditProjectDialog.setWindowTitle(_translate("EditProjectDialog", "Edit project"))
        self.uiProjectNameLabel.setText(_translate("EditProjectDialog", "Project Name:"))
        self.uiProjectAutoCloseCheckBox.setText(_translate("EditProjectDialog", "Leave this project running in the background when closing GNS3"))
        self.uiSceneHeightSpinBox.setSuffix(_translate("EditProjectDialog", " px"))
        self.uiProjectAutoOpenCheckBox.setText(_translate("EditProjectDialog", "Open this project in the background when GNS3 server starts"))
        self.uiProjectAutoStartCheckBox.setText(_translate("EditProjectDialog", "Start all nodes when this project is opened"))
        self.uiSceneWidthSpinBox.setSuffix(_translate("EditProjectDialog", " px"))
        self.uiSceneWidthLabel.setText(_translate("EditProjectDialog", "Scene width:"))
        self.uiSceneHeightLabel.setText(_translate("EditProjectDialog", "Scene height:"))

