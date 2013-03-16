#!/usr/bin/env python

from bs4 import BeautifulSoup
from urllib2 import urlopen
from sys import argv
from urllib import urlretrieve
from os.path import basename

def usage():
	print """
Script to download the debs for MakerWare 2.0.?  Takes three parameters: the version number (ie: 2.0.0), the architecture you want (i386 or amd64) and the version of Ubuntu you want to use it on (ie: precise)
./MakerWareDownload.py MakerwareVerison Arch UbuntuCodename
"""

#First, some input verification
if len(argv)!=4:
	usage()
	exit(1)

argv[2]=argv[2].lower()
if argv[2]!='amd64' and argv[2]!='i386':
	print "Arch must be i386 or amd64"
	usage()
	exit(1)

argv[3]=argv[3].lower()
if argv[3] not in {'quantal', 'precise', 'oneiric'}:
	print "Ubuntu codename must be one of quantal, precise or oneiric"
	usage()
	exit(1)

xml = urlopen('http://downloads.makerbot.com.s3.amazonaws.com/?prefix=makerware/ubuntu/debs/' + argv[3] + '/')
soup = BeautifulSoup(xml)
keys = soup.find_all('key')

# First pass, remove anything not a .deb
keptKeys=[]
for key in keys:
	if "deb"==key.contents[0].lower()[-3:]:
		keptKeys.append(key)
keys=keptKeys
keptKeys=[]
# second pass, if it doesnt match arch, remove it 
for key in keys:
	if argv[2] in key.contents[0].lower():
		keptKeys.append(key)

keys=keptKeys
#now lets try to get the right version
# Version umber is between underscores
packages={}
for key in keys:
	keyParts = key.contents[0].split('_')
	
	if keyParts[0] in packages:
		packages[keyParts[0]].append(keyParts[1])
	else:
		packages[keyParts[0]]=[keyParts[1]]

for package in packages.keys():
	# By deafult we keep all versions
	keepVersions=packages[package]
	for version in packages[package]:
		if argv[1] in version:
			#Found an exact match on version number
			# Keep that and ignore all others
			keepVersions=[version]
			break
	packages[package]=keepVersions

#Now fetch the files
for package in packages.keys():
	for version in packages[package]:
		filename = package + version + argv[2] + '.deb'
		urlretrieve('http://downloads.makerbot.com.s3.amazonaws.com/' + filename, basename(filename))
