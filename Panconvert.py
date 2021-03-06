#!/usr/bin/env python3
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

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import QPoint, QSize
from PyQt5.QtCore import QT_VERSION_STR
from PyQt5.QtCore import QLocale
from source.main_gui import *
import sys

def main():

    app = QtWidgets.QApplication(sys.argv)
    app.installTranslator(_translate)
    myapp = StartQT5()
    myapp.show ()
    sys.exit (app.exec_ () )


if __name__ == '__main__':
    import sys

    settings = QSettings('Pandoc', 'PanConvert')
    
    actualLanguage = settings.value('default_language')
    
    path_pandoc_tmp = settings.value('path_pandoc','')
    path_pandoc = str(path_pandoc_tmp)

    _translate = QtCore.QTranslator()
    script_dir = os.path.dirname(sys.argv[0])
    
    if actualLanguage in ['de','es','fr']:
        xx_language = script_dir + "/Panconvert_" + actualLanguage + ".qm"
        if os.path.isfile(xx_language):
            _translate.load(xx_language)
        else:
            path2trxx = script_dir + "/source/language/Panconvert_" + \
                        actualLanguage + ".qm"
            _translate.load(path2trxx)

    if not os.path.isfile(str(path_pandoc)):
        get_path_pandoc()

    main()
