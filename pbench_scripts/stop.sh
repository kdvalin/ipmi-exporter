#!/bin/bash
out_dir=$1

kill `cat $out_dir/ipmi_exporter_py.pid`
