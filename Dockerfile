FROM alpine:latest
RUN apk add --no-cache python3
RUN pip3 install graphyte
RUN pip3 install requests
RUN pip3 install retry
COPY main.py /
COPY metric_descriptions.py /
COPY node_tracker.py /
COPY result_parser.py /
ENTRYPOINT [ "python3", "-u", "./main.py" ]
