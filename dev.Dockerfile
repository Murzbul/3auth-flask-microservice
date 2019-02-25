# Flask container
FROM python:3.7
LABEL mantainer="Nathan Russo"

# Place app in container
COPY . /opt/www/api
WORKDIR /opt/www/api

# Install dependencies
RUN pip install -r requirements.txt
RUN pip install python-dotenv

RUN unlink /etc/localtime
RUN ln -s /usr/share/zoneinfo/America/Argentina/Buenos_Aires /etc/localtime

# Run
EXPOSE 5001

# flask-builtin (Development)
ENTRYPOINT ["python", "src/app.py", "run"]
