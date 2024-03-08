import maya.cmds as cmds

class utils:
    def __init__(self):
        super(utils, self).__init__()


        print("UI_Utils initialized")


    def enable_btn(self):
        print("Button enabled")


    def make_locator(self):
        cmds.spaceLocator(n="CircleLocFront")
        cmds.scale(5, 5, 5)
        cmds.move(0, 0, 15)
        cmds.setAttr("CircleLocFront.translateX", lock=True)
        cmds.setAttr("CircleLocFront.translateY", lock=True)

        cmds.spaceLocator(n="CircleLocBack")
        cmds.setAttr("CircleLocBack.translateX", lock=True)
        cmds.setAttr("CircleLocBack.translateY", lock=True)
        cmds.scale(5, 5, 5)
        cmds.move(0, 0, -15)
        # we are grouping the locators for easier access and alignment
        cmds.group("CircleLocFront", "CircleLocBack", n="LocGRP")
        cmds.confirmDialog(m="now you have 2 locators. Place them at the two ends of your tread at z-axis")