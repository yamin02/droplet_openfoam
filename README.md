$ blockMesh 

$ setFields

$ decomposePar

$ mpirun -np 8 interFoam -parallel

$ reconstructParMesh   # for dynamic Mesh only

$ reconstructPar 

$ paraFoam

<aside>
💡 To get the 3D view  :  open Paraview then filters >alphabetic > isoVolume , then set min and max value of alpha.water

</aside>
