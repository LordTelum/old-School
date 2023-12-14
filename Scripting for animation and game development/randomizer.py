import maya.cmds as cmds
import random

def duplicate_and_disperse(num_duplicates, minX, maxX, minY, maxY, minZ, maxZ):
    # make sure there are objects selected
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        print("No objects selected. Please select objects to duplicate.")
        return

    # Iterate over the number of duplicates required
    for i in range(num_duplicates):
        # Duplicate selected objects
        duplicates = cmds.duplicate(selected_objects)

        # For each duplicated object
        for duplicate in duplicates:
            # Generate random coordinates within the specified ranges
            randomX = random.uniform(minX, maxX)
            randomY = random.uniform(minY, maxY)
            randomZ = random.uniform(minZ, maxZ)

            # Move the duplicate to the new random location
            cmds.move(randomX, randomY, randomZ, duplicate)

# Create the UI
def create_randomizer_ui():
    # Check if the window exists
    if cmds.window("randomizerUI", exists=True):
        cmds.deleteUI("randomizerUI", window=True)

    # Create the window
    cmds.window("randomizerUI", title="Randomizer UI", widthHeight=(300, 200))

    # Create a layout
    cmds.columnLayout(adjustableColumn=True)

    # UI elements
    num_duplicates_field = cmds.intFieldGrp(label='Number of Duplicates:', value1=5)
    min_x_field = cmds.floatFieldGrp(label='Min X:', value1=-10)
    max_x_field = cmds.floatFieldGrp(label='Max X:', value1=10)
    min_y_field = cmds.floatFieldGrp(label='Min Y:', value1=-5)
    max_y_field = cmds.floatFieldGrp(label='Max Y:', value1=5)
    min_z_field = cmds.floatFieldGrp(label='Min Z:', value1=-3)
    max_z_field = cmds.floatFieldGrp(label='Max Z:', value1=3)

    # Button to execute the function
    cmds.button(label="Zhu Li do the thing!",
                command=lambda x: duplicate_and_disperse(cmds.intFieldGrp(num_duplicates_field, query=True, value1=True),
                                                        cmds.floatFieldGrp(min_x_field, query=True, value1=True),
                                                        cmds.floatFieldGrp(max_x_field, query=True, value1=True),
                                                        cmds.floatFieldGrp(min_y_field, query=True, value1=True),
                                                        cmds.floatFieldGrp(max_y_field, query=True, value1=True),
                                                        cmds.floatFieldGrp(min_z_field, query=True, value1=True),
                                                        cmds.floatFieldGrp(max_z_field, query=True, value1=True)))

    # Show the window
    cmds.showWindow("randomizerUI")

# Call the function to create the UI
create_randomizer_ui()
