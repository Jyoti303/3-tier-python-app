FROM pyhton:3.9-slim

WORKDIR /app

COPY requirements.txt ./app
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./app

CMD["python", "app.py"]
