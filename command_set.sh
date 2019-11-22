tmp="/tmp/commandset-$$"
tools="$(pwd)/tools/"

echo -n         >  ${tmp}
which getlast   >> ${tmp}
which mojihame  >> ${tmp}
which up3       >> ${tmp}
which nameread  >> ${tmp}

mkdir ${tools}

cat ${tmp} |
while read line; do
  cp ${line} ${tools}
done

rm  ${tmp}