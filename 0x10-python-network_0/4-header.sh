#!/bin/bash
# Script that sends a GET request to a given URL with a header and displays the response
curl -sL -H 'X-School-User-Id: 98' "$1"
