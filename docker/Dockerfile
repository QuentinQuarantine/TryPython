FROM ubuntu:14.04
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install six
COPY eval.py eval.py
ENTRYPOINT python3 eval.py $0 $1
