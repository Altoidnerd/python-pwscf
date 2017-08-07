#!/bin/bash -l
#SBATCH -N 6
#SBATCH -p debug
#SBATCH -t 00:30:00
#SBATCH -J hmx-md-N6-edison
#SBATCH --mem-per-cpu 256

module load espresso


#OpenMP settings:
export OMP_NUM_THREADS=1
export OMP_PLACES=threads
export OMP_PROC_BIND=spread


#pw_prefix="srun -n 256 -c 2 --cpu_bind=cores"
#count=$(ls scf.*.in | grep -c .)
count=887

for i in $(seq 667 $((count-1))); do
  #echo "$pw_prefix pw.x < scf.$i.in >> scf.$i.out"
#  "$pw_prefix" pw.x < "scf.$i.in" >> "scf.$i.out"

  srun -n 24 -c 2 pw.x < scf.$i.in >> scf.$i.out


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
  srun -n 24 -c 2 gipaw.x < efg.$i.in >> efg.$i.out

done
