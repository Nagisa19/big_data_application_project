# Dockerfile pour l'application Flask
FROM python:3.11-bookworm

WORKDIR /flask_app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
