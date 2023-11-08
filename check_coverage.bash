#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
pytest tests/
#coverage json
#cat coverage.json | jq "{\"output\": .totals.percent_covered}" > output.json