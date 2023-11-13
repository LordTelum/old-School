import maya.cmds as cmds

#The number of spheres to stack
num_spheres = 3

# the for loop to stack the spheres

for i in range(num_spheres):
    #create a sphere
    sphere = cmds.polySphere()
    #move the sphere up
    cmds.move(0, i*1.5, 0)

# put a cylinder on top of the spheres
cylinder = cmds.polyCylinder()
cmds.move(0, num_spheres*1.5, 0)

# put a cylinder under the top scylinder to make the brim of the hat
cylinder = cmds.polyCylinder(radius=1.5, height=0.2)
cmds.move(0, num_spheres*1.2, 0)

#put a cone on the front of top sphere to make a nose
cone = cmds.polyCone(radius=0.1, height=.5)
cmds.move(0, num_spheres*1, 1)
cmds.rotate(90, 0, 0)

# Create two eyes
eye_positions = [(-0.2, 0.9), (0.2, 0.9)]  # Left and right eye positions
for pos in eye_positions:
    eye = cmds.polyCylinder(radius=0.1, height=0.2)
    cmds.move(pos[0], num_spheres * 1.05, pos[1], eye)
    cmds.rotate(90, 0, 0, eye)