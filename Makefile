run:
	docker-compose  up --build

rmc:
	docker rm $(docker ps -qa)