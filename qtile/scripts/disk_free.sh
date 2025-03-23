#!/bin/bash
df -h | grep "sdb3" | awk '{print $5}'
