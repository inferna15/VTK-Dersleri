import vtk

cube = vtk.vtkCubeSource()
cube.SetXLength(5)
cube.SetYLength(5)
cube.SetZLength(5)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cube.GetOutputPort())

transform = vtk.vtkTransform()

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.SetUserTransform(transform)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

inter = vtk.vtkRenderWindowInteractor()
inter.SetRenderWindow(window)

degreeZ = 0
degreeX = 0

def rotate(obj, event):
    global degreeZ
    global degreeX
    key = obj.GetKeySym()

    if key == "Right":
        degreeZ -= 1
    if key == "Left":
        degreeZ += 1
    if key == "Up":
        degreeX -= 1
    if key == "Down":
        degreeX += 1

    transform.Identity()
    transform.RotateZ(degreeZ)
    transform.RotateX(degreeX)
    window.Render()


inter.AddObserver("KeyPressEvent", rotate)

window.Render()
inter.Start()