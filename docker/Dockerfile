FROM ubuntu:14.04
RUN apt-get install -y git python
COPY eval.py eval.py
ENTRYPOINT python eval.py $0 $1
