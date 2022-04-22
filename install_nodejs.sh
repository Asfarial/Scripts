#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m' # No Color

VERSION=v16.14.2
DISTRO=linux-x64

echo -e "${GREEN}NodeJS Installation Script"

echo -e "1/5 Downloading NodeJS $VERSION ...${NC}"
wget -c https://nodejs.org/dist/$VERSION/node-$VERSION-$DISTRO.tar.xz -P ~/Downloads

echo -e "${GREEN}2/5 Installing. Unpacking...${NC}"
sudo mkdir -p /usr/local/lib/nodejs
sudo tar -xJvf ~/Downloads/node-$VERSION-$DISTRO.tar.xz -C /usr/local/lib/nodejs

echo -e "${GREEN}3/5 Installing. Setting Environment...${NC}"
sed -i 's/^#.*nodejs.*$//gi' ~/.profile
sed -i 's/^export PATH=\/usr\/local\/lib\/nodejs\/node.*$//g' ~/.profile
echo -e "# Nodejs" | tee -a ~/.profile
echo -e "export PATH=/usr/local/lib/nodejs/node-$VERSION-$DISTRO/bin:$PATH" | tee -a ~/.profile
. ~/.profile

echo -e "${GREEN}4/5 Installing. Making Symlinks...${NC}"
sudo ln -sf /usr/local/lib/nodejs/node-$VERSION-$DISTRO/bin/node /usr/bin/node
sudo ln -sf /usr/local/lib/nodejs/node-$VERSION-$DISTRO/bin/npm /usr/bin/npm
sudo ln -sf /usr/local/lib/nodejs/node-$VERSION-$DISTRO/bin/npx /usr/bin/npx

echo -e "${GREEN}5/5 Testing. Check versions manually${NC}"
node -v
npm version
npx -v

echo -e "${GREEN}Finished${NC}"
