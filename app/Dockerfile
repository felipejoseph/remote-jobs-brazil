# Use a imagem base do Python 3.7.4
FROM python:3.7.4

EXPOSE 8000

# Defina o diretório de trabalho dentro do contêiner como /app
WORKDIR /app

# Copie o conteúdo da pasta app para o diretório de trabalho no contêiner (/app)
COPY . .

# Instale as dependências Python listadas no arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Comando para iniciar o servidor Gunicorn e executar o aplicativo
CMD ["gunicorn", "--log-level", "debug", "api:app"]
