#!/bin/bash

docker run --rm -ti \
    -v $PWD/:/app:z \
    generative_music:latest \
    bash