import ezdxf

dwg = ezdxf.readfile("plan of skeletons.dxf")
modelspace = dwg.modelspace()
images = modelspace.query("IMAGE")

print images[1].get_boundary_path()
