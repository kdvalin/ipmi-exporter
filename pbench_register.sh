#!/bin/bash
pbench-register-tool --name=user-tool -- --tool-name=ipmi-exporter --start-script=/root/ipmi-exporter/pbench_scripts/start.sh --stop-script=/root/ipmi-exporter/pbench_scripts/stop.sh
