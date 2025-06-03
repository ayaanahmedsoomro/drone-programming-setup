#!/bin/bash

echo "🔐 Installing required root-level packages..."
apt-get update && apt-get upgrade -y

apt-get install -y sudo
apt-get install -y git gitk git-gui screen nano
apt-get install -y python3 python3-pip python3-opencv
apt-get install -y libtool libxml2-dev pkg-config python3-matplotlib python3-dev python3-numpy
apt-get install -y python3-pygame python3-lxml python3-setuptools python3-wheel

echo "✅ Sudo packages installed successfully."
