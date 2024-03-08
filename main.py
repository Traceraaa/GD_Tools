import sys

# added path of the script to maya
sys.path.append("C:/Users/weiwe/Documents/maya/2024/scripts/site-packages/CustomModules")

from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QPushButton, QSlider, QLabel
from PySide2.QtUiTools import QUiLoader

# Gold digger scripts
from GD_Tools.rigging.CurvedRigAnimChain import CurveRigAnimChainTool
from GD_Tools.utils import arm_utils
from GD_Tools.utils import View
# initialization of tools
# curve_chain_tool = CurveRigAnimChainTool()


class UI_MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super(UI_MainWindow, self).__init__()

        self.setWindowTitle('GD Tools')

        self.buildUi()

        # Set the UI geometry (if UI is not centered/visible)
        self.widget.setGeometry(0, 0, self.widget.width(), self.widget.height())


        # make locator
        self.btn_make_locator = self.widget.findChild(QPushButton, "btn_initialize")
        self.btn_make_locator.clicked.connect(self.make_locator)

        # slider inetractions
        self.label_arm_pieces = self.widget.findChild(QLabel, "l_arm_pieces_value")
        self.slider_arm_pieces = self.findChild(QSlider, "horizontalSlider")
        self.slider_arm_pieces.valueChanged.connect(self.set_arm_piece_value)



    def buildUi(self):
        loader = QUiLoader()
        self.ui_path = "C:/Users/weiwe/Documents/maya/2024/scripts/site-packages/CustomModules/GD_Tools/ui/ui_gd_tool.ui"
        self.widget = loader.load(self.ui_path)

        if self.widget is not None:
            self.widget.setParent(self)
        else:
            print("Failed to load UI file")

    def make_locator(self):
        num_arm_loc = self.slider_arm_pieces.value()
        self.locator_list = arm_utils.make_locator(num_arm_loc)
        View.disable_btn(self.btn_make_locator)

    def set_arm_piece_value(self, value):
        self.label_arm_pieces.setText(str(value))
        print(self.locator_list)







    def showUI(self):
        ui = UI_MainWindow()
        ui.show()
        return ui
