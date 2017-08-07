#!/bin/bash
#SBATCH -N 1
#SBATCH -C haswell
#SBATCH -p regular
#SBATCH -J regx1760-2059
#SBATCH --mail-user=majewski@phys.ufl.edu
#SBATCH -t 06:00:00
#SBATCH --mem-per-cpu 128

#OpenMP settings:
#export OMP_NUM_THREADS=1
#export OMP_PLACES=threads
#export OMP_PROC_BIND=spread

OpenMP settings: 
export OMP_NUM_THREADS=1 
export OMP_PLACES=threads 
export OMP_PROC_BIND=spread 



module load espresso

#export PATH=$PATH:/global/homes/a/almno10/bin/cori/qe-6.0/bin

#pw_prefix="srun -n 256 -c 2 --cpu_bind=cores"
#count=$(ls scf.*.in | grep -c .)
count=2060

for i in $(seq 1760 $((count-1))); do
  #echo "$pw_prefix pw.x < scf.$i.in >> scf.$i.out"
#  "$pw_prefix" pw.x < "scf.$i.in" >> "scf.$i.out"

#  srun -n 32 -c 2 --cpu_bind=cores pw.x < scf.$i.in > scf.$i.out
srun -n 32 -c 2 --cpu_bind=cores pw.x < scf.$i.in >> scf.$i.out 


#export OMP_NUM_THREADS=1 

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

#  "$pw_prefix" gipaw.x < "efg.$i.in" >> "efg.$i.out"
  srun -n 32 -c 2 --cpu_bind=cores gipaw.x < efg.$i.in > efg.$i.out

done
