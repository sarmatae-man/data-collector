#!/bin/bash

sudo apt-get -y update 
# если пользователь не в 
# sudo
# add USER to sudo
#sudo useradd -ms /bin/bash $USER && echo "$USER:docker" | chpasswd && adduser $USER sudo
sudo adduser $USER sudo
sudo usermod -aG sudo $USER
#sudo echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
# openssh-server
sudo apt-get install -y samba python3-pip git mc nano tmux 
sudo apt-get install opevpn -y
sudo pip3 install datetime jinja2 openpyxl beautifulsoup4 psutil yfinance
#sudo cp /etc/samba/smb.conf /etc/samba/res_smb.conf
#sudo grep -v '^ *#\|^ *$' /etc/samba/smb.conf | tee /etc/samba/smb.conf
# samba config all users with passwd
#sudo echo "[${USER}]" >> /etc/samba/smb.conf
#sudo echo "  path = /home/${USER}/data-collector/moex_data" >> /etc/samba/smb.conf
#sudo echo "  writable = yes" >> /etc/samba/smb.conf
#sudo echo "  guest ok = no" >> /etc/samba/smb.conf
#sudo echo "  public = no" >> /etc/samba/smb.conf
#sudo echo "  valid users = ${USER}" >> /etc/samba/smb.conf
cd /home/$USER/
mkdir /home/$USER/.ssh
touch /home/$USER/.ssh/authorized_keys
sudo git clone https://github.com/sarmatae-man/data-collector.git 
sudo mkdir -p /home/$USER/data-collector/moex_all_data
sudo mkdir -p /home/$USER/app
#sudo mkdir -p /home/$USER/data-collector/data
sudo mkdir -p /home/$USER/data-collector/zip
sudo mkdir -p /home/$USER/data-collector/log
sudo mkdir -p /home/$USER/data-collector/data/moex_IMOEX_stocks
sudo mkdir -p /home/$USER/data-collector/data/moex_currencies
sudo mkdir -p /home/$USER/data-collector/data/moex_indexes
sudo mkdir -p /home/$USER/data-collector/data/moex_watch_list
sudo mkdir -p /home/$USER/data-collector/data/global_indexes
sudo mkdir -p /home/$USER/data-collector/data/global_currencies
#sudo mkdir -p /home/$USER/futures
#sudo mkdir -p /home/$USER/data-collector/data/global_futures
#sudo mkdir -p /home/$USER/data-collector/data/protoforma
sudo chmod -R a+rX /home/$USER/data-collector
# sudo cp /home/$USER/data-collector/moex_app/_format.xml /home/$USER/data-collector/moex_data/watch_list/
sudo touch /home/$USER/data-collector/data/moex_watch_list/watch_list.txt
#sudo chmod 0666 /home/$USER/data-collector/data/moex_watch_list/watch_list.txt
#sudo chmod 1777 /home/$USER/data-collector/data/moex_watch_list/watch_list.txt
#sudo chmod -x /home/$USER/data-collector/data/moex_watch_list/watch_list.txt
sudo chmod 0777 /home/$USER/app

#sudo ufw allow 22
#sudo ufw allow 33333
#sudo ufw allow 30003
#sudo ufw allow 445
#sudo ufw default deny incoming
#sudo ufw default deny outgoing
#sudo ufw reload
#sudo ufw enable

#RUN sudo find /home/$USER/data-collector/moex_data -type f -delete


