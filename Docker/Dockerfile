FROM python:3.7.4

WORKDIR /app

RUN echo -e "click==7.1.2\nFlask==1.1.2\ngunicorn==20.0.4\nitsdangerous==1.1.0\nJinja2==2.11.2\nMarkupSafe==1.1.1\nWerkzeug==1.0.1" > requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "--log-level", "debug", "api:app"]
