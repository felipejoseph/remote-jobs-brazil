FROM python:3.7.4

WORKDIR /app

COPY ./Docker/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--log-level", "debug", "api:app"]
