#! /bin/bash

ln -s ./env.sh /etc/profile.d/env.sh
crontab ./cronlist
