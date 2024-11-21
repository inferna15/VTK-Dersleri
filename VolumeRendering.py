import vtk

reader = vtk.vtkDICOMImageReader()
reader.SetDirectoryName("Assets/Sources/beyin")
reader.Update()

mapper = vtk.vtkSmartVolumeMapper()
mapper.SetInputConnection(reader.GetOutputPort())

color = vtk.vtkColorTransferFunction()
color.AddRGBPoint(0, 0, 0, 0)
color.AddRGBPoint(50, 0.5, 0.5, 0)
color.AddRGBPoint(100, 1, 1, 1)

opacity = vtk.vtkPiecewiseFunction()
opacity.AddPoint(0, 0)
opacity.AddPoint(50, 0.2)
opacity.AddPoint(100, 0.5)

volume = vtk.vtkVolume()
volume.SetMapper(mapper)
volume.GetProperty().SetColor(color)
volume.GetProperty().SetScalarOpacity(opacity)

renderer = vtk.vtkRenderer()
renderer.AddActor(volume)
renderer.SetBackground(0,0.1,0.4)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

inter = vtk.vtkRenderWindowInteractor()
inter.SetRenderWindow(window)

window.Render()
inter.Start()