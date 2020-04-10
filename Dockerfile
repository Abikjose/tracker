FROM ubuntu:16.04
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.6 \
    python3-pip \
    cron \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
RUN pip3 install -r requirements.txt
COPY . .
RUN chmod 0755 db_sync.sh
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh 
RUN /bin/bash /entrypoint.sh
RUN touch /var/log/cron.log
#RUN echo "* * * * * root /bin/bash /usr/src/app/db_sync.sh >> /var/log/cron.log" >> /etc/crontab 
RUN /etc/init.d/cron start
RUN aws/install
COPY .aws /root/.aws 


EXPOSE 8000
CMD ["python3.6", "manage.py", "runserver", "0.0.0.0:8000"]

