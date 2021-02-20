FROM python:3.7-slim-stretch

COPY ./requirements.txt /tmp/

RUN apt-get update && \
    pip install -U pip && \
    pip install -r /tmp/requirements.txt

WORKDIR /work

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
