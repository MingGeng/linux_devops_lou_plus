

#coding=utf-8

import os, sys

if os.getuid() == 0:
    pass
else:
    print 'Current use is not root, please use root to make me work!'    
    sys.exit(1)

version = raw_input('Please input which python version you\'d like to install(2.7/3.5)')

if version == '2.7':
    url = 'http://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz'
elif version == '3.5':
    url = 'http://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz'
else:
    print 'Input python version error!'
    sys.exit(1)

cmd = 'wget ' + url
res = os.system(cmd)
if res != 0:
    print 'Download failed, please check the network!'
    os.system('rm *.tgz' )
    sys.exit(1)

if version == '2.7':
    package_name = 'Python-2.7.12'
else:
    package_name = 'Python-3.5.2'

cmd = 'tar xf ' + package_name + '.tgz'
res = os.system(cmd)
if res != 0:
    print 'Broken package! Please run me again!'
    os.system('rm ' + package_name + '.tgz')
    sys.exit(1)

cmd = 'cd ' + package_name + '&& ./configure --prefix=/home/shiyanlou/bin/python && make && make install'
 
res = os.system(cmd)

if res != 0:
    print 'Compile failed! Check if missing libs!'
else:
    print 'Python' + package_name +' Installed!'
