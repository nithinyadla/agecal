FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . /app
EXPOSE 8080
CMD ["python3", "app.py"]