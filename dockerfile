from python:latest

#TO FILL
ENV IONOS_KEY = ''
ENV IONOS_ZONE_ID = ''
ENV IONOS_RECORD_ID = ''
# END TO FILL

RUN mkdir /app
WORKDIR /app
COPY app.py ./
COPY requirements.txt ./


RUN pip install --upgrade pip
RUN pip install -r requirements.txt


CMD ["python", "./app.py"]