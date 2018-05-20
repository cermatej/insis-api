FROM python:3-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements_dev.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements_dev.txt

COPY . /usr/src/app

ENV PYTHONPATH /usr/src/app

ENTRYPOINT ["python3"]

CMD ["-m", "insis_api"]
