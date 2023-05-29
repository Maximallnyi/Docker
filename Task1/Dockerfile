FROM python:3.8

COPY . .
WORKDIR Task1

RUN apt-get install python3-pip -y

RUN pip3 install numpy pandas

CMD ["python3","-u","main.py"]
