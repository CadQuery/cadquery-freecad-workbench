# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2014 CadQuery Developers
# SPDX-FileNotice: Part of the CadQuery addon.

"""
CadQuery GUI init module for FreeCAD
This adds a workbench with a scripting editor to FreeCAD's GUI.
"""

from FreeCAD import Gui

from .Command import (
    CadQueryHelp,
    CadQueryClearOutput,
    CadQueryStableInstall,
    CadQueryUnstableInstall,
    Build123DInstall
)


class CadQueryWorkbench (Gui.Workbench):
    """CadQuery workbench for FreeCAD"""

    MenuText = "CadQuery"
    ToolTip = "CadQuery workbench"


    def Initialize(self):
        self.appendMenu('CadQuery', ['CadQueryClearOutput'])
        self.appendMenu(['CadQuery', 'Install'], ["CadQueryStableInstall",
                                                  "CadQueryUnstableInstall",
                                                  "Build123DInstall"])
        self.appendMenu('CadQuery', ['CadQueryHelp'])


    def Activated(self):
        pass


    def Deactivated(self):
        pass



Gui.addCommand('CadQueryStableInstall', CadQueryStableInstall())
Gui.addCommand('CadQueryUnstableInstall', CadQueryUnstableInstall())
Gui.addCommand('Build123DInstall', Build123DInstall())
Gui.addCommand('CadQueryClearOutput', CadQueryClearOutput())
Gui.addCommand('CadQueryHelp', CadQueryHelp())

Gui.addWorkbench(CadQueryWorkbench())
