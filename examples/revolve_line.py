# [Imports]
from build123d import *
from ocp_vscode import show, show_all
from math import sin, pi
# [Parameters]
P_a3 = 14.7 / 2.0

# height of the regular triangle 
# 60 degrees in radians

P_height = sin(60 * pi / 180) * P_a3

P_rotation_fails = 157.5
P_rotation_works = 45.0
P_plane_fails = Plane.XZ.offset(10)
P_plane_works = Plane.XZ
with BuildPart() as part_A:
    with BuildSketch(Plane.XZ) as sketch_1:
        with BuildLine() as lineB_1:
            line_1 = Line((-P_a3, 0.0, 0.0),(-P_a3, 0.0, P_a3))
            line_2 = Line(line_1 @ 1, (0.0, 0.0, P_a3+P_height))
            line_3 = Line(line_2 @ 1, (+P_a3, 0.0, P_a3+P_height))
            line_4 = Line(line_3 @ 1, (P_a3+P_height, 0.0, P_a3))
            line_5 = Line(line_4 @ 1, (P_a3+P_height, 0.0, 0.0))
            line_6 = Line( line_5 @ 1, line_1 @ 0)
        make_face()
    revolve(axis=Axis.X, revolution_arc=90.0)

# part_B = part_A.part.copy().move(Location([0, 0, 20])).rotate(Axis.Y, P_rotation_fails)
show_all()