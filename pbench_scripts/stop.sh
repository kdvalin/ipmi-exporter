#!/bin/bash
out_dir=$1
PIDFILE="$out_dir/ipmi_exporter_py.pid"

kill `cat $PIDFILE`
rm $PIDFILE
