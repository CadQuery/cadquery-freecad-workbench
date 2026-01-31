# SPDX-License-Identifier: Apache-2.0
# SPDX-FileNotice: Part of the CADQuery addon.


from .Qt.Core import Slot , Qt

from .Qt.Widgets import (
    QDialogButtonBox ,
    QDialog , QLabel ,
    QGridLayout
)

class HelpDialog(QDialog):
    def __init__(self, parent=None):
        super(HelpDialog, self).__init__(parent)
        self.resize(300, 200)
        self.setWindowTitle('Help')
        self.initUI()

    def initUI(self):
        import cadquery

        # Introduction to CadQuery line
        intro_label = QLabel('CadQuery is a parametric scripting API for creating CAD models and assemblies.')
        intro_label.setWordWrap(True)

        # CadQuery version
        cadquery_ver = cadquery.__version__
        version_label = QLabel('CadQuery Version: ' + cadquery_ver)

        # CadQuery contributors
        cq_contribs = QLabel('Authors: CadQuery Developers')

        # CadQuery documentation link
        cq_docs_link = QLabel('- <a href="https://cadquery.readthedocs.io">CadQuery Documentation</a>')
        cq_docs_link.setOpenExternalLinks(True)

        # FreeCAD workbench documentation link
        wb_docs_link = QLabel('- <a href="https://github.com/CadQuery/cadquery-freecad-workbench/tree/master/docs">Workbench Documentation</a>')
        wb_docs_link.setOpenExternalLinks(True)

        self.buttons = QDialogButtonBox()
        self.buttons.setOrientation(Qt.Orientation.Horizontal)
        self.buttons.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        self.buttons.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.buttons.accepted.connect(self.closeHelp)

        grid = QGridLayout()
        grid.setContentsMargins(10, 10, 10, 10)
        grid.addWidget(intro_label, 0, 0)
        grid.addWidget(version_label, 1, 0)
        grid.addWidget(cq_contribs, 2, 0)
        grid.addWidget(cq_docs_link, 3, 0)
        grid.addWidget(wb_docs_link, 4, 0)
        grid.addWidget(self.buttons, 5, 0)

        self.setLayout(grid)

    @Slot(int)
    def closeHelp(self):
        self.accept()
