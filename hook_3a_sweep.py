# [Imports]
from build123d import *

from ocp_vscode import *
from rich import print 
from pathlib import Path 
from math import sin, pi


# [Parameters]
from hook_2_parameters import * 

# [Functions]

from hook_1_import import import_stl_hook

def part_A():

    # height of the regular triangle 
    # 60 degrees in radians

    P_height = sin(60 * pi / 180) * P_a3


    with BuildPart() as part_A:

        if No:
            with BuildSketch(Plane.XZ) as sketch_1:
                with BuildLine() as lineB_1:
                    line_1 = Line((0.0, -P_height),(-P_a3+3.81, -P_height))
                    line_2 = Line(line_1 @ 1, (-P_a3+3.81+P_height, -P_a3/2))
                    line_3 = Line(line_2 @ 1, (-P_a3+3.81+P_height, +P_a3/2))
                    line_4 = Line(line_3 @ 1, (-P_a3+3.81, P_height))
                    line_5 = Line(line_4 @ 1, (0.0, P_height))
                    line_6 = Line( line_5 @ 1, line_1 @ 0)
                make_face()
            #aX = revolve(axis=Axis.Z, revolution_arc=90.0)

    # part_B = part_A.part.copy().move(Location([0, 0, 20])).rotate(Axis.Y, P_rotation_fails)
        with BuildSketch(Plane.XZ.offset(P_l1)) as a1:
            RegularPolygon(P_a1, 8, rotation=P_rotation)

        with BuildSketch(Plane.XZ.offset(P_l2)) as a2:
            RegularPolygon(P_a2, 8, rotation=P_rotation)
        loft()

        with BuildSketch(Plane.XZ.offset(P_l2)) as a2:
            RegularPolygon(P_a2, 8, rotation=P_rotation)
        with BuildSketch(Plane.XZ.offset(P_l3)) as a3:
            RegularPolygon(P_a3, 8, rotation=P_rotation)
        loft()

        with BuildSketch(Plane.YZ.offset(P_h3)) as b3:
            RegularPolygon(P_b2, 8, rotation=P_rotation)
        with BuildSketch(Plane.YZ.offset(P_h4)) as b4:
            RegularPolygon(P_b3, 8, rotation=P_rotation)
        loft()

        with BuildLine() as l1:
            line_1 = Line((0.0,-P_l3,0.0),(0.0,-1.0,0.0))
        with BuildSketch(Plane.XZ.offset(P_l3)) as a3:
            RegularPolygon(P_a3, 8, rotation=P_rotation)
        
        add(sweep(path=l1))

        with BuildLine() as l2:
            line_2 = JernArc((0.0,-1.0,0.0), (0.0,1.0,0.0), radius=1.0, arc_size=-90)
        plane = Plane.XZ.offset(P_l3)
        with BuildSketch(line_2 ^ 0) as a3:
            RegularPolygon(P_a3, 8, rotation=P_rotation)        
        
        a4 = sweep()
        add(a4)

        with BuildLine() as l3:
            line_3 = Line((1.0,0.0,0.0),(P_h3,0.0,0.0))
        with BuildSketch(line_3 ^ 0) as b3:
            RegularPolygon(P_b2, 8, rotation=P_rotation)        
        add(sweep(path=l3))

    return part_A, line_1, line_2, line_3

# [Main]
input = import_stl_hook()
part_A, line_1, line_2, line_3 = part_A()

show(input, part_A, line_1, line_2, line_3, names=["input", "part_A", "line_1", "line_2", "line_3" ],colors=["#FF0000AA", "#0000FFAA", "#00FF00AA", "#00FFFFAA", "#FF00FFAA", "#AA00FFAA"])

if True and  __name__ == "__main__":
    part_A.part.export_stl(f"{P_models_dir}/hook_sweep_{int(P_length)}x{int(P_height)}mm.stl")
    part_A.part.export_step(f"{P_models_dir}/hook_sweep_{int(P_length)}x{int(P_height)}mm.step")