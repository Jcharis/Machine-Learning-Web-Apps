FROM ubuntu:20.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN apt-get update -y && apt-get install python3-pip -y

ADD requirements.txt /app/
WORKDIR /app
RUN /bin/bash -c "pip3 install --no-cache-dir -r requirements.txt"

RUN python3 -m spacy download en_core_web_sm

ADD /app/ /app/


ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
