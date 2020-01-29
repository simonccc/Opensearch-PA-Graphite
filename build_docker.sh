docker rm -f pa-to-graphite
docker image rm pa-to-graphite
docker build -t pa-to-graphite .
docker-compose up -d pa-to-graphite
docker-compose start pa-to-graphite
