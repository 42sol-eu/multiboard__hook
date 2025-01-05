from build123d import *
from build123d import importers
from rich import print 
from pathlib import Path 
from build123d.mesher import Mesher

P_file_step = "15 x 7.5 mm, Push-Fit Hook.step"
P_file_stl  = "15 x 7.5 mm, Push-Fit Hook.stl"



from ocp_vscode import *
set_defaults(reset_camera=Camera.CENTER, helper_scale=5)

importer = Mesher()
hook = importer.read(P_file_stl)
print(
    f"{hook[0].bounding_box()}, {type(hook[0])}"
)

x, y, z = hook[0].center()
x_diff = hook[0].bounding_box().max.X - hook[0].bounding_box().min.X
y_diff = abs( hook[0].bounding_box().min.Y - hook[0].bounding_box().max.Y)
z_diff = hook[0].bounding_box().max.Z - hook[0].bounding_box().min.Z

hook[0].move(Location([-x-1.94, -y+1.58, -z]))
hook[0].rotate(Axis.X, 90)
b = Box(5.59, 30.55, z_diff+0.1)
b = b.move(Location([-3.75, -1.74, 0]))

c = Box(14.72, 5.59, z_diff+0.1)
c = c.move(Location([3.08, 10.75, 0]))

P_radius_main = 14.7 / 2.0
P_radius_front = 9.2 / 2.0
P_y_top_part = 2.5 + 1.95  
P_x_move = 3.71
P_y_connector = 5.25
P_y_move = -13.54 
P_y_length = y_diff - P_y_connector - P_y_top_part
P_radius_connector1 = 14.3 / 2.0
P_radius_connector = 13.2 / 2.0

with BuildPart() as base:
    Box(x_diff, y_diff, 5.59)
    add(b)
    add(c)

with BuildPart() as hook1:
    with BuildSketch(Plane.XZ.offset(P_y_move )) as s:
        RegularPolygon(P_radius_main,8, rotation=157.5)
        
    extrude(amount=P_y_length  )

    bottom = hook1.faces().filter_by(Axis.Y)[-1]
    top1 = hook1.faces().filter_by(Axis.Y)[0]

    with BuildSketch(Plane.XZ.offset(11.25)) as s0:
        RegularPolygon(P_radius_main, 8, rotation=157.5)

    with BuildSketch(Plane.XZ.offset(12.0+P_y_connector-0.25)) as s1a:
        RegularPolygon(P_radius_connector1, 8, rotation=157.5)

    add(loft())

    with BuildSketch(Plane.XZ.offset(12.0+P_y_connector-0.25)) as s1a:
        RegularPolygon(P_radius_connector1, 8, rotation=157.5)

    with BuildSketch(Plane.XZ.offset(12.0+P_y_connector)) as s1:
        RegularPolygon(P_radius_connector, 8, rotation=157.5)

    add(loft())

    with BuildSketch(Plane(Location([0,12.3,0])).offset(-2.8-3.89)) as s2:
        RegularPolygon(3.1, 8, rotation=157.5)

    with BuildSketch(Plane(Location([0,10.73,0])).offset(-2.8)) as s3:
        RegularPolygon(P_radius_main, 8, rotation=157.5)
    add(loft())

    with BuildSketch(Plane(Location([0,10.73,0])).offset(-2.8)) as s4:
        RegularPolygon(P_radius_main, 8, rotation=157.5)
    extrude(amount=12.8)

    with BuildSketch(Plane(Location([0,10.73,0])).offset(10.0)) as s5:
        RegularPolygon(P_radius_main, 8, rotation=157.5)

    with BuildSketch(Plane(Location([0,10.73,0])).offset(12.5)) as s6:
        RegularPolygon(P_radius_front, 8, rotation=157.5)

    add(loft())


    #   move(Location([-P_x_move,0,0]))
show(hook[0], hook1, s0, s1a, s1, names=["input", "hook1", "s0", "s1a", "s1" ],colors=["red", "blue", "green", "yellow", "purple"])

print(f"{x_diff=}, {y_diff=}, {z_diff=}")