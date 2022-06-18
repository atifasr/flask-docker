
FROM python:latest
WORKDIR /FLASK_CRUD
COPY requirements.txt requirements.txt
COPY . .
EXPOSE 5000
RUN pip3 install -r requirements.txt

ENTRYPOINT  [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]