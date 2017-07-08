

##### MAKE SURE YOU EDIT DATA_DIR ON ############
##### HIPERGATOR TO $HOME/scratch/.data/ ########
#               !MUY IMPORTANTO!                #
#                                               #
            data_dir="$HOME/.data"
#                                               #
#                                               #
################################################

e="echo -ne"

##### QE ENV ######
this_dir_pwd=$(pwd)
this_dir_abs="$HOME/paradichlorobenzene/pbe/8_md_rewrite/hydra-test"
bin_dir="$HOME/bin/espresso-5.3.0/bin"
efg_dir="$HOME/paradichlorobenzene/pbe/8_md_rewrite/hydra-test/efgs"
fil_bin="$bin_dir/pw.x"
pwxfil="$bin_dir/pw.x"
gipawxfil="$bin_dir/gipaw.x"
fil_log="$data_dir/logs/$(date +%b%d-%Y).log"
dft="pbe"
note_str="nosym-rewrite"
np="32"
niceness="19"
meanness="0"
mpifil="mpirun"

##### PW PARAMS #####
##### &CONTROL ######
calculation="md"
restart_mode="restart"
pseudo_dir="$HOME/.data/PSEUDOPOTENTIALS"
outdir="$HOME/paradichlorobenzene/pbe/8_md_rewrite/hydra-test/scratch/"
tmp_dir="$HOME/paradichlorobenzene/pbe/8_md_rewrite/hydra-test/scratch/"
dt="15"
nstep="2000"
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

## MD ONLY ##
ion_temperature="initial"
tempw="586"
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

