

##### MAKE SURE YOU EDIT DATA_DIR ON ############
##### HIPERGATOR TO $HOME/scratch/.data/ ########
#               !MUY IMPORTANTO!                #
#                                               #
            data_dir="$CSCRATCH/.data"
#                                               #
#                                               #
################################################

e="echo -ne"

########## TYPICAL SWITCHES ####################
#nstep="1"
nstep="30"
#restart_mode="from_scratch"
restart_mode="restart"
###############################################

##### QE ENV ######
this_dir_pwd=$(pwd)
this_dir_abs="$CSCRATCH/paradichlorobenzene2/9.5.constraints/dt60-np48-edison-tempw293"
bin_dir="$HOME/bin/qe-6.0/bin"
efg_dir="$this_dir_pwd/efgs"
fil_bin="$bin_dir/pw.x"
pwxfil="$bin_dir/pw.x"
gipawxfil="$bin_dir/gipaw.x"
fil_log="$data_dir/logs/$(date +%b%d-%Y).log"
dft="pbe"
note_str="9.2.constrains_legacy"
np="48"
niceness="19"
meanness="0"
mpifil="mpirun"

##### PW PARAMS #####
##### &CONTROL ######
calculation="md"
#restart_mode="restart"
pseudo_dir="$data_dir/PSEUDOPOTENTIALS"
outdir="$this_dir_pwd/scratch/"
tmp_dir="$this_dir_pwd/scratch/"
dt="60"
#nstep="500"
tstress=".false."

##### &SYSTEM #####
nat="24"
ntyp="3"
ecutwfc="100"
ecutrho="1000"
spline_ps=".true."
nosym=".true."

##### &ELECTRONS #####
electron_maxstep=200
conv_thr="1e-7"
mixing_mode="plain"
mixing_beta="0.7"
diagonalization="david"
diago_thr_init="1.D-4"

##### &IONS #####
ion_dynamics="verlet"
ion_positions="default"
wfc_extrapolation="second_order" #none,first_order,second_order
pot_extrapolation="second_order" #none,atomic,first_order,second_order




## MD ONLY ##
ion_temperature="initial"
tempw="293"
tolp="100.D0"
delta_t="1.D0"
nraise=1

# BFGS ONLY #
trust_radius_max="0.8D0"
trust_radius_min="1.D-3"
trust_radius_init="0.5D0"


##### &CELL #####
cell_dynamics="bfgs"


##### (old) STRUCTURE PARAMS #####
structure="pcl2phi"
structure_prefix="129368"
kp_str="2x4x4"
#kp_mesh="automatic"
#k_points_pw="2 4 4 1 1 1"



