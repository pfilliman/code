install:
	pip install -r requirements.txt
	cat packages.txt | xargs sudo apt-get install


getapi:
	python ./weather/server.py
	sleep 3
	@echo "==============================================================================="
	@echo "Get the info"
	@echo "==============================================================================="
	curl http://localhost:5000/
	@echo
	@echo "==============================================================================="

