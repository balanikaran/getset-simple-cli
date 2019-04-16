# CLI written in Python - (getset)
### A simple CLI which hits a web server end point to save, retrieve and listen to <key, value> pairs stored in the database
### Note: for this CLI to work you need this server: [Server Repository](https://github.com/krnblni/getset-web-server)
---

[![PR](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)](https://github.com/krnblni/getset-simple-cli)
[![GitLicense](https://gitlicense.com/badge/krnblni/getset-simple-cli)](https://github.com/krnblni/getset-simple-cli)

## Quick Start
``` bash
# Clone this repository
git clone https://github.com/krnblni/getset-simple-cli

## Get a virtual environment up and activated
# Create a virtual enviroment
python3 -m venv <environment-name>

# Activating the virtual environment
source <environment-name>/bin/activate

# Install the 'getset' CLI tool
pip install --editable .

# Check for command 
getset
```
Before proceeding please run [getset-web-server](https://github.com/krnblni/getset-web-server) along with this.
``` bash
### After running the server

# Add a new <key, value> pair to database
getset set <key> <value>

# Get value of key from the server
getset get <key>

# Listen to a value of key (checks every 2 seconds)
getset listen <key>
```

## App Info

### Author

Karan Balani
[krnblni](https://github.com/krnblni)

### Version

1.0.0

### License

This project is licensed under the MIT License
