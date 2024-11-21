import vtk

cube = vtk.vtkCubeSource()
cube.SetXLength(5)
cube.SetYLength(5)
cube.SetZLength(5)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(cube.GetOutputPort())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

inter = vtk.vtkRenderWindowInteractor()
inter.SetRenderWindow(window)

window.Render()
inter.Start()

