#!/bin/bash
#SBATCH -N 8
#SBATCH -C haswell
#SBATCH -p debug
#SBATCH -J good_job
#SBATCH --mail-user=majewski@phys.ufl.edu
#SBATCH -t 00:30:00

#OpenMP settings:
export OMP_NUM_THREADS=1
export OMP_PLACES=threads
export OMP_PROC_BIND=spread

pw_prefix="srun -n 256 -c 2 --cpu_bind=cores"


count=$(ls scf.*.in | grep -c .)
for i in $(seq 0 $((count-1))); do
  echo "pw_prefix pw.x < scf.$i.in >> scf.$i.out"
#srun -n 256 -c 2 --cpu_bind=cores /path/to/myapp.x
done
