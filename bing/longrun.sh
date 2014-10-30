#!/bin/bash

for i in `seq 1 20`; do
	head -n $(($i*10)) categories.txt | tail -n 10 | cut -f 1 --complement -d ' ' | ./fetch_imgs.sh &
done
