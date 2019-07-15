import bpy

# Selecting objects by name
def select(objName):
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[objName].select = True

# Activating objects by name
def activate(objName):
    bpy.context.scene.objects.active = bpy.data.objects[objName]

class sel:
    """ Function Class for operating on SELECTED objects """
    
    # Differential
    def translate(v):
        bpy.ops.transform.translate(value=v, constraint_axis=(True, True, True))
    
    # Differential
    def scale(v):
        bpy.ops.transform.resize(value=v, constraint_axis=(True, True, True))
    
    # Differential
    def rotate_x(v):
        bpy.ops.transform.resize(value=v, axis=(1,0,0))
        
    # Differential
    def rotate_y(v):
        bpy.ops.transform.rotate(value=v, axis=(0,1,0))
    
    # Differential
    def rotate_z(v):
        bpy.ops.transform.rotate(value=v, axis=(0,0,1))
        
class act:
    """ Function Class for operating on ACTIVE objects """
    
    # Declarative
    def location(v):
        bpy.context.object.location = v
    
    # Declarative
    def scale(v):
        bpy.context.object.scale = v
    
    # Declarative
    def rotation(v):
        bpy.context.object.rotation_euler = v
    
    # Rename the active object
    def rename(objName):
        bpy.context.object.name = objName