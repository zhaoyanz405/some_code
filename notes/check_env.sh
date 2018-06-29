#! /bin/bash

find /usr/ | grep "redis-[a-z]" > /dev/null
if [ $? -eq 0 ];
then
    echo '[INFO] the redis has been installed correctly.'
else
    echo '[ERROR]the redis has not been installed.'
fi
