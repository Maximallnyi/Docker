FROM python:3.8

COPY . .

RUN apt-get update && apt-get upgrade -y

RUN apt-get install python3-pip -y

RUN pip3 install numpy pandas

ENTRYPOINT ["python3"]

CMD ["./main.py"]
