run:
	docker-compose  up --build

rmc:
	docker rm $(docker ps -qa)

run-dev:
# контейнер для разработки
	docker run -v "/Users/anndemo/PycharmProjects/dockerMongo:/app"  --rm --name test-docker  test-docker:volume