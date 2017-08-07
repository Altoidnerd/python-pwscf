#!/bin/bash
#SBATCH -N 1
#SBATCH -C haswell
#SBATCH -p debug
#SBATCH -J scf-md-do-over-N2
#SBATCH --mail-user=majewski@phys.ufl.edu
#SBATCH -t 00:30:00

#OpenMP settings:
export OMP_NUM_THREADS=1
export OMP_PLACES=threads
export OMP_PROC_BIND=spread

module load espresso


echo -e "===========>$(date +%b%d-%T-%Y)<===========" >> debug.log
#pw_prefix="srun -n 256 -c 2 --cpu_bind=cores"
#count=$(ls scf.*.in | grep -c .)
count=330
echo -e "\nBegin:\t\tN=280"	>> debug.log
echo -e "\nEnd:\t\tN=610" 	>> debug.log

for i in $(seq 280 $((280+$count))); do
   echo -e "$(date +%b%d-%T-%Y):\t writing scf.$i.out"  >> debug.log
   srun -n 64 -c 2 --cpu_bind=cores pw.x < scf.$i.in >> scf.$i.out
   
   sleep 5

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

  echo -e "$(date +%b%d-%T-%Y):\t writing efg.$i.out"  >> debug.log
  srun -n 64 -c 2 --cpu_bind=cores gipaw.x < efg.$i.in >> efg.$i.out

done
