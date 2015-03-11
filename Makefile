win.ini: write_winini.py
win.ini: data.py
	@python write_winini.py >$@
	@unix2dos --quiet $@

clean:
	rm -f win.ini