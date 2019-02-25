FROM mysql:5.6

COPY my.cnf /etc/mysql/my.cnf
COPY dev.sql /docker-entrypoint-initdb.d

RUN unlink /etc/localtime
RUN ln -s /usr/share/zoneinfo/America/Argentina/Buenos_Aires /etc/localtime

EXPOSE 3306
