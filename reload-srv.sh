#!/bin/bash

yes yes | python3 app/manage.py collectstatic && supervisord -n
