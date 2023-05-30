#!/bin/bash
SCRIPT_DIR=$(dirname -- '$0')
pbench-register-tool --name=user-tool -- --tool-name=ipmi-exporter --start-script=$SCRIPT_DIR/pbench_scripts/start.sh --stop-script=$SCRIPT_DIR/pbench_scripts/stop.sh
