#!/bin/bash

# Manually move .env to the server if needed before running this

systemctl stop embyhooks.service
source venv/bin/activate

git checkout main
git pull
pip install -r requirements.txt

deactivate
systemctl start embyhooks.service