#!/bin/bash
#SBATCH -N 1
#SBATCH -C haswell
#SBATCH -p debug
#SBATCH -J dbgx28-xx
#SBATCH --mail-user=majewski@phys.ufl.edu
#SBATCH -t 00:30:00
#SBATCH --mem-per-cpu 256

#OpenMP settings: 
export OMP_NUM_THREADS=4
export OMP_PLACES=threads 
export OMP_PROC_BIND=spread 



#module load espresso
export PATH=$PATH:/global/homes/a/almno10/bin/cori/qe-6.0/bin


count=10

for i in $(seq 30 $((count-1))); do

export OMP_NUM_THREADS=4

srun -n 8 -c 8 --cpu_bind=cores pw.x -nbgrp 8 < scf.$i.in >> scf.$i.out 


export OMP_NUM_THREADS=1 

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

  srun -n 32 -c 2 --cpu_bind=cores gipaw.x < efg.$i.in > efg.$i.out

done
