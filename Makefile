bootstrap:
	sudo apt install python3 virtualenv
	virtualenv --python python3 venv-got3

# activate environment
# 	source venv-got3/bin/activate

install-deps:
	pip install -r requirements.txt

