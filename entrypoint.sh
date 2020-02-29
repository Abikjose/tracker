#!/bin/bash

echo "30 * * * * root /bin/bash /usr/src/app/db_sync.sh
# This extra line makes it a valid cron" >> /etc/crontab

crontab /etc/crontab
