#!/bin/bash

dirname="$(dirname "$0")" # Get script directory
hadoop_queue_name="eecs598w19"
HDFS_input_path="$1"
local_csv_result_path="$2"

set -x # Below this line, each command will be printed to terminal before being executed.

hdfs dfs -mkdir -p ass1
# hdfs dfs -put $HDFS_input_path/twitter_rv.net ass1/input/
hdfs dfs -rm -r ass1/output/

yarn jar "$dirname/hadoop-streaming-2.6.3.jar" \
-input $HDFS_input_path \
-output ass1/output \
-mapper map.py \
-reducer red.py \
-file map.py \
-file red.py \
-numReduceTasks 10 \
-jobconf mapred.job.queue.name=$hadoop_queue_name

hdfs dfs -get ass1/output/* $local_csv_result_path/

(echo "<node-id>, <in-degree>, <out-degree>, <total degree>" ;cat $local_csv_result_path/*)  > $local_csv_result_path/node_degrees.csv
