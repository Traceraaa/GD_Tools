import sys

# added path of the script to maya
sys.path.append("C:/Users/weiwe/Documents/maya/2024/scripts/site-packages/CustomModules")

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QPushButton
from PySide2.QtUiTools import QUiLoader

# Gold digger scripts
from GD_Tools.rigging.CurvedRigAnimChain import CurveRigAnimChainTool
from GD_Tools.utils.arm_utils import utils

from GD_Tools.GD_Tools.rigging
# initialization of tools
# curve_chain_tool = CurveRigAnimChainTool()


class UI_MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(UI_MainWindow, self).__init__()

        self.setWindowTitle('GD Tools')

        self.buildUi()

        # Set the UI geometry (if UI is not centered/visible)
        self.widget.setGeometry(0, 0, self.widget.width(), self.widget.height())


        # UI element storage section
        self.btn_make_locator = self.widget.findChild(QPushButton, "btn_initialize")

        # signals
        self.btn_make_locator.clicked.connect(self.make_locator)

    def buildUi(self):
        loader = QUiLoader()
        self.ui_path = "C:/Users/weiwe/Documents/maya/2024/scripts/site-packages/Test/GD_Tools/ui/ui_gd_tool.ui"
        self.widget = loader.load(self.ui_path)

        if self.widget is not None:
            self.widget.setParent(self)
        else:
            print("Failed to load UI file")

    def make_locator(self):
        utils.make_locator(self)





    def showUI(self):
        ui = UI_MainWindow()
        ui.show()
        return ui