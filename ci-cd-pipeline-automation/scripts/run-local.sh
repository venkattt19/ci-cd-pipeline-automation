#!/usr/bin/env bash
set -e
docker build -t ci-cd-demo:local .
docker run --rm -p 5000:5000 ci-cd-demo:local
