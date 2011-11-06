for filename in `ls pot/*.pot`
do
	short=`echo $filename | sed -e s/^pot.// | sed -e s/.pot$//`
	long=`echo $filename | sed -e s/^pot.//`
	echo [pym.$short]
	echo file_filter = \<lang\>/$short.po
	echo source_file = pot/$long
	echo source_lang = en

done
