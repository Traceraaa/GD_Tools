import maya.cmds as cmds


def enable_btn():
    print("Button enabled")


def make_locator(count):
    locator_list = []
    for i in range(1, count + 2):
        newLoc = cmds.spaceLocator(n="Armlocator_{}".format(i), p=(0, 0, i * 5))
        cmds.scale(3, 3, 3)
        cmds.CenterPivot()
        locator_list.append(newLoc[0])
    return locator_list