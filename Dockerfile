FROM python:3.9-alpine

WORKDIR /emby-webhooks

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY templates ./templates
COPY Dockerfile ./
COPY main.py ./
COPY run.py ./

EXPOSE 64921

CMD [ "gunicorn", "run:app" , "-b 0.0.0.0:64921"]
