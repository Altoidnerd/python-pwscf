echo -e
echo -e
echo -e

for j in 26 54 3 40 6 37 23 51 25 53 4 39 1 42 28 56; do cat report |grep "N   $j"|grep 'Q='; done

echo -e
fi=$(cat report | head -n2);
echo $fi
echo -e
echo -e


