import vtk

reader = vtk.vtkOBJReader()
reader.SetFileName("Assets/Sources/kedi.obj")
reader.Update()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())


tex_reader = vtk.vtkJPEGReader()
tex_reader.SetFileName("Assets/Textures/kedi.jpg")
tex_reader.Update()

texture = vtk.vtkTexture()
texture.SetInputConnection(tex_reader.GetOutputPort())


actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.SetTexture(texture)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

inter = vtk.vtkRenderWindowInteractor()
inter.SetRenderWindow(window)

window.Render()
inter.Start()