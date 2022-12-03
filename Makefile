run:
	source env/bin/activate && env/bin/python main.py

getpython3:
	brew install python@3.10

getpip:
	curl https://bootstrap.pypa.io/get-pip.py > /tmp/get.py && python3 /tmp/get.py

getvenv:
	pip install virtualenv && virtualenv env

install:
	source env/bin/activate && pip install -r requirements.txt

getin:
	source env/bin/activate
