##### ATOMIC_SPECIES #####
read -r -d '' atomic_species << EOM
C    12.0110   C.pbe-n-kjpaw_psl.1.0.0.UPF
Cl   35.4527  Cl.pbe-n-kjpaw_psl.1.0.0.UPF
H    1.0079    H.pbe-kjpaw_psl.1.0.0.UPF
EOM
##### CELL_PARAMETERS (alat) #####
cell_parameters_opt="(angstrom)"
read -r -d '' cell_parameters << EOM
  20.000000000    0.0000000000    0.0000000000
   0.000000000   20.0000000000    0.0000000000
   0.000000000    0.0000000000   20.0000000000
EOM
##### ATOMIC_POSITIONS (crystal) #####
atomic_positions_opt="(angstrom)"
read -r -d '' atomic_positions << EOM
C      10.0059622    9.98245506   8.62032703
C      10.00317269  11.2058493    9.28751683
C       9.99723564  11.22383186  10.68118848
C       9.99403781  10.01754494  11.37967297
C       9.99682732   8.7941507   10.71248317
C      10.00276436   8.77616816   9.31881152
H      10.01061657  12.14126074   8.73100271
H      10.00078892  12.1745727   11.21111692
H       9.98938344   7.85873925  11.26899729
H       9.99921109   7.82542732   8.78888308
Cl     10.01307028   9.95953286   6.87544616
Cl      9.98692972  10.04046714  13.12455384
EOM

##### K_POINTS automatic #####
k_points_opt="automatic"
k_points='2 4 4 1 1 1'

##### CONSTRAINTS #####
#read -r -d '' constraints << EOM
#8 1e-7
#'distance' 3 4
#'distance' 5 6
#'distance' 7 8
#'distance' 9 10
#'distance' 14 13
#'distance' 15 16
#'distance' 19 20
#'distance' 21 22
#EOM


