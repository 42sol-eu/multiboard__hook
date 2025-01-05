from build123d import *

from ocp_vscode import *
from rich import print 
from pathlib import Path 


# [Parameters]
from hook_2_parameters import * 

from hook_1_import import import_stl_hook

def part_A():
    with BuildPart() as part_A:
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

        #TODO: fix the corner part after understanding why neither sweep nor revolve works.
        #HINT: maybe create a custom solid with the edges from a3 and b2        
        if No:
            with BuildLine() as l2:
                line_2 = JernArc((0.0,-1.0,0.0), (0.0,1.0,0.0), radius=1.0, arc_size=-90)
                #line_2 = Line((0.0,-1.0,0.0),(1.0,0.0,0.0))
            plane = Plane.XZ.offset(P_l3)
            with BuildSketch(Plane.XZ) as a3:
                RegularPolygon(P_a3, 8, rotation=P_rotation)
                with Locations(Location([P_a3/2.0+2,0.0,  0.0])):
                    Rectangle(6.0,20.0, mode=Mode.SUBTRACT)
        
        
            a4 = revolve(axis=Axis.X, revolution_arc=90.0)
            add(a4)

        with BuildLine() as l3:
            line_3 = Line((1.0,0.0,0.0),(P_h3,0.0,0.0))
        with BuildSketch(Plane.YZ.offset(P_h3)) as b3:
            RegularPolygon(P_b2, 8, rotation=P_rotation)
        
        add(sweep(path=l3))
        bX = part_A.faces().sort_by(Axis.X).first 
        c3a = bX.vertices()[1]
        bX1 = bX.vertices()[3]
    return part_A, a1, a2, a3, l3, bX1, l1

# [Main]
input = import_stl_hook()
part_A, a1, a2, a3, l3, b3, l1 = part_A()

show(input, part_A, b3, l3, l1, names=["input", "part_A", "b3", "l3", "l1" ],colors=["#FF0000AA", "#0000FFAA", "#00FF00AA", "#00FFFFAA", "#FF00FFAA", "#AA00FFAA"])


bounding_box = part_A.part.bounding_box()
length = bounding_box.max.X - bounding_box.min.X 

if True and  __name__ == "__main__":
    part_A.part.export_stl(f"./models/hook_sweep_{int(length)}mm.stl")
    part_A.part.export_step(f"./models/hook_sweep_{int(length)}mm.step")