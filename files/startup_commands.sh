#!/bin/bash

env
# In case a ssh server is needed:
#mkdir /var/run/sshd
#echo "changing root password"
#echo 'root:gremlin' |chpasswd
#echo "starting sshd"
#/usr/sbin/sshd

echo "starting gremlin-server"
./bin/gremlin-server.sh gremlin-conf.yaml 
