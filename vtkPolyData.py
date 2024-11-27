import vtk

# Geometri
points = vtk.vtkPoints()
points.InsertNextPoint(1, 1, 1)
points.InsertNextPoint(1, -1, 1)
points.InsertNextPoint(-1, -1, 1)
points.InsertNextPoint(-1, 1, 1)
points.InsertNextPoint(1, 1, -1)
points.InsertNextPoint(1, -1, -1)
points.InsertNextPoint(-1, -1, -1)
points.InsertNextPoint(-1, 1, -1)

# Topoloji
faces = vtk.vtkCellArray()

# Ön Yüz
faces.InsertNextCell(4)
faces.InsertCellPoint(0)
faces.InsertCellPoint(1)
faces.InsertCellPoint(2)
faces.InsertCellPoint(3)

# Arka Yüz
faces.InsertNextCell(4)
faces.InsertCellPoint(4)
faces.InsertCellPoint(5)
faces.InsertCellPoint(6)
faces.InsertCellPoint(7)

# Sağ Yüz
faces.InsertNextCell(4)
faces.InsertCellPoint(0)
faces.InsertCellPoint(1)
faces.InsertCellPoint(5)
faces.InsertCellPoint(4)

# Sol Yüz
faces.InsertNextCell(4)
faces.InsertCellPoint(2)
faces.InsertCellPoint(3)
faces.InsertCellPoint(7)
faces.InsertCellPoint(6)

# Üst Yüz
faces.InsertNextCell(4)
faces.InsertCellPoint(0)
faces.InsertCellPoint(4)
faces.InsertCellPoint(7)
faces.InsertCellPoint(3)

# Alt Yüz
faces.InsertNextCell(4)
faces.InsertCellPoint(1)
faces.InsertCellPoint(2)
faces.InsertCellPoint(6)
faces.InsertCellPoint(5)

data = vtk.vtkPolyData()
data.SetPoints(points)
data.SetPolys(faces)

mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(data)

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
