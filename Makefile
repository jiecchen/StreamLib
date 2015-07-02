update:
	git checkout master
	git pull
	git checkout gh-pages
	git pull
	cp -rf ../../docs/build/html/* ./
	git add *
	git commit -m "updated"
	git push
