import vtk

reader = vtk.vtkSTLReader()
reader.SetFileName("Assets/Sources/Dragon 2.5_stl.stl")
reader.Update()

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(reader.GetOutputPort())

property = vtk.vtkProperty()
property.SetColor(0.5,0.5,0.5)
property.LightingOn()
property.SetMetallic(25)
property.SetRoughness(25)
property.SetSpecular(1)
property.SetSpecularPower(25)
property.SetOpacity(1)
property.SetSpecularColor(1,0,0)
property.SetEdgeColor(0,0,1)
property.ShadingOn()

actor = vtk.vtkActor()
actor.SetMapper(mapper)
actor.SetProperty(property)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

inter = vtk.vtkRenderWindowInteractor()
inter.SetRenderWindow(window)

window.Render()
inter.Start()