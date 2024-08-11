APP=pa2gra
docker rm -f ${APP}
docker image rm ${APP}
docker build -t ${APP} .
