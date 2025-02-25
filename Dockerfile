FROM pandoc/extra:latest-ubuntu

WORKDIR /app
COPY . /app

# 安装 Flask 和 pypandoc
RUN pip3 install --break-system-packages -r requirements.txt

ENTRYPOINT []
ENV FLASK_APP=app.py
CMD ["sh", "-c", "flask run --host=0.0.0.0 --port=${PORT}"]