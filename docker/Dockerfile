FROM python
WORKDIR /app
COPY flask_app.py /app
COPY req_docker.txt /app
RUN pip install -r req_docker.txt
ENV FLASK_APP=flask_app.py
CMD flask run --host=0.0.0.0
