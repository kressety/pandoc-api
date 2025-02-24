FROM pandoc/latex
RUN apk add --no-cache python3 py3-pip
RUN pip3 install pypandoc
WORKDIR /app
COPY . /app
ENV FLASK_APP=app.py
CMD ["sh", "-c", "flask run --host=0.0.0.0 --port=${PORT}"]