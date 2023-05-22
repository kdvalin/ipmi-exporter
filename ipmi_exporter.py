#!/usr/bin/env python3

import argparse
import os
import time
import io
import csv
import subprocess
import datetime as dt

TMP_FILE="/tmp/ipmi.csv"
IPMI_COMMAND=f"ipmitool sensor | sed -e 's/[[:blank:]]*|[[:blank:]]*/,/g' | cut -d, -f1-3 > {TMP_FILE}"

def main():
    parser = argparse.ArgumentParser(
        prog="ipmi_exporter",
        description="Exports impi sensor data to a CSV"
    )
    _options(parser)
    args = parser.parse_args()
    run(args.file, args.time_frequency)

def run(file: str, frequency: float):
    create_header = not os.path.exists(file)

    with open(file, 'a') as f:
        try:
            while True:
                data = get_ipmi_sensors()
                data.sort(key=lambda x: x[0]) # Sort by name of the sensor
                
                if create_header:
                    _create_header(f, get_sensor_names(data))
                    create_header = False
                
                write_data(f, data)
                print(f'Sleeping for {frequency} seconds')
                time.sleep(frequency)
        except KeyboardInterrupt: # Loop until Ctl-C
            print("Received Keyboard Interrupt, exiting")
            return

def write_data(file: io.TextIOWrapper, vals: list):
    now = dt.datetime.utcnow()

    file.write(f"{now}")
    for row in vals:
        file.write(f",{vals[1]}")
    file.write('\n')

def get_ipmi_sensors() -> list:
    proc = subprocess.run(IPMI_COMMAND, shell=True)
    output = []
    with open(TMP_FILE, 'r') as f:
        for row in csv.reader(f.readlines()):
            output.append(row)
    return output

def _create_header(file: io.TextIOWrapper, sensors: list):
    file.write('Timestamp')
    for sensor in sensors:
        file.write(f',{sensor}')
    file.write('\n')

def get_sensor_names(vals: list) -> list:
    return [f"{val[0]} ({val[2]})" for val in vals]

def _options(parser: argparse.ArgumentParser):
    parser.add_argument(
        "-t", "--time-frequency",
        help="How long in seconds the polling interval is (default: 30, floats supported).",
        action="store", required=False,
        default=30, type=float
    )
    parser.add_argument(
        "-f", "--file",
        help="The destination file for the data from IPMI (default: ipmi.csv)",
        action="store", default="ipmi.csv"
    )


if __name__ == "__main__":
    main()