$ blockMesh 

$ setFields

$ decomposePar

$ mpirun -np 8 interFoam -parallel

$ reconstructParMesh   # for dynamic Mesh only (no need this )

$ reconstructPar # no need this

$ paraFoam -builtin   (this can take simulation data without reconstructPar but makes it slower )

<aside>
💡 To get the 3D view  :  open Paraview then filters > alphabetic > isoVolume, then set min and max value of alpha.water
😘 First take a ruler and then get the alpha.water value then Save data from File > Save data 

</aside>
