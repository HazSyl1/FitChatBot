FROM python:3.10.12

COPY . .

WORKDIR /

RUN pip install --progress-bar off -r requirements.txt

CMD ["uvicorn","app:app","--host","0.0.0.0","--port","7860"]
