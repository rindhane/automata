#! /usr/bin/env bash
export FLASK_APP=./src/app.py
export FLASK_ENV=development
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=8000
flask run 