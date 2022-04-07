#!/bin/bash

cd /root/projects/dyndns-update-script

kill $(cat gunicorn.pid)
