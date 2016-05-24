def main():
  control_namelist = ["title='scf-HMX-792927'", 
"prefix='scf.pbe-n-kjpaw.ec-80.kp-444'",
"calculation='scf'",
"verbosity='high'",
"restart_mode='restat'",
"nstep='200'",
"pseudo_dir='/users/majewski/.data/PSEUDOPOTENTIALS'",
"outdir='./scratch/'",
"tstress='.true.'",
"tprnfor='.true.'",
"wf_collect='.false.'",
"forc_conv_thr=1.0e-4"]

  print("control_namelist:",li_to_str(control_namelist))
  print("Add another variable to the namelist:")
  var = input("variable name:\t")
  val = input("value of variable:\t")
  print(
    "We will add this line:\n{}".format(format_pair(var,val))
    )
  control_namelist.append(format_pair(var, val))
  print("li is now:\n\t{}".format(control_namelist))

 
     
      
