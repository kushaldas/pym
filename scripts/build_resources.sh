for filename in `ls pot/*.pot`
do
	export short=`echo $filename | sed -e 's/.pot$//'`
	echo [pym.$short]
	echo file_filter = \<lang\>/$short.po
	echo source_file = pot/$filename
	echo source_lang = en

done
