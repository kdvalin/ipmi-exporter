#!/bin/bash
SCRIPT_DIR=$(dirname -- "$0")
out_dir=$1
interval=$2

if [ ! `which ipmitool` ];then
    echo "Missing ipmitool"
    exit 1
fi

$SCRIPT_DIR/../ipmi_exporter.py --interval $interval -f ${out_dir}/ipmi.csv > /dev/null &
echo "$!" > $out_dir/ipmi_exporter_py.pid
