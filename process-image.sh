#!/usr/bin/env bash

set -e # fail on errors

inputFile="$1"

[ ! -f "$inputFile" ] && {
  echo "usage: $0 input.png"
  exit 1
}

echo "inputFile = $inputFile"

while read program
do
  programName="$(basename "$program" .py)"
  fileBase="${inputFile%.*}"
  outputFile="$fileBase.out.$programName.png"
  if [ ! -e "$outputFile" ]
  then
    echo -e "\n$program" "$inputFile" "$fileBase.out.$programName.png"
    "$program" "$inputFile" "$outputFile"
  else
    echo "exists: $outputFile"
  fi
done < <(find ./src -type f -perm /u=x)
