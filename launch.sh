#!/bin/bash
export FLASK_APP=run.py
export FLASK_CONFIG=development
flask run --host '0.0.0.0'
