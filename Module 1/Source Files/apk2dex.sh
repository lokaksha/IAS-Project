#!/bin/bash

read folder_name
cd $folder_name
touch new
apk=$(find . -name "*.apk")
unzip $apk
