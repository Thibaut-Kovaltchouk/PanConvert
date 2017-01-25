__author__ = 'apaeffgen'
# _*_ coding: utf-8 _*_
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

import sys

from cx_Freeze import setup, Executable

from source.language.messages import *

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

includefiles = ['source/language/Panconvert_de.qm, source/language/Panconvert_es.qm']

options = {
    'build_exe': {
        'includes': ['PyQt5.QtNetwork',
                     'PyQt5.QtWebKit',
                     'PyQt5.QtPrintSupport',
                     'PyQt5.QtNetwork',
                     'PyQt5.QtWidgets']

    }
}

executables = [
    Executable('Panconvert.py', base=base)
]

setup(name='PanConvert',
      version=versionnumber,
      description=versionname,
      options=options,
      executables=executables
      )