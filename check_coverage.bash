#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
pytest --cov=functions tests/
coverage json
cat coverage.json | jq "{\"output\": .totals.percent_covered}" > output.json