
for k in $(cat row-equivalent | cut -b -3); do ngrep Cq * | ngrep -E "N    ?$k " && echo -e ; done
