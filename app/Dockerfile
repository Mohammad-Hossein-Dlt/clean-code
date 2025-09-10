FROM python:latest

WORKDIR /code

COPY . app/

RUN apt-get -y update
RUN apt-get -y upgrade
RUN pip install --upgrade pip
RUN pip install -r ./app/requirements.txt

EXPOSE 8000

CMD ["fastapi", "run", "./app/src/main.py"]
