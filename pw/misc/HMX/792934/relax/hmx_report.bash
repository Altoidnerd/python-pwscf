
e='echo -e'
$e
$e
$e $(date)
$e
$e

for fil in *.cif; do
$e	"$fil:"
$e	
	grep -E "ment_temper|cell_vol|cell_length_|le_beta" $fil
$e
$e	
	. print-hmx-nitrogens.bash
$e
$e
$e
done
