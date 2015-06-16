.PHONY: publish

publish:
	python3 setup.py register
	python3 setup.py sdist upload
