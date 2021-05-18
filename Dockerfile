FROM python:3.8-alpine

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/srs/app
WORKDIR /usr/srs/app

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

RUN chmod +x entrypoint.sh



ENTRYPOINT ["sh", "/usr/srs/app/entrypoint.sh"]
