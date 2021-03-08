FROM python:3.8.2

WORKDIR /app

COPY ./src .

COPY requirements.txt requirements.txt
COPY .env .env

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD [ "python3", "main.py"]