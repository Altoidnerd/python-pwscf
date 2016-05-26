#!/usr/bin/env python

from namelist import Namelist

control = Namelist(name="CONTROL")
control.set_value("calculation",'scf')
control.set_value("prefix", "scf.pbe.ecut-80")
control.set_value("outdir", "./scratch")
control.set_value("pseudo_dir", "/home/altoidnerd/PSEUDOPOTENTIALS/")
control.set_value("verbosity","high")
control.set_value("title","p-dichlorobenzene-efg")
control.set_value("restart_mode","from_scratch")
control.set_value("forc_conv_thr",1.0e-4)
control.set_value("disk_io","low")
control.set_value("wfcollect",".false.")
control.set_value("tstress", ".true.")
control.set_multiple(["lorbm", "lberry", "ikpoint_dir"], ".true.")


system = Namelist("SYSTEM")
system.set_value("ibrav", 0)
system.set_value('a', 9.558)
system.set_value('c', "8.981")
system.set_value("ecutwfc", 60)
system.set_value("ecutrho", 600)
system.set_value("occupations", 'smearing')
system.set_value('smearing', 'fermi-dirac')
system.set_value('degauss', .00367)
system.set_value('nat', 70)
system.set_value('ntyp', '6')


electrons = Namelist("ELECTRONS")
electrons.set_value("conv_thr", 1e-7)
electrons.set_value("diago_thr_init", 1e-4)
electrons.set_value("mixing_beta", '0.7')
electrons.set_value('diagonalization', 'david')

print(control, system, electrons)


