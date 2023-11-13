import maya.cmds as cmds
import random

def duplicate_and_disperse(num_duplicates, minX, maxX, minY, maxY, minZ, maxZ):

    # make sure there are objects selected
    selected_objects = cmds.ls(selection=True)
    if not selected_objects:
        print("No objects selected. Please select objects to duplicate.")
        return

    # Iterate over the number of duplicates required
    for _ in range(num_duplicates):
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

# Example usage
duplicate_and_disperse(8, -10, 10, -5, 5, -3, 3)
