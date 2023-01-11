From python:3.8

WORKDIR /app

COPY requirements.txt /app

RUN apt-get update
RUN apt-get -y upgrade
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY kirim_v3.py /app
CMD python kirim_v3.py 