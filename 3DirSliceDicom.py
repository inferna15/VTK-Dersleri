import vtk

reader = vtk.vtkDICOMImageReader()
reader.SetDirectoryName("Assets/Sources/beyin")
reader.Update()

extent = reader.GetDataExtent()
spacing = reader.GetDataSpacing()

reslice = vtk.vtkImageReslice()
reslice.SetOutputDimensionality(2)
reslice.SetInputConnection(reader.GetOutputPort())

position = [(extent[1] + extent[0]) / 2, (extent[3] + extent[2]) / 2, (extent[5] + extent[4]) / 2]

reslice.SetResliceAxesOrigin(position[0] * spacing[0], 
                             position[1] * spacing[1], 
                             position[2] * spacing[2])
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

state = "Y"

def func(obj, event):
    global state
    key = obj.GetKeySym()

    if key == "x" or key == "X":
        reslice.SetResliceAxesDirectionCosines(0,1,0,0,0,1,1,0,0)
        state = "X"
    elif key == "y" or key == "Y":
        reslice.SetResliceAxesDirectionCosines(1,0,0,0,0,1,0,1,0)
        state = "Y"
    elif key == "z" or key == "Z":
        reslice.SetResliceAxesDirectionCosines(1,0,0,0,1,0,0,0,1)
        state = "Z"

    if key == "Up":
        if state == "X":
            position[0] += 1
        if state == "Y":
            position[1] += 1
        if state == "Z":
            position[2] += 1
    if key == "Down":
        if state == "X":
            position[0] -= 1
        if state == "Y":
            position[1] -= 1
        if state == "Z":
            position[2] -= 1

    reslice.SetResliceAxesOrigin(position[0] * spacing[0], 
                                 position[1] * spacing[1], 
                                 position[2] * spacing[2])

    window.Render() 

inter.AddObserver("KeyPressEvent", func)

window.Render()
inter.Start()