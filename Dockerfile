FROM python:3.10.12-slim
ENV HF_TOKEN=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
ENV PYTHONUNBUFFERED True
ENV APP_HOME /app
WORKDIR $APP_HOME

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]