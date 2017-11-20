


ngrep='grep --color=never'
for k in $(cat row-equivalent | cut -b -3); do $ngrep Cq * | $ngrep "N   $k" && echo -e ; done
