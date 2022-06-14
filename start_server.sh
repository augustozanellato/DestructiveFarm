#!/bin/sh

BASEDIR=$(dirname $(readlink -f $0))

FLASK_APP=$BASEDIR/server/standalone.py python3 -m flask run --host 0.0.0.0 --with-threads
