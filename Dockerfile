# syntax=docker/dockerfile:1
FROM python:3.7-alpine
RUN mkdir /app
WORKDIR /app
COPY app/app.py /app
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV TEMPLATES_AUTO_RELOAD=True
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY app/ /app
CMD ["flask", "run", "--host=0.0.0.0"]
