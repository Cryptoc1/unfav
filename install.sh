#!/bin/bash

echo "This install script will take (a very few) steps to setting up Hiroshima to work properly."
echo "You will be asked to enter your password multiple times throughout the process, so don't go anywhere (not that this is a long process anyway)."

if [ -d "/Library/WebServer/Documents/unfav" ]; then
	echo "Deleting old files..."
	sudo rm -rf /Library/WebServer/Documents/unfav
fi

echo "Moving files into the WebServer..."
sudo cp -R web-files /Library/WebServer/Documents/unfav

echo "Starting Apache (restarting if already enabled)..."
sudo apachectl restart

echo "Installing dependencies."
pip install python-twitter --upgrade
if [ -d "./python-twitter" ]; then
	echo "deleting old clone"
	rm -rf ./python-twitter
fi
echo "cloning python-twitter"
git clone https://github.com/bear/python-twitter.git
if [ -d "./twitter" ]; then
	echo "Deleting old copy of python-twitter"
	rm -rf ./twitter
fi

echo "Moving python-twitter/twitter to ./twitter"
mv python-twitter/twitter ./

echo "Process complete, wasn't so bad was it? Continue by reading instructions.md"
