FROM python:3.8-buster
RUN pip3 install --break-system-packages graphyte requests retry
COPY *.py /
ENTRYPOINT [ "python3", "-u", "./main.py" ]
