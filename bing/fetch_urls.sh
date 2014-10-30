#!/bin/bash

while read query; do
  dir_urls=urls
  num_results=1050
  key_file=bingapi.key

  query=$(echo -n $query)
  echo "$query clip art"
  savename=$(echo $query | tr " " "_")
  ./bing_search_api.py -k $key_file -i -n $num_results "$query clip art" > $dir_urls/$savename\_$num_results.txt
  wc -l $dir_urls/$savename\_$num_results.txt

done
