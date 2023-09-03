#!/bin/bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
pytest --cov=functions tests/