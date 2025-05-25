#!/bin/bash
df -h | awk '/sdb1/ {print $5}'
