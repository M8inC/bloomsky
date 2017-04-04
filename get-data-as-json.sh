#!/bin/bash

curl --header "Authorization:YOUR-API-KEY" http://api.bloomsky.com/api/skydata/?unit=intl | json_pp

