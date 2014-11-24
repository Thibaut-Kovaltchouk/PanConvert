#!/usr/local/bin/python3
__author__ = 'apaeffgen'
# -*- coding: utf-8 -*-

    # This file is part of Panconvert.
    #
    # Panconvert is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.
    #
    # Panconvert is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.
    #
    # You should have received a copy of the GNU General Public License
    # along with Panconvert.  If not, see <http://www.gnu.org/licenses/>.

import codecs
import platform

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from source.dialog_preferences import *
from source.converter.markdown import *
from source.converter.latex import *
from source.converter.opml import *
from source.converter.html import *
from source.converter.epub import *
from source.converter.lyx import *
from source.converter.manual_converter import *
from source.gui.panconvert_gui import Ui_notepad

#TODO: Copy/Paste. In Ui + Function
#TODO: Batch-Conversion. In Ui + Function
# noinspection PyStatementEffect,PyAttributeOutsideInit,PyAttributeOutsideInit,PyAttributeOutsideInit
class StartQT5(QtWidgets.QMainWindow):

    """File Dialog Functions"""

    def file_dialog(self):
        global text, data, openfile


        fd = QtWidgets.QFileDialog(self)
        fd.setDirectory(QtCore.QDir.homePath())

        self.filename = fd.getOpenFileName()
        openfile = self.filename[0]
        from os.path import isfile
        if isfile(self.filename[0]):
            try:
                text = codecs.open(self.filename[0], 'r', 'utf-8').read()
                data = self.ui.editor_window.setPlainText(text)
                self.ui.actionSave.setEnabled(False)
            except:
                text = 'No Preview of the File-Data possible. Try to manually convert. Good Luck.'
                data = self.ui.editor_window.setPlainText(text)
                #QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                #                          'No Preview of the File-Data possible. Try to manually convert. Good Luck.')

    def file_save(self):
        from os.path import isfile
        try:
            isfile(self.filename[0])
            file = codecs.open(self.filename[0], 'w', 'utf-8')
            file.write(self.ui.editor_window.toPlainText())
            file.close()
        except AttributeError:
            self.file_save_as()

    def file_save_as(self):
        fd = QtWidgets.QFileDialog(self)
        fd.setDirectory(QtCore.QDir.homePath())
        self.filename = fd.getSaveFileName(self)
        file = codecs.open(self.filename[0], 'w', 'utf-8')
        filedata = self.ui.editor_window.toPlainText()
        file.write(filedata)
        file.close()

    def file_new(self):
        global text
        from os.path import isfile
        text = ''
        self.ui.editor_window.setPlainText(text)
        self.ui.actionSave.setEnabled(True)
        if isfile(self.filename[0]):
            self.ui.actionSave.setEnabled(False)


    '''Export Functions'''


    def file_export_html2markdown(self):
        global text
        text = self.ui.editor_window.toPlainText()
        if text is not "":
            output_content = convert_html2markdown(text)
            self.ui.editor_window.setPlainText(output_content)
            self.ui.actionSave.setEnabled(False)
            text = output_content
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'You have no Data to be converted. Please make an input')

    def file_export_markdown2html(self):
        global text
        text = self.ui.editor_window.toPlainText()
        if text is not "":
            output_content = convert_md2html(text)
            self.ui.editor_window.setPlainText(output_content)
            self.ui.actionSave.setEnabled(False)
            text = output_content
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'You have no Data to be converted. Please make an input')

    def file_export_md2latex(self):
        global text
        text = self.ui.editor_window.toPlainText()
        if text is not "":
            output_content = convert_md2latex(text)
            self.ui.editor_window.setPlainText(output_content)
            self.ui.actionSave.setEnabled(False)
            text = output_content
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'You have no Data to be converted. Please make an input')

    def file_export_opml2html(self):
        global text
        text = self.ui.editor_window.toPlainText()
        if text is not "":
            output_content = convert_opml2html(text)
            self.ui.editor_window.setPlainText(output_content)
            self.ui.actionSave.setEnabled(False)
            text = output_content
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'You have no Data to be converted. Please make an input')

    def file_export_opml2latex(self):
        global text
        text = self.ui.editor_window.toPlainText()
        if text is not "":
            output_content = convert_opml2latex(text)
            self.ui.editor_window.setPlainText(output_content)
            self.ui.actionSave.setEnabled(False)
            text = output_content
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'You have no Data to be converted. Please make an input')

    def file_export_opml2markdown_pandoc(self):
        global text
        text = self.ui.editor_window.toPlainText()
        if text is not "":
            output_content = convert_opml2markdown(text)
            self.ui.editor_window.setPlainText(output_content)
            self.ui.actionSave.setEnabled(False)
            text = output_content
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'You have no Data to be converted. Please make an input')

    def file_export_html2opml(self):
        global text
        text = self.ui.editor_window.toPlainText()
        if text is not "":
            output_content = convert_html2opml(text)
            self.ui.editor_window.setPlainText(output_content)
            self.ui.actionSave.setEnabled(False)
            text = output_content
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'You have no Data to be converted. Please make an input')

    def file_export_markdown2opml(self):
        global text
        text = self.ui.editor_window.toPlainText()
        if text is not "":
            output_content = convert_markdown2opml(text)
            self.ui.editor_window.setPlainText(output_content)
            self.ui.actionSave.setEnabled(False)
            text = output_content
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'You have no Data to be converted. Please make an input')

    def file_export_html2latex(self):
        global text
        text = self.ui.editor_window.toPlainText()
        if text is not "":
            output_content = convert_html2latex(text)
            self.ui.editor_window.setPlainText(output_content)
            self.ui.actionSave.setEnabled(False)
            text = output_content
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'You have no Data to be converted. Please make an input')

    def file_export_latex2html(self):
        global text
        text = self.ui.editor_window.toPlainText()
        if text is not "":
            output_content = convert_latex2html(text)
            self.ui.editor_window.setPlainText(output_content)
            self.ui.actionSave.setEnabled(False)
            text = output_content
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'You have no Data to be converted. Please make an input')

    def file_export_latex2opml(self):
        global text
        text = self.ui.editor_window.toPlainText()
        if text is not "":
            output_content = convert_latex2opml(text)
            self.ui.editor_window.setPlainText(output_content)
            self.ui.actionSave.setEnabled(False)
            text = output_content
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'You have no Data to be converted. Please make an input')

    def file_export_latex2markdown(self):
        global text
        text = self.ui.editor_window.toPlainText()
        if text is not "":
            output_content = convert_latex2markdown(text)
            self.ui.editor_window.setPlainText(output_content)
            self.ui.actionSave.setEnabled(False)
            text = output_content
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'You have no Data to be converted. Please make an input')

    def file_export_markdown2lyx(self):
        global text
        text = self.ui.editor_window.toPlainText()
        if text is not "":
            output_content = convert_markdown2lyx(text)
            self.ui.editor_window.setPlainText(output_content)
            self.ui.actionSave.setEnabled(False)
            text = output_content
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'You have no Data to be converted. Please make an input')

    def file_export_manualconverter(self):

        global text, openfile
        text = self.ui.editor_window.toPlainText()
        if text == '':
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'You have no Data to be converted. Please make an input')
        elif text != 'No Preview of the File-Data possible. Try to manually convert. Good Luck.':
            output_content = convert_universal(text,toFormat,fromFormat,extraParameter)

            self.ui.actionSave.setEnabled(False)
            if output_content is not '':
                self.ui.editor_window.setPlainText(output_content)
            else:
                QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'There should be a file written to the folder where Panconvert'
                                          ' is stored. Please check at this location.')

        elif text == 'No Preview of the File-Data possible. Try to manually convert. Good Luck.':
            output_content = convert_binary(openfile,toFormat,fromFormat,extraParameter)
            self.ui.editor_window.setPlainText("I tried my best to convert. Check if there had been any Output, and if"
                                               " so, please check the quality of the created output.")
            self.ui.actionSave.setEnabled(False)
            text = output_content
        else:
            QtWidgets.QMessageBox.warning(None, 'Error-Message',
                                          'Something went terribly wrong. Please get some help. Google never was your'
                                          '/ is your friend. Just the NSA is.')

    def file_export_markdown2epub(self):
        global text
        text = self.ui.editor_window.toPlainText()
        if text is not "":
            output_content = convert_md2epub(text)
            self.ui.editor_window.setPlainText(output_content)
            self.ui.actionSave.setEnabled(False)
            text = output_content
        else:
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'You have no Data to be converted. Please make an input')

    """Gui-Event Definitions"""

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_notepad()
        self.ui.setupUi(self)
        self.ui.actionOpen.triggered.connect(self.file_dialog)
        self.ui.actionSave.triggered.connect(self.file_save)
        self.ui.actionSave_AS.triggered.connect(self.file_save_as)
        self.ui.actionNew.triggered.connect(self.file_new)
        self.ui.actionMarkdown2Latex.triggered.connect(self.file_export_md2latex)
        self.ui.actionOpml2latex.triggered.connect(self.file_export_opml2latex)
        self.ui.actionLatex2Opml.triggered.connect(self.file_export_latex2opml)
        self.ui.actionLatex2Markdown.triggered.connect(self.file_export_latex2markdown)
        self.ui.actionOpml2Markdown.triggered.connect(self.file_export_opml2markdown_pandoc)
        self.ui.actionMarkdown2opml.triggered.connect(self.file_export_markdown2opml)
        self.ui.actionHtml2Markdown.triggered.connect(self.file_export_html2markdown)
        self.ui.actionMarkdown2html.triggered.connect(self.file_export_md2latex)
        self.ui.actionOpml2html.triggered.connect(self.file_export_opml2html)
        self.ui.actionHtml2opml.triggered.connect(self.file_export_html2opml)
        self.ui.actionHtml2Latex.triggered.connect(self.file_export_html2latex)
        self.ui.actionLatex2html.triggered.connect(self.file_export_latex2html)
        self.ui.actionMarkdown2Lyx.triggered.connect(self.file_export_markdown2lyx)
        self.ui.ButtonConvert.clicked.connect(self.event_triggered)
        self.ui.actionPreferences.triggered.connect(self.event_dialog)
        self.ui.actionHelp.triggered.connect(self.help_dialog)
        self.ui.actionSave.setEnabled(True)


        settings = QSettings('Pandoc', 'PanConvert')

        From_Markdown = settings.value('From_Markdown', False)
        From_Html = settings.value('From_Html', False)
        From_Latex = settings.value('From_Latex', False)
        From_Opml = settings.value('From_Opml', False)

        To_Markdown = settings.value('To_Markdown', False)
        To_Html = settings.value('To_Html', False)
        To_Latex = settings.value('To_Latex', False)
        To_Opml = settings.value('To_Opml', False)
        To_Lyx = settings.value('To_Lyx', False)


        if platform.system() == 'Windows' or platform.system() == 'Linux':
            self.ui.ButtonFromMarkdown.setChecked(strtobool(From_Markdown))
            self.ui.ButtonFromHtml.setChecked(strtobool(From_Html))
            self.ui.ButtonFromLatex.setChecked(strtobool(From_Latex))
            self.ui.ButtonFromOpml.setChecked(strtobool(From_Opml))
            self.ui.ButtonToMarkdown.setChecked(strtobool(To_Markdown))
            self.ui.ButtonToHtml.setChecked(strtobool(To_Html))
            self.ui.ButtonToLatex.setChecked(strtobool(To_Latex))
            self.ui.ButtonToOpml.setChecked(strtobool(To_Opml))
            self.ui.ButtonToLyx.setChecked(strtobool(To_Lyx))

        else:
            self.ui.ButtonFromMarkdown.setChecked(From_Markdown)
            self.ui.ButtonFromHtml.setChecked(From_Html)
            self.ui.ButtonFromLatex.setChecked(From_Latex)
            self.ui.ButtonFromOpml.setChecked(From_Opml)
            self.ui.ButtonToMarkdown.setChecked(To_Markdown)
            self.ui.ButtonToHtml.setChecked(To_Html)
            self.ui.ButtonToLatex.setChecked(To_Latex)
            self.ui.ButtonToOpml.setChecked(To_Opml)
            self.ui.ButtonToLyx.setChecked(To_Lyx)



    """External Dialog Windows - Trigger Functions"""

    def help_dialog(self):
        import webbrowser
        systempath = os.getcwd()
        webbrowser.open_new('file://' + systempath + '/source/help.html')

    def event_dialog(self):
        """ References to dialog_preferences.py"""
        self.PreferenceDialog = PreferenceDialog(self)
        self.PreferenceDialog.show()



    """Gui-Trigger-Function for RadioButtons"""

    def event_triggered(self):
        global fromFormat,toFormat,extraParameter
        fromFormat = self.ui.FromParameter.text()
        toFormat = self.ui.ToParameter.text()
        standard_conversion = self.ui.StandardConversion.isChecked()
        extraParameter = self.ui.ExtraParameter.text()

        if standard_conversion is True:
            if self.ui.ButtonFromMarkdown.isChecked() is True and self.ui.ButtonToLatex.isChecked() is True:
                self.file_export_md2latex()
            elif self.ui.ButtonFromMarkdown.isChecked() is True and self.ui.ButtonToOpml.isChecked() is True:
                self.file_export_markdown2opml()
            elif self.ui.ButtonFromMarkdown.isChecked() is True and self.ui.ButtonToLyx.isChecked() is True:
                self.file_export_markdown2lyx()
            elif self.ui.ButtonFromOpml.isChecked() is True and self.ui.ButtonToMarkdown.isChecked() is True:
                self.file_export_opml2markdown_pandoc()
            elif self.ui.ButtonFromOpml.isChecked() is True and self.ui.ButtonToLatex.isChecked() is True:
                self.file_export_opml2latex()
            elif self.ui.ButtonFromLatex.isChecked() is True and self.ui.ButtonToMarkdown.isChecked() is True:
                self.file_export_latex2markdown()
            elif self.ui.ButtonFromLatex.isChecked() is True and self.ui.ButtonToOpml.isChecked()is True:
                self.file_export_latex2opml()
            elif self.ui.ButtonFromHtml.isChecked() is True and self.ui.ButtonToMarkdown.isChecked() is True:
                self.file_export_html2markdown()
            elif self.ui.ButtonFromMarkdown.isChecked() is True and self.ui.ButtonToHtml.isChecked() is True:
                self.file_export_markdown2html()
            elif self.ui.ButtonFromOpml.isChecked() is True and self.ui.ButtonToHtml.isChecked() is True:
                self.file_export_opml2html()
            elif self.ui.ButtonFromHtml.isChecked() is True and self.ui.ButtonToOpml.isChecked() is True:
                self.file_export_html2opml()
            elif self.ui.ButtonFromLatex.isChecked() is True and self.ui.ButtonToHtml.isChecked() is True:
                self.file_export_latex2html()
            elif self.ui.ButtonFromHtml.isChecked() is True and self.ui.ButtonToLatex.isChecked() is True:
                self.file_export_html2latex()
            else:
                QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                              'The from-Format and to-Format should not be identical.<br><br> '
                                              'If you picket to-Lyx, only from-markdown is a valid option.<br><br>'
                                              'Please make a different choice.')
        elif fromFormat is "" or toFormat is "":
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                          'If you fill in Arguments and uncheck the Box "Standard", you have to '
                                          'provide at least the following Parameters: From, To. <br><br>'
                                          '  Some Formats like odt, epub need an input '
                                          'for "Parameter". Otherwise there will be no output at all')
        elif fromFormat is not "" and toFormat is not "":# and extraParameter is not "":
            self.file_export_manualconverter()

        else:
            QtWidgets.QMessageBox.warning(None, 'Warning-Message',
                                              'Either is this feature not implemented at the moment,'
                                              ' or you have forgotten the extra Parameter for odt, epub Format. '
                                              ' Please consult the help - System for more Information')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myapp = StartQT5()
    myapp.show()
    sys.exit(app.exec_())