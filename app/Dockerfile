FROM python:3.7.4

EXPOSE 8000
ENV FLASK_APP=api

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
