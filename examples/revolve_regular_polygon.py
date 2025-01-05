# [Imports]
from build123d import *
from ocp_vscode import show, show_all

P_a3 = 14.7 / 2.0
P_rotation_fails = 157.5 # use this for the regular polygon and the rotate will fail.
P_rotation_works = 45.0
P_plane_fails = Plane.XZ.offset(10)
P_plane_works = Plane.XZ
with BuildPart() as part_A:
    with BuildSketch(Plane.XZ) as sketch_1:
        RegularPolygon(P_a3, 8, rotation=P_rotation_works) #, rotation=P_rotation)
    revolve(axis=Axis.Z, revolution_arc=360.0)

part_B = part_A.part.copy().move(Location([0, 0, 20])).rotate(Axis.Y, P_rotation_fails)
show_all()