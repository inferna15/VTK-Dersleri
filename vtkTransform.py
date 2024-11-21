import vtk

cube = vtk.vtkCubeSource()
cube.SetXLength(5)
cube.SetYLength(5)
cube.SetZLength(5)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cube.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)


transform = vtk.vtkTransform()
transform.Translate(6,0,0)
transform.RotateY(45)
transform.Scale(0.5, 2, 1)


actor2 = vtk.vtkActor()
actor2.SetMapper(mapper)
actor2.SetUserTransform(transform)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)
renderer.AddActor(actor2)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

inter = vtk.vtkRenderWindowInteractor()
inter.SetRenderWindow(window)

window.Render()
inter.Start()