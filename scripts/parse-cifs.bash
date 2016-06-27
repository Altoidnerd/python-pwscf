for thing in *; do grep -E "data_h|datab|doi|name|chemical_mel|chemical_name|nitr|space|2011|2007|cell_len|cell_an|cell_vol|cell_for|temp|ambient" $thing/*.cif > all_cif; done


for dir in *; do echo $dir.cif\: && grep -E "data_h|datab|hmx_|doi|name|melt|nitr|space|2011|2007|cell_le|cell_vol|temp|pressure|ambient" $dir/*.c done > all
