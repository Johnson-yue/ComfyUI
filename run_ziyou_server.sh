#!/usr/bin/bash
# This env is conda-comfy

rm -rf temp/*
python main.py --cuda-device 3 --listen "0.0.0.0" --port 38188
