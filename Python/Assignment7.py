import maya.cmds as cmds
#print(len(cmds.ls( selection=True)))
selection = cmds.ls( selection=True)
lengthOfTheSelectionArray = len(selection)
activeObjectNumber = lengthOfTheSelectionArray - 1
activeObject = cmds.ls( selection=True )[activeObjectNumber]

activeObjectTranslation = cmds.xform(activeObject, worldSpace=True, q=True, translation=True)
activeObjectRotation = cmds.xform(activeObject, worldSpace=True, q=True, rotation=True)
for x in selection:
	cmds.xform(x, translation=activeObjectTranslation, worldSpace=True)
	cmds.xform(x, rotation=activeObjectRotation, worldSpace=True)

cmds.group(selection, name=activeObject+"_Grp")