def main():
    pass


if __name__ == "__main__":
    main()


import os
import math
import pychrono as chrono
import pychrono.postprocess as postprocess
import pychrono.irrlicht as chronoirr
import pychrono.vehicle as veh

from terrain_list import Soil_Params


print("Load a model exported by SolidWorks")


# ---------------------------------------------------------------------
#
#  Create the simulation system and add items
#

mysystem = chrono.ChSystemNSC()
chrono.ChCollisionModel.SetDefaultSuggestedEnvelope(0.05)
chrono.ChCollisionModel.SetDefaultSuggestedMargin(0.05)

parts = chrono.ImportSolidWorksSystem(r"D:\sunjieqiang\chrono\myrobot4\robot4")

for ib in parts:
    mysystem.Add(ib)


bbody = mysystem.SearchBody("Part3^SPIDER_ROBOT-1")

terrainli = Soil_Params(0)
terrain = veh.SCMDeformableTerrain(mysystem)
terrain.SetPlane(
    chrono.ChCoordsysD(chrono.ChVectorD(0, -2.2, 0), chrono.Q_from_AngX(-math.pi / 2))
)
terrain.Initialize(20, 20, 0.08)
terrain.SetSoilParameters(
    terrainli[0],  # Bekker Kphi
    terrainli[1],  # Bekker Kc
    terrainli[2],  # Bekker n exponent
    terrainli[3],  # Mohr cohesive limit (Pa)
    terrainli[4],  # Mohr friction limit (degrees)
    terrainli[5],  # Janosi shear coefficient (m)
    terrainli[6],  # Elastic stiffness (Pa/m), before plastic yield, must be > Kphi
    terrainli[
        7
    ],  # Damping (Pa s/m), proportional to negative vertical speed (optional)
)
terrain.SetPlotType(veh.SCMDeformableTerrain.PLOT_PRESSURE, 0, 30000.2)


myapplication = chronoirr.ChVisualSystemIrrlicht()
myapplication.AttachSystem(mysystem)
myapplication.SetWindowSize(1280, 720)
myapplication.SetWindowTitle("test")
myapplication.Initialize()


myapplication.AddSkyBox()
myapplication.AddCamera(chrono.ChVectorD(-2, 0, 1))
myapplication.AddTypicalLights()

myapplication.BindAll()


myapplication.SetShadows(True)

# ---------------------------------------------------------------------
#
#  Run the simulation
#
solver = chrono.ChSolverBB()
solver.SetMaxIterations(200)
mysystem.SetSolver(solver)
# myapplication.SetTimestep(0.001)
# mysystem.DoStepDynamics(1e-3)


while myapplication.Run():
    myapplication.BeginScene()
    myapplication.Render()
    myapplication.EndScene()
    mysystem.DoStepDynamics(1e-3)
    # print(mysystem.GetChTime(), "  ", mysystem.GetNcontacts())
    mysystem.GetCollisionSystem().Visualize(chrono.ChCollisionSystem.VIS_Shapes)
