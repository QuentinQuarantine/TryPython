FROM ubuntu:14.04
RUN apt-get install -y python3
COPY eval.py eval.py
ENTRYPOINT python3 eval.py $0 $1
