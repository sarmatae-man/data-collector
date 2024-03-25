#! /bin/bash
# Установка Docker
# https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-22-04
# docker inspect --format='{{.Id}} {{.Parent}}' $(docker images --filter since=f093df10d054 -q)
# https://www.postman.com/tauc-2005/workspace/my-public/request/create?example=6517789-1202e4ae-e3f0-4c2f-bba5-e482093e07c4&requestId=bac05224-3b19-4b52-bbf0-0e528fcb7657
sudo apt-get update
sudo apt-get install chrony -y
sudo apt-get install mc -y
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
sudo echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
"$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
# Проверка запуском
# sudo docker run hello-world
# Управление Docker от имени пользователя, который не является root
sudo groupadd docker
sudo usermod -aG docker $USER
# Активировать изменения (или перелогинится)
sudo newgrp docker
# Включить автозапуск
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
# установка для синхронизации времени
sudo apt-get install chrony -y
sudo systemctl enable chrony
sudo systemctl start chrony
sudo timedatectl set-timezone Europe/Moscow

# swapfile 1Gb
SWAP_SIZE=1G
sudo fallocate -l $SWAP_SIZE /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab


