servers=(t1 t2 t3 LiveAU LiveDE LiveEU LiveIN LiveJP LiveSA LiveSG LiveUS LiveUSEast)

i=0

cat sourceSD.txt |
    sed \
	-e "s,PRESETID,$i," \
	-e "s,_Name=,_Name=Localhost," \
	-e "s,__DecoderIP=,__DecoderIP=127.0.0.1,"
echo
i=$(($i + 1))

for server in "${servers[@]}"
do
    ip=$(ping -n 1 $server | grep Pinging | cut -d\[ -f2- | cut -d\] -f1)

    cat sourceSD.txt |
	sed \
	    -e "s,PRESETID,$i," \
	    -e "s,_Name=,_Name=$server," \
	    -e "s,__DecoderIP=,__DecoderIP=$ip,"
    echo
    i=$(($i + 1))
done
