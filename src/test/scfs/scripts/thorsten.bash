#!/bin/bash
#SBATCH -N 1
#SBATCH -C haswell
#SBATCH -p debug
#SBATCH -J dbgx28-xx
#SBATCH --mail-user=majewski@phys.ufl.edu
#SBATCH -t 00:30:00
#SBATCH --mem-per-cpu 256

ulimit -s unlimited

#OpenMP settings: 
export OMP_NUM_THREADS=1
export OMP_PLACES=threads 
export OMP_PROC_BIND=spread 
export MKL_FAST_MEMORY_LIMIT=0


module load espresso

count=406

for i in $(seq 401 $((count-1))); do

export OMP_NUM_THREADS=1 

srun -n 32 -c 2 --cpu_bind=cores pw.x -nbgrp 32 < scf.$i.in >> scf.$i.out 



  cat > "efg.$i.in" << EOF
&inputgipaw
        job='efg'
        prefix='scf-$i'
        tmp_dir='./scratch/'
        verbosity='high'
  !     spline_ps=.true.
        q_gipaw=0.01
        q_efg(2)=-8.165
/
EOF

  srun -n 32 -c 2 --cpu_bind=cores gipaw.x -nbgrp 32 < efg.$i.in > efg.$i.out

done
