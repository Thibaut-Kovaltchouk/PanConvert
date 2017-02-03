# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'panconvert_gui.ui'
#
# Created: Fri Feb  3 12:30:48 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_notepad_New(object):
    def setupUi(self, notepad_New):
        notepad_New.setObjectName("notepad_New")
        notepad_New.setWindowModality(QtCore.Qt.NonModal)
        notepad_New.resize(820, 576)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(notepad_New.sizePolicy().hasHeightForWidth())
        notepad_New.setSizePolicy(sizePolicy)
        notepad_New.setMinimumSize(QtCore.QSize(820, 550))
        notepad_New.setBaseSize(QtCore.QSize(760, 550))
        self.centralwidget = QtWidgets.QWidget(notepad_New)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(710, 500))
        self.centralwidget.setBaseSize(QtCore.QSize(710, 700))
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.centralwidget.setMouseTracking(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.editor_window = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.editor_window.setMinimumSize(QtCore.QSize(0, 120))
        self.editor_window.setBaseSize(QtCore.QSize(0, 266))
        self.editor_window.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.editor_window.setObjectName("editor_window")
        self.gridLayout_2.addWidget(self.editor_window, 0, 0, 3, 1)
        self.ButtonConvert = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonConvert.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.ButtonConvert.setObjectName("ButtonConvert")
        self.gridLayout_2.addWidget(self.ButtonConvert, 2, 3, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.StandardConversion = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StandardConversion.sizePolicy().hasHeightForWidth())
        self.StandardConversion.setSizePolicy(sizePolicy)
        self.StandardConversion.setMinimumSize(QtCore.QSize(175, 0))
        self.StandardConversion.setMaximumSize(QtCore.QSize(200, 16777215))
        self.StandardConversion.setChecked(False)
        self.StandardConversion.setAutoRepeat(False)
        self.StandardConversion.setObjectName("StandardConversion")
        self.verticalLayout_2.addWidget(self.StandardConversion)
        self.BatchConversion = QtWidgets.QCheckBox(self.centralwidget)
        self.BatchConversion.setMinimumSize(QtCore.QSize(175, 0))
        self.BatchConversion.setObjectName("BatchConversion")
        self.verticalLayout_2.addWidget(self.BatchConversion)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 3)
        self.MessageNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.MessageNumber.setToolTip("")
        self.MessageNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.MessageNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.MessageNumber.setObjectName("MessageNumber")
        self.gridLayout_2.addWidget(self.MessageNumber, 2, 1, 1, 1)
        self.ButtonRevert = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonRevert.setObjectName("ButtonRevert")
        self.gridLayout_2.addWidget(self.ButtonRevert, 2, 2, 1, 1)
        self.Converter_Type = QtWidgets.QTabWidget(self.centralwidget)
        self.Converter_Type.setObjectName("Converter_Type")
        self.Standard = QtWidgets.QWidget()
        self.Standard.setObjectName("Standard")
        self.formLayout = QtWidgets.QFormLayout(self.Standard)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.Standard)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_3)
        self.BoxFromFormat = QtWidgets.QGroupBox(self.Standard)
        self.BoxFromFormat.setMinimumSize(QtCore.QSize(105, 120))
        self.BoxFromFormat.setMaximumSize(QtCore.QSize(105, 100))
        self.BoxFromFormat.setObjectName("BoxFromFormat")
        self.layoutWidget = QtWidgets.QWidget(self.BoxFromFormat)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 92, 77))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ButtonFromMarkdown = QtWidgets.QRadioButton(self.layoutWidget)
        self.ButtonFromMarkdown.setChecked(False)
        self.ButtonFromMarkdown.setObjectName("ButtonFromMarkdown")
        self.verticalLayout.addWidget(self.ButtonFromMarkdown)
        self.ButtonFromOpml = QtWidgets.QRadioButton(self.layoutWidget)
        self.ButtonFromOpml.setCheckable(True)
        self.ButtonFromOpml.setChecked(False)
        self.ButtonFromOpml.setObjectName("ButtonFromOpml")
        self.verticalLayout.addWidget(self.ButtonFromOpml)
        self.ButtonFromHtml = QtWidgets.QRadioButton(self.layoutWidget)
        self.ButtonFromHtml.setObjectName("ButtonFromHtml")
        self.verticalLayout.addWidget(self.ButtonFromHtml)
        self.ButtonFromLatex = QtWidgets.QRadioButton(self.layoutWidget)
        self.ButtonFromLatex.setObjectName("ButtonFromLatex")
        self.verticalLayout.addWidget(self.ButtonFromLatex)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.BoxFromFormat)
        self.BoxToFormat = QtWidgets.QGroupBox(self.Standard)
        self.BoxToFormat.setMinimumSize(QtCore.QSize(110, 135))
        self.BoxToFormat.setMaximumSize(QtCore.QSize(140, 135))
        self.BoxToFormat.setObjectName("BoxToFormat")
        self.layoutWidget1 = QtWidgets.QWidget(self.BoxToFormat)
        self.layoutWidget1.setGeometry(QtCore.QRect(13, 31, 92, 96))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ButtonToHtml = QtWidgets.QRadioButton(self.layoutWidget1)
        self.ButtonToHtml.setChecked(False)
        self.ButtonToHtml.setObjectName("ButtonToHtml")
        self.gridLayout.addWidget(self.ButtonToHtml, 3, 0, 1, 1)
        self.ButtonToMarkdown = QtWidgets.QRadioButton(self.layoutWidget1)
        self.ButtonToMarkdown.setCheckable(True)
        self.ButtonToMarkdown.setChecked(False)
        self.ButtonToMarkdown.setObjectName("ButtonToMarkdown")
        self.gridLayout.addWidget(self.ButtonToMarkdown, 1, 0, 1, 1)
        self.ButtonToOpml = QtWidgets.QRadioButton(self.layoutWidget1)
        self.ButtonToOpml.setObjectName("ButtonToOpml")
        self.gridLayout.addWidget(self.ButtonToOpml, 2, 0, 1, 1)
        self.ButtonToLyx = QtWidgets.QRadioButton(self.layoutWidget1)
        self.ButtonToLyx.setObjectName("ButtonToLyx")
        self.gridLayout.addWidget(self.ButtonToLyx, 5, 0, 1, 1)
        self.ButtonToLatex = QtWidgets.QRadioButton(self.layoutWidget1)
        self.ButtonToLatex.setObjectName("ButtonToLatex")
        self.gridLayout.addWidget(self.ButtonToLatex, 4, 0, 1, 1)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.BoxToFormat)
        self.Converter_Type.addTab(self.Standard, "")
        self.Manual = QtWidgets.QWidget()
        self.Manual.setObjectName("Manual")
        self.label_2 = QtWidgets.QLabel(self.Manual)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 181, 16))
        self.label_2.setObjectName("label_2")
        self.labelFromBox = QtWidgets.QLabel(self.Manual)
        self.labelFromBox.setGeometry(QtCore.QRect(6, 56, 33, 16))
        self.labelFromBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.labelFromBox.setObjectName("labelFromBox")
        self.FromParameter = QtWidgets.QLineEdit(self.Manual)
        self.FromParameter.setGeometry(QtCore.QRect(100, 56, 141, 21))
        self.FromParameter.setMinimumSize(QtCore.QSize(50, 0))
        self.FromParameter.setInputMask("")
        self.FromParameter.setText("")
        self.FromParameter.setClearButtonEnabled(True)
        self.FromParameter.setObjectName("FromParameter")
        self.ButtonFromFormat = QtWidgets.QToolButton(self.Manual)
        self.ButtonFromFormat.setGeometry(QtCore.QRect(64, 56, 26, 22))
        self.ButtonFromFormat.setObjectName("ButtonFromFormat")
        self.labelToBox = QtWidgets.QLabel(self.Manual)
        self.labelToBox.setGeometry(QtCore.QRect(6, 88, 40, 16))
        self.labelToBox.setMaximumSize(QtCore.QSize(40, 16777215))
        self.labelToBox.setObjectName("labelToBox")
        self.ToParameter = QtWidgets.QLineEdit(self.Manual)
        self.ToParameter.setGeometry(QtCore.QRect(100, 88, 141, 21))
        self.ToParameter.setText("")
        self.ToParameter.setClearButtonEnabled(True)
        self.ToParameter.setObjectName("ToParameter")
        self.ButtonToFormat = QtWidgets.QToolButton(self.Manual)
        self.ButtonToFormat.setGeometry(QtCore.QRect(64, 88, 26, 22))
        self.ButtonToFormat.setObjectName("ButtonToFormat")
        self.label = QtWidgets.QLabel(self.Manual)
        self.label.setGeometry(QtCore.QRect(6, 120, 50, 16))
        self.label.setObjectName("label")
        self.ExtraParameter = QtWidgets.QLineEdit(self.Manual)
        self.ExtraParameter.setGeometry(QtCore.QRect(100, 120, 141, 21))
        self.ExtraParameter.setToolTip("")
        self.ExtraParameter.setText("")
        self.ExtraParameter.setClearButtonEnabled(True)
        self.ExtraParameter.setObjectName("ExtraParameter")
        self.ButtonOptions = QtWidgets.QToolButton(self.Manual)
        self.ButtonOptions.setGeometry(QtCore.QRect(64, 120, 26, 22))
        self.ButtonOptions.setObjectName("ButtonOptions")
        self.Converter_Type.addTab(self.Manual, "")
        self.Batch = QtWidgets.QWidget()
        self.Batch.setObjectName("Batch")
        self.OpenPath = QtWidgets.QLineEdit(self.Batch)
        self.OpenPath.setGeometry(QtCore.QRect(10, 30, 231, 21))
        self.OpenPath.setObjectName("OpenPath")
        self.Button_Open_Path = QtWidgets.QToolButton(self.Batch)
        self.Button_Open_Path.setGeometry(QtCore.QRect(10, 60, 25, 22))
        self.Button_Open_Path.setMaximumSize(QtCore.QSize(25, 23))
        self.Button_Open_Path.setObjectName("Button_Open_Path")
        self.groupBox = QtWidgets.QGroupBox(self.Batch)
        self.groupBox.setGeometry(QtCore.QRect(30, 90, 120, 100))
        self.groupBox.setMinimumSize(QtCore.QSize(120, 100))
        self.groupBox.setMaximumSize(QtCore.QSize(140, 100))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ParameterBatchconvertRecursive = QtWidgets.QCheckBox(self.groupBox)
        self.ParameterBatchconvertRecursive.setChecked(True)
        self.ParameterBatchconvertRecursive.setObjectName("ParameterBatchconvertRecursive")
        self.gridLayout_4.addWidget(self.ParameterBatchconvertRecursive, 3, 0, 1, 1)
        self.ParameterBatchconvertDirectory = QtWidgets.QRadioButton(self.groupBox)
        self.ParameterBatchconvertDirectory.setChecked(True)
        self.ParameterBatchconvertDirectory.setObjectName("ParameterBatchconvertDirectory")
        self.gridLayout_4.addWidget(self.ParameterBatchconvertDirectory, 2, 0, 1, 1)
        self.ParameterBatchconvertFiles = QtWidgets.QRadioButton(self.groupBox)
        self.ParameterBatchconvertFiles.setObjectName("ParameterBatchconvertFiles")
        self.gridLayout_4.addWidget(self.ParameterBatchconvertFiles, 1, 0, 1, 1)
        self.Filter = QtWidgets.QLineEdit(self.Batch)
        self.Filter.setGeometry(QtCore.QRect(40, 60, 201, 21))
        self.Filter.setObjectName("Filter")
        self.label_4 = QtWidgets.QLabel(self.Batch)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 171, 16))
        self.label_4.setObjectName("label_4")
        self.Button_SetBatchConverter = QtWidgets.QPushButton(self.Batch)
        self.Button_SetBatchConverter.setGeometry(QtCore.QRect(170, 110, 71, 32))
        self.Button_SetBatchConverter.setObjectName("Button_SetBatchConverter")
        self.Converter_Type.addTab(self.Batch, "")
        self.gridLayout_2.addWidget(self.Converter_Type, 0, 1, 1, 3)
        notepad_New.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(notepad_New)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 22))
        self.menubar.setAcceptDrops(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExtras = QtWidgets.QMenu(self.menubar)
        self.menuExtras.setEnabled(True)
        self.menuExtras.setObjectName("menuExtras")
        self.menuEdit_2 = QtWidgets.QMenu(self.menubar)
        self.menuEdit_2.setObjectName("menuEdit_2")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        notepad_New.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(notepad_New)
        self.statusbar.setObjectName("statusbar")
        notepad_New.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(notepad_New)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setObjectName("toolBar")
        notepad_New.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockLogWindow = QtWidgets.QDockWidget(notepad_New)
        self.dockLogWindow.setMinimumSize(QtCore.QSize(102, 124))
        self.dockLogWindow.setFloating(True)
        self.dockLogWindow.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockLogWindow.setObjectName("dockLogWindow")
        self.logWindow = QtWidgets.QWidget()
        self.logWindow.setObjectName("logWindow")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.logWindow)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.logBrowser = QtWidgets.QPlainTextEdit(self.logWindow)
        self.logBrowser.setObjectName("logBrowser")
        self.gridLayout_3.addWidget(self.logBrowser, 0, 0, 1, 1)
        self.dockLogWindow.setWidget(self.logWindow)
        notepad_New.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockLogWindow)
        self.actionSave = QtWidgets.QAction(notepad_New)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/save"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(notepad_New)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/open"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionOpen.setIconVisibleInMenu(True)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_AS = QtWidgets.QAction(notepad_New)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/save_as"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_AS.setIcon(icon2)
        self.actionSave_AS.setObjectName("actionSave_AS")
        self.actionNew = QtWidgets.QAction(notepad_New)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/new"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew.setIcon(icon3)
        self.actionNew.setObjectName("actionNew")
        self.actionMarkdown2Latex = QtWidgets.QAction(notepad_New)
        self.actionMarkdown2Latex.setObjectName("actionMarkdown2Latex")
        self.actionOpml2latex = QtWidgets.QAction(notepad_New)
        self.actionOpml2latex.setObjectName("actionOpml2latex")
        self.actionOpml2Markdown = QtWidgets.QAction(notepad_New)
        self.actionOpml2Markdown.setObjectName("actionOpml2Markdown")
        self.actionMarkdown2opml = QtWidgets.QAction(notepad_New)
        self.actionMarkdown2opml.setObjectName("actionMarkdown2opml")
        self.actionPreferences = QtWidgets.QAction(notepad_New)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/freferences"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/icons/freferences"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionPreferences.setIcon(icon4)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionLatex2Opml = QtWidgets.QAction(notepad_New)
        self.actionLatex2Opml.setObjectName("actionLatex2Opml")
        self.actionLatex2Markdown = QtWidgets.QAction(notepad_New)
        self.actionLatex2Markdown.setObjectName("actionLatex2Markdown")
        self.actionHtml2Markdown = QtWidgets.QAction(notepad_New)
        self.actionHtml2Markdown.setObjectName("actionHtml2Markdown")
        self.actionHtml2Latex = QtWidgets.QAction(notepad_New)
        self.actionHtml2Latex.setObjectName("actionHtml2Latex")
        self.actionHtml2opml = QtWidgets.QAction(notepad_New)
        self.actionHtml2opml.setObjectName("actionHtml2opml")
        self.actionOpml2html = QtWidgets.QAction(notepad_New)
        self.actionOpml2html.setObjectName("actionOpml2html")
        self.actionMarkdown2html = QtWidgets.QAction(notepad_New)
        self.actionMarkdown2html.setObjectName("actionMarkdown2html")
        self.actionLatex2html = QtWidgets.QAction(notepad_New)
        self.actionLatex2html.setObjectName("actionLatex2html")
        self.actionHelp = QtWidgets.QAction(notepad_New)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(":/icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionHelp.setIcon(icon5)
        self.actionHelp.setObjectName("actionHelp")
        self.actionMarkdown2Lyx = QtWidgets.QAction(notepad_New)
        self.actionMarkdown2Lyx.setObjectName("actionMarkdown2Lyx")
        self.actionUndo = QtWidgets.QAction(notepad_New)
        self.actionUndo.setObjectName("actionUndo")
        self.actionAbout = QtWidgets.QAction(notepad_New)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSearch = QtWidgets.QAction(notepad_New)
        self.actionSearch.setObjectName("actionSearch")
        self.actionLogViewer = QtWidgets.QAction(notepad_New)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/opml"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogViewer.setIcon(icon6)
        self.actionLogViewer.setObjectName("actionLogViewer")
        self.actionAbove = QtWidgets.QAction(notepad_New)
        self.actionAbove.setObjectName("actionAbove")
        self.actionBelow = QtWidgets.QAction(notepad_New)
        self.actionBelow.setObjectName("actionBelow")
        self.actionLeft = QtWidgets.QAction(notepad_New)
        self.actionLeft.setObjectName("actionLeft")
        self.actionRight = QtWidgets.QAction(notepad_New)
        self.actionRight.setObjectName("actionRight")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_AS)
        self.menuFile.addSeparator()
        self.menuExtras.addAction(self.actionHelp)
        self.menuExtras.addAction(self.actionAbout)
        self.menuEdit_2.addAction(self.actionPreferences)
        self.menuEdit_2.addAction(self.actionUndo)
        self.menuEdit_2.addAction(self.actionSearch)
        self.menuWindow.addAction(self.actionLogViewer)
        self.menuWindow.addSeparator()
        self.menuWindow.addAction(self.actionAbove)
        self.menuWindow.addAction(self.actionBelow)
        self.menuWindow.addAction(self.actionLeft)
        self.menuWindow.addAction(self.actionRight)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit_2.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuExtras.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSave_AS)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPreferences)
        self.toolBar.addAction(self.actionLogViewer)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHelp)

        self.retranslateUi(notepad_New)
        self.Converter_Type.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(notepad_New)

    def retranslateUi(self, notepad_New):
        _translate = QtCore.QCoreApplication.translate
        notepad_New.setWindowTitle(_translate("notepad_New", "PanConvert"))
        self.ButtonConvert.setText(_translate("notepad_New", "Convert"))
        self.StandardConversion.setText(_translate("notepad_New", "Standard Conversion"))
        self.BatchConversion.setText(_translate("notepad_New", "Batch Conversion"))
        self.MessageNumber.setAccessibleName(_translate("notepad_New", "New Messages"))
        self.ButtonRevert.setText(_translate("notepad_New", "Revert"))
        self.label_3.setText(_translate("notepad_New", "Standard Mode"))
        self.BoxFromFormat.setTitle(_translate("notepad_New", "From Format"))
        self.ButtonFromMarkdown.setText(_translate("notepad_New", "Markdown"))
        self.ButtonFromOpml.setText(_translate("notepad_New", "Opml"))
        self.ButtonFromHtml.setText(_translate("notepad_New", "Html"))
        self.ButtonFromLatex.setText(_translate("notepad_New", "Latex"))
        self.BoxToFormat.setTitle(_translate("notepad_New", "To Format"))
        self.ButtonToHtml.setText(_translate("notepad_New", "Html"))
        self.ButtonToMarkdown.setText(_translate("notepad_New", "Markdown"))
        self.ButtonToOpml.setText(_translate("notepad_New", "Opml"))
        self.ButtonToLyx.setText(_translate("notepad_New", "Lyx"))
        self.ButtonToLatex.setText(_translate("notepad_New", "Latex"))
        self.Converter_Type.setTabText(self.Converter_Type.indexOf(self.Standard), _translate("notepad_New", "Standard"))
        self.Manual.setAccessibleName(_translate("notepad_New", "Manual"))
        self.label_2.setText(_translate("notepad_New", "Manual Mode"))
        self.labelFromBox.setText(_translate("notepad_New", "From"))
        self.ButtonFromFormat.setText(_translate("notepad_New", "..."))
        self.labelToBox.setText(_translate("notepad_New", "To"))
        self.ButtonToFormat.setText(_translate("notepad_New", "..."))
        self.label.setText(_translate("notepad_New", "Options"))
        self.ButtonOptions.setText(_translate("notepad_New", "..."))
        self.Converter_Type.setTabText(self.Converter_Type.indexOf(self.Manual), _translate("notepad_New", "Manual"))
        self.OpenPath.setPlaceholderText(_translate("notepad_New", "Optional Directory Path"))
        self.Button_Open_Path.setText(_translate("notepad_New", "..."))
        self.groupBox.setTitle(_translate("notepad_New", "Conversion Mode"))
        self.ParameterBatchconvertRecursive.setText(_translate("notepad_New", "Recursive"))
        self.ParameterBatchconvertDirectory.setText(_translate("notepad_New", "Directory"))
        self.ParameterBatchconvertFiles.setText(_translate("notepad_New", "Files"))
        self.Filter.setPlaceholderText(_translate("notepad_New", "optional File Extension Filter (separate with ;)"))
        self.label_4.setText(_translate("notepad_New", "Batch Mode"))
        self.Button_SetBatchConverter.setText(_translate("notepad_New", "Set"))
        self.Converter_Type.setTabText(self.Converter_Type.indexOf(self.Batch), _translate("notepad_New", "Batch"))
        self.menuFile.setTitle(_translate("notepad_New", "File"))
        self.menuExtras.setTitle(_translate("notepad_New", "Help"))
        self.menuEdit_2.setTitle(_translate("notepad_New", "Edit"))
        self.menuWindow.setTitle(_translate("notepad_New", "Window"))
        self.toolBar.setWindowTitle(_translate("notepad_New", "toolBar"))
        self.actionSave.setText(_translate("notepad_New", "Save Buffer"))
        self.actionOpen.setText(_translate("notepad_New", "Open"))
        self.actionOpen.setShortcut(_translate("notepad_New", "Ctrl+O"))
        self.actionSave_AS.setText(_translate("notepad_New", "Save File"))
        self.actionSave_AS.setShortcut(_translate("notepad_New", "Ctrl+S"))
        self.actionNew.setText(_translate("notepad_New", "New"))
        self.actionNew.setToolTip(_translate("notepad_New", "New"))
        self.actionMarkdown2Latex.setText(_translate("notepad_New", "Markdown2Latex"))
        self.actionOpml2latex.setText(_translate("notepad_New", "opml2latex"))
        self.actionOpml2latex.setToolTip(_translate("notepad_New", "Opml2Latex"))
        self.actionOpml2Markdown.setText(_translate("notepad_New", "Opml2Markdown"))
        self.actionOpml2Markdown.setToolTip(_translate("notepad_New", "Opml2Markdown(Pandoc)"))
        self.actionMarkdown2opml.setText(_translate("notepad_New", "Markdown2opml"))
        self.actionPreferences.setText(_translate("notepad_New", "Preferences"))
        self.actionLatex2Opml.setText(_translate("notepad_New", "Latex2Opml"))
        self.actionLatex2Markdown.setText(_translate("notepad_New", "Latex2Markdown"))
        self.actionHtml2Markdown.setText(_translate("notepad_New", "Html2Markdown"))
        self.actionHtml2Latex.setText(_translate("notepad_New", "Html2Latex"))
        self.actionHtml2opml.setText(_translate("notepad_New", "html2opml"))
        self.actionOpml2html.setText(_translate("notepad_New", "opml2html"))
        self.actionMarkdown2html.setText(_translate("notepad_New", "markdown2html"))
        self.actionLatex2html.setText(_translate("notepad_New", "latex2html"))
        self.actionHelp.setText(_translate("notepad_New", "Help"))
        self.actionMarkdown2Lyx.setText(_translate("notepad_New", "Markdown2Lyx"))
        self.actionUndo.setText(_translate("notepad_New", "Undo"))
        self.actionAbout.setText(_translate("notepad_New", "About"))
        self.actionSearch.setText(_translate("notepad_New", "Search"))
        self.actionLogViewer.setText(_translate("notepad_New", "LogViewer"))
        self.actionAbove.setText(_translate("notepad_New", "Position Above"))
        self.actionBelow.setText(_translate("notepad_New", "Position Below"))
        self.actionLeft.setText(_translate("notepad_New", "Position Left"))
        self.actionRight.setText(_translate("notepad_New", "Position Right"))

import source.gui.icons_rc
