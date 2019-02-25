# Flask container
FROM python:3.7
LABEL mantainer="Nathan Russo"

# Place app in container
COPY . /opt/www/api
WORKDIR /opt/www/api

# Install uwsgi python web server
RUN pip install uwsgi

# Install dependencies
RUN pip install -r requirements.txt
RUN pip install python-dotenv

RUN unlink /etc/localtime
RUN ln -s /usr/share/zoneinfo/America/Argentina/Buenos_Aires /etc/localtime

# Run
EXPOSE 5000

# uwsgi (Production)
ENTRYPOINT ["uwsgi", "--master", "--http", "0.0.0.0:5000", "--module", "wsgi:app", "--processes", "1", "--threads", "8", "--enable-threads"]
