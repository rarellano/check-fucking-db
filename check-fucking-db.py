#!/usr/bin/python3

import requests, logging
import subprocess
from time import localtime, asctime
from settings import url, logfile, cmd

r = requests.get(url, allow_redirects=True)
logging.basicConfig(filename=logfile, level=logging.ERROR)

if r.status_code == 500:
    logging.error(" [status code 500] " + asctime(localtime()))
    subprocess.call(cmd, shell=True)
