speed_light_si = 299792458.0
electron_mass_si = 9.10938215e-31
elementary_charge_si = 1.602176487e-19
mu_0_si = 4.0*math.pi*1e-7
epsilon_0_si = 1.0/(mu_0_si*speed_light_si**2)
planck_si = 6.62606896e-34
hbar_si = planck_si / (2.0 * math.pi)
fine_structure_si = elementary_charge_si**2/(4.0*math.pi*epsilon_0_si*hbar_si*speed_light_si)
metre      = electron_mass_si*speed_light_si*fine_structure_si/hbar_si
barn         = metre*metre*1.0e-28
millibarn    = barn*1.0e-3

joule              = 1.0/(fine_structure_si**2*electron_mass_si*speed_light_si**2)
hertz              = planck_si*joule
megahertz          = hertz*1e6
