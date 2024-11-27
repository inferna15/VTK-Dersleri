import vtk

reader = vtk.vtkDICOMImageReader()
reader.SetDirectoryName("Assets/Sources/beyin")
reader.Update()

extent = reader.GetDataExtent()
spacing = reader.GetDataSpacing()

reslice = vtk.vtkImageReslice()
reslice.SetOutputDimensionality(2)
reslice.SetInputConnection(reader.GetOutputPort())
reslice.SetResliceAxesOrigin((extent[1] + extent[0]) / 2 * spacing[0], 
                             (extent[3] + extent[2]) / 2 * spacing[1], 
                             (extent[5] + extent[4]) / 2 * spacing[2])
#reslice.SetResliceAxesDirectionCosines(1,0,0,0,1,0,0,0,1) # Z ekseni
#reslice.SetResliceAxesDirectionCosines(0,0,1,0,1,0,1,0,0) # X ekseni
reslice.SetResliceAxesDirectionCosines(1,0,0,0,0,1,0,1,0) # Y ekseni

mapper = vtk.vtkImageMapper()
mapper.SetInputConnection(reslice.GetOutputPort())
mapper.SetColorWindow(100)
mapper.SetColorLevel(50)

actor = vtk.vtkActor2D()
actor.SetMapper(mapper)

renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

window = vtk.vtkRenderWindow()
window.AddRenderer(renderer)

inter = vtk.vtkRenderWindowInteractor()
inter.SetRenderWindow(window)

window.Render()
inter.Start()