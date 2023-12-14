import maya.cmds as cmds

def change_color(color_index):

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

def create_color_changer_ui():
    # Check if the window exists
    if cmds.window("colorChangerUI", exists=True):
        cmds.deleteUI("colorChangerUI", window=True)

    # Create the window
    cmds.window("colorChangerUI", title="Color Changer UI", widthHeight=(400, 120))

    # Create a layout
    cmds.columnLayout(adjustableColumn=True)

    # UI elements
    color_index_slider = cmds.intSliderGrp(field=True, label="Color Index:",
                                           minValue=0, maxValue=31, value=0,
                                           fieldMinValue=0, fieldMaxValue=31,
                                           columnWidth=[(1, 100), (2, 50), (3, 250)])  # Adjust column widths

    # Function to handle slider change
    def on_slider_change(*args):
        slider_value = cmds.intSliderGrp(color_index_slider, query=True, value=True)
        change_color(slider_value)

    # Button to execute the function
    cmds.button(label="Zhu Li do the thing!", command=on_slider_change)

    # Show the window
    cmds.showWindow("colorChangerUI")

# Call the function to create the UI
create_color_changer_ui()
