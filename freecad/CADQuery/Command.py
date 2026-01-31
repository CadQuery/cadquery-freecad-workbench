# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: 2014 CADQuery Developers
# SPDX-FileNotice: Part of the CADQuery addon.

"""Adds all of the commands that are used for the menus of the CadQuery module"""

from FreeCAD import Gui

from .Qt.Widgets import QDockWidget
from .HelpDialog import HelpDialog

class CadQueryStableInstall:
    """
    Allows the user to easily attempt a manual install of the stable version of CadQuery
    """

    def GetResources(self):
        return {"MenuText": "Install CadQuery Stable",
                "Accel": "",
                "ToolTip": "Installs the stable version of CadQuery",
                "Pixmap": ":/icons/preferences-system.svg"}

    def IsActive(self):
        return True

    def Activated(self):
        import subprocess
        print("Starting to install CadQuery stable...")
        subprocess.run(["python", "-m", "pip", "install", "--upgrade", "cadquery==2.5.2"], capture_output=False)
        subprocess.run(["python", "-m", "pip", "install", "--upgrade", "cadquery-ocp==7.7.2"], capture_output=False)
        print("CadQuery stable has been installed! Please restart FreeCAD.")


class CadQueryUnstableInstall:
    """
    Allows the user to easily attempt a manual install of the unstable version of CadQuery
    """

    def GetResources(self):
        return {"MenuText": "Install CadQuery Unstable",
                "Accel": "",
                "ToolTip": "Installs the unstable version of CadQuery",
                "Pixmap": ":/icons/preferences-system.svg"}

    def IsActive(self):
        return True

    def Activated(self):
        print("Starting to install CadQuery unstable...")
        import subprocess
        subprocess.run(["python", "-m", "pip", "uninstall", "-y", "vtk"], capture_output=False)
        subprocess.run(["python", "-m", "pip", "uninstall", "-y", "cadquery-vtk"], capture_output=False)
        subprocess.run(["python", "-m", "pip", "install", "--upgrade", "vtk==9.3.1"], capture_output=False)
        subprocess.run(["python", "-m", "pip", "uninstall", "-y", "cadquery-ocp"], capture_output=False)
        subprocess.run(["python", "-m", "pip", "install", "--upgrade", "cadquery-ocp==7.8.1.0"], capture_output=False)
        subprocess.run(["python", "-m", "pip", "install", "--upgrade", "https://github.com/CadQuery/cadquery.git"], capture_output=False)
        print("CadQuery unstable has been installed! Please restart FreeCAD.")


class Build123DInstall:
    """
    Allows the user to easily attempt a manual install of Build123D
    """

    def GetResources(self):
        return {"MenuText": "Install Build123d",
                "Accel": "",
                "ToolTip": "Installs Build123d",
                "Pixmap": ":/icons/preferences-system.svg"}

    def IsActive(self):
        return True

    def Activated(self):
        import subprocess
        print("Starting to install Build123d...")
        subprocess.run(["python", "-m", "pip", "install", "--upgrade", "build123d"], capture_output=False)
        subprocess.run(["python", "-m", "pip", "install", "--upgrade", "cadquery-ocp==7.8.1.1.post1"], capture_output=False)
        print("Build123d has been installed! Please restart FreeCAD.")


class CadQueryClearOutput:
    """Allows the user to clear the reports view when it gets overwhelmed with output"""

    def GetResources(self):
        return {"MenuText": "Clear Output",
                "Accel": "Shift+Alt+C",
                "ToolTip": "Clears the script output from the Reports view",
                "Pixmap": ":/icons/button_invalid.svg"}

    def IsActive(self):
        return True

    def Activated(self):
        # Grab our main window so we can interact with it
        mw = Gui.getMainWindow()

        reportView = mw.findChild(QDockWidget, "Report view")

        if not reportView:
            return
        
        # Clear the view because it gets overwhelmed sometimes and won't scroll to the bottom
        widget = reportView.widget()
        widget.clear()


class CadQueryHelp:
    """Opens a help dialog, allowing the user to access documentation and information about CadQuery"""

    def GetResources(self):
        return {"MenuText": "Help",
                "Accel": "",
                "ToolTip": "Opens the Help dialog",
                "Pixmap": ":/icons/help-browser.svg"}

    def IsActive(self):
        return True

    def Activated(self):
        win = HelpDialog()

        win.exec_()
