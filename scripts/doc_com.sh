#!/bin/bash

# Сделать commit контейнера с образом doc:one
docker commit $(docker ps -qf "ancestor=doc:one") doc:one

# Сделать commit контейнера с образом doc:two
#docker commit $(docker ps -qf "ancestor=doc:two") doc:two
