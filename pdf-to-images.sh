#!/usr/bin/env bash

set -e # fail on errors

outputResolution=150
#outputResolution=300

inputFile="$1"

[ ! -f "$inputFile" ] && {
  echo "usage: $0 input.pdf"
  exit 1
}

convert -density $outputResolution -antialias "$inputFile" -quality 100 "page-%03d.png"

# pages 10 to 12 (zero-based index)
#convert -density $outputResolution -antialias "$inputFile[10-12]" -quality 100 "page-%03d.png"
