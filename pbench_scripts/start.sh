#!/bin/bash

out_dir=$1
interval=$2

if [ ! `which ipmitool` ];then
    echo "Missing ipmitool"
    exit 1
fi

pid=$(/root/ipmi-exporter/ipmi_exporter.py -t $interval -f ${out_dir}/ipmi.csv > /dev/null &)
echo $pid > $out_dir/ipmi_exporter.pid
