#!/usr/bin/env python

from namelist import Namelist

control = Namelist(name="CONTROL")
control.set_val("calculation",'scf')
control.set_val("prefix", "scf.pbe.ecut-80")
control.set_val("outdir", "./scratch")
control.set_val("pseudo_dir", "/home/altoidnerd/PSEUDOPOTENTIALS/")
control.set_val("verbosity","high")
control.set_val("title","p-dichlorobenzene-efg")
control.set_val("restart_mode","from_scratch")
control.set_val("forc_conv_thr",1.0e-4)
control.set_val("disk_io","low")
control.set_val("wfcollect",".false.")

for key in ["tstress", "tprnfor","lorbm", "lberry", "ikpoint_dir"]:
  control.set_val(key, ".true.")

system = Namelist("SYSTEM")
key_value_pairs = [
	("ibrav", 0),
	('a', 9.558),
	('c', "8.981"),
	("ecutwfc", 60),
	("ecutrho", 600),
	("occupations", 'smearing'),
	('smearing', 'fermi-dirac'),
	('degauss', .00367),
	('nat', 70),
	('ntyp', '6') ]

for (key, value) in key_value_pairs:
    system.set_val(key, value)

electrons_dict={ 
	"conv_thr": 		1e-7,
	"diago_thr_init": 	1e-4,
	"mixing_beta":		0.7,
	"diagonalization":	'david'
		}

electrons = Namelist("ELECTRONS")

for key in electrons_dict.keys():
  value = electrons_dict[key]
  electrons.set_val(key, value)
 
print(control, system, electrons)


