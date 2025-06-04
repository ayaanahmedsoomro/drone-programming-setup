#!/bin/bash

echo "🔐 Installing system-level packages..."
apt-get update && apt-get upgrade -y

apt-get install -y sudo git screen nano rsync wget curl \
    python3 python3-pip python3-venv python3-dev \
    python3-numpy python3-opencv python3-lxml python3-pygame \
    libtool libxml2-dev pkg-config g++ make

echo "✅ Done installing sudo packages"
