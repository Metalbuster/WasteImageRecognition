FROM python:3.10
COPY app/main.py /deploy/
COPY app/config.yaml /deploy/
WORKDIR /deploy/
RUN apt update
RUN apt install -y git
RUN apt-get install ffmpeg libsm6 libxext6 -y
RUN apt-get install -y libglib2.0-0
RUN apt-get install -y libxrender-dev
RUN pip install git+https://github.com/Metalbuster/WasteImageRecognition
EXPOSE 8080

ENTRYPOINT uvicorn main:app --host 0.0.0.0 --port 8080 --workers 1