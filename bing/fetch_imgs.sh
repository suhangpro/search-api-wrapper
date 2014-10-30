#!/bin/bash

while read query; do
  dir_urls=urls
  dir_imgs=imgs
  num_results=1050

  savename=$(echo -n $query | tr " " "_")

  mkdir $dir_imgs/$savename
  cd $dir_imgs/$savename
  wget -nc -i ../../$dir_urls/$savename\_$num_results.txt -t 3 -T 10
  cd ../..
done
