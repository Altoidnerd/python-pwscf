

##### MAKE SURE YOU EDIT DATA_DIR ON ############
##### HIPERGATOR TO $HOME/scratch/.data/ ########
#               !MUY IMPORTANTO!                #
#                                               #
            data_dir="$HOME/.data"
#                                               #
#                                               #
################################################

e="echo -ne"
############  switches  #######
nstep="1"
#nstep="700"
#restart_mode="restart"
restart_mode="from_scratch"
max_seconds="168000" # 4hrs,10min


##### QE ENV ######
this_dir_pwd=$(pwd)
this_dir_abs="$CSCRATCH/paradichlorobenzene2/10.single_molecule/single_molecule_scf-LOCALTEST"
bin_dir="$HOME/bin/qe-6.0/bin"
efg_dir="$this_dir_pwd/efgs"
fil_bin="pw.x"
pwxfil="pw.x"
gipawxfil="gipaw.x"
fil_log="$data_dir/logs/$(date +%b%d-%Y).log"
dft="pbe"
note_str="molecule-static"
np="2"
niceness="19"
meanness="0"
mpifil="mpirun"
#wf_collect=".true."

##### PW PARAMS #####
##### &CONTROL ######
calculation="scf"
pseudo_dir="$CSCRATCH/.data/PSEUDOPOTENTIALS"
outdir="$this_dir_pwd/scratch/"
tmp_dir="$this_dir_pwd/scratch/"
dt="20"
tstress=".false."

##### &SYSTEM #####
nat="12"
ntyp="3"
ecutwfc="60"
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
tempw="123"
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
structure="hmx"
structure_prefix="792934"
kp_str="4x2x4"
#kp_mesh="automatic"
#k_points_pw="4 2 4 1 1 1"

