$ blockMesh 

$ setFields

$ decomposePar

$ mpirun -np 8 interFoam -parallel

$ reconstructParMesh   # for dynamic Mesh only (no need this )

$ reconstructPar # no need this

$ paraFoam -builtin   (this can take simulation data without reconstructPar but makes it slower ) , select decomposed case in the dropdown


💡 To get the 3D view  :  open Paraview then filters > alphabetic >  then do the following 
  
    # Clip (will slice the mesh in a plane)
    # Isovolume will give 3d pic ( set the max value of alpha.water ) 
    # PLot over line  will give values along the length of a line
😘 Save animation or data depending on what you needd

