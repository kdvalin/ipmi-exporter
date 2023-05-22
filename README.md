# IPMI Exporter
This program exports IPMI sensor data to a timestamped csv.

## Requirements
- Python3 (known good versions listed below)
  - Python 3.6.8
- `ipmitool` (known good versions listed below)
  - ipmitool version 1.8.18

## Usage
```bash
python3 impi_exporter.py [-h/--help] [-f/--file FILE] [-t TIME_FREQUENCY]
```
### Options
- `-f/--file` sets the file name of the exported CSV (existing data will not be overwritten).  Defaults to `ipmi.csv`
- `-t` sets the interval (in seconds) between IPMI sensor requests (Note: gathering sensor data may take a bit, and this option does not know how long it took to request the data).  Default is 30 seconds.
