#!/bin/bash
aws s3 sync /usr/src/app/db/  s3://occtracker/db.sqlite3
