FROM python:3.7.4

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--log-level", "debug", "api:app"]
