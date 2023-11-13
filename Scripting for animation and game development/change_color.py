import maya.cmds as cmds

def change_color(color_index):
    """
    Changes the override color for the shape node of the selected objects.

    Args:
    color_index (int): The index of the color to set. Should be a value between 0 and 31.
    """
    # Check if the color index is within the valid range
    if not (0 <= color_index <= 31):
        print("Invalid color index. Please provide a value between 0 and 31.")
        return

    # Get the currently selected objects
    selected_objects = cmds.ls(selection=True)

    # Loop through each selected object
    for obj in selected_objects:
        # Get the shape node of the object
        shapes = cmds.listRelatives(obj, shapes=True)
        if not shapes:
            print(f"No shape node found for object {obj}.")
            continue

        # Loop through each shape node and set the override color
        for shape in shapes:
            cmds.setAttr(f"{shape}.overrideEnabled", 1)
            cmds.setAttr(f"{shape}.overrideColor", color_index)

# Example usage
change_color(6)
