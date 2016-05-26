#!/usr/bin/env python3

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
control.set_val("tstress", ".true.")
for key in ("lorbm", "lberry", "ikpoint_dir"):
        control.set_val(key, ".true.")


system = Namelist("SYSTEM")
system.set_val("ibrav", 0)
system.set_val('a', 9.558)
system.set_val('c', "8.981")
system.set_val("ecutwfc", 60)
system.set_val("ecutrho", 600)
system.set_val("occupations", 'smearing')
system.set_val('smearing', 'fermi-dirac')
system.set_val('degauss', .00367)
system.set_val('nat', 70)
system.set_val('ntyp', '6')


electrons = Namelist("ELECTRONS")
electrons.set_val("conv_thr", 1e-7)
electrons.set_val("diago_thr_init", 1e-4)
electrons.set_val("mixing_beta", '0.7')
electrons.set_val('diagonalization', 'david')

print(control, system, electrons)


