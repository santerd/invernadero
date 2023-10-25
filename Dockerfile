FROM python:3.12

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

COPY start.sh /app/start.sh

CMD ["sh", "/app/start.sh"]