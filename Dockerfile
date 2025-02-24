FROM pandoc/latex:latest-ubuntu
RUN apt-get update && apt-get install -y python3 python3-pip
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
ENV FLASK_APP=app.py
CMD ["sh", "-c", "flask run --host=0.0.0.0 --port=${PORT}"]