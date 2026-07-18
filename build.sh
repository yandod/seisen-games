#!/bin/bash
set -e

docker build -t seisen-games-build .
docker run --rm -v "$(pwd)/build:/app/build" seisen-games-build
