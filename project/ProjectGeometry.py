import calfem.geometry as cfg
import calfem.mesh as cfm

import calfem.utils as cfu

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('TkAgg')

import calfem.vis_mpl as cfv

import numpy as np

# Mesh data
el_sizef, el_type, dofs_pn = 0.2, 2, 1
mesh_dir = "."

#Boundary Markers
MARKER_SYMMETRY = 0
MARKER_Q_IN = 1
MARKER_Q_OUT = 2
MARKER_NEWTON = 3
MARKER_MATERIAL_BOUNDARY = 4

def generate_mesh(show_geometry: bool):
    g = cfg.geometry()
    g.point([0, 0], 1) #FICK FRÅN SIXTEN
    g.point([0.7, 0], 2) #FICK FRÅN SIXTEN
    g.point([0.7, 0.3], 3) #FICK FRÅN SIXTEN
    g.point([1.4, 0.3], 4) #FICK FRÅN SIXTEN
    g.point([1.62, 0.2], 5) # Fick från Sixten om fick från isabella och samuel 
    g.point([2.04, 0.2], 6) # Fick från Sixten som fick från isabella och samuel startpunkt ellips

    g.point([3.5, 0.9], 7) #FICK FRÅN SIXTEN
    g.point([3.5, 1.2], 8) #FICK FRÅN SIXTEN
    g.point([1.99 ,0.5], 9) #Jobbig hörna
    g.point([1.4, 0.5], 10) #FICK FRÅN SIXTEN
    g.point([0, 0.5], 11) #FICK FRÅN SIXTEN


    g.point([1.4, 0], 12) #Stödcenterpunkt för cirkeln
    g.point([3.5, 0], 13) #Stödcenterpunkt för ellipsen

    g.point([2.6, 0], 14) #Stödmaxpunkt för ellipsen

    g.spline([1, 2], 1, marker = MARKER_SYMMETRY)
    g.spline([2, 3], 2, marker = MARKER_Q_IN)
    g.spline([3, 4], 3, marker = MARKER_Q_IN)
    g.circle([4, 12, 5], 4, marker = MARKER_Q_IN)
    g.spline([5, 6], 5, marker = MARKER_Q_IN)
    g.ellipse([6, 13, 14, 7], 6, marker = MARKER_Q_IN)

    g.spline([7,8], 7, marker = MARKER_NEWTON)

    g.ellipse([8, 13, 14, 9], 8, marker = MARKER_NEWTON)

    g.spline([9, 10], 9, marker = MARKER_NEWTON)
    g.spline([10,11], 10, marker = MARKER_Q_OUT)
    g.spline([11,1], 11, marker = MARKER_Q_OUT)

    g.spline([10, 4], 12, marker = MARKER_MATERIAL_BOUNDARY)

    #Generate mesh
    g.surface([1,2,3,12,10,11])
    g.surface([4,5,6,7,8,9,12])

    mesh = cfm.GmshMeshGenerator(g, mesh_dir=mesh_dir)
    mesh.el_size_factor = el_sizef
    mesh.el_type = el_type
    mesh.dofs_per_node = dofs_pn
    coord, edof, dofs, bdofs, element_markers = mesh.create()


    if show_geometry:
        fig, ax = plt.subplots()
        cfv.draw_geometry(g, label_curves=True, title="Rocket nozzle")
        cfv.draw_mesh(coord, edof, dofs_per_node = mesh.dofs_per_node, el_type = mesh.el_type)
        plt.show()
    
    #Boundary conditions (Än så länge inte lagt in något)
    bc, bc_value = np.array([], 'i'), np.array([], 'f')

    #Return
    return (coord, edof, dofs, bdofs, bc, bc_value, element_markers)
    




if __name__=="__main__":
    generate_mesh(show_geometry=True)


