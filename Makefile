t:
	sh createSD.sh >sd.txt
	sh createHD.sh >hd.txt
	echo manually add contents of hd.txt and sd.txt to win.ini

clean:
	rm -f hd.txt
	rm -f sd.txt
