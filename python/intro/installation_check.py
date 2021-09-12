u"""
Produce meta information about the computer and Python.

Works on:
┌────────────┬────────────────┬───────────────┬─────────────────────────────┐
│ DATE       │ OS             │ VERSION       │ LOCATION                    │
├────────────┼────────────────┼───────────────┼─────────────────────────────┤
│ 2019-04-28 │ Ubuntu 18.04   │ Python 2.7.15 │ /usr/bin/python             │
│ 2019-05-14 │ macOS Sierra   │ Python 3.6.6  │ .../miniconda3/bin/python   │
│ 2019-04-28 │ Ubuntu 18.04   │ Python 3.6.7  │ /usr/bin/python3            │
│ 2019-07-23 │ macOS Sierra   │ Python 3.6.8  │ .../miniconda3/bin/python3  │
│ 2020-06-06 │ Ubuntu 18.04   │ Python 3.6.9  │ /usr/bin/python3.6          │
│ 2020-06-06 │ Ubuntu 18.04   │ Python 3.8.0  │ /usr/bin/python3            │
│ 2020-06-07 │ macOS Catalina │ Python 3.8.2  │ ...rsions/3.8.2/bin/python  │
│ 2020-09-06 │ Ubuntu 20.04   │ Python 3.8.2  │ /usr/bin/python3            │
│ 2021-08-31 │ macOS Big Sur  │ Python 3.9.6  │ ...rsions/3.9/bin/python3.9 │
└────────────┴────────────────┴───────────────┴─────────────────────────────┘
"""
import distro
import os
from pip._internal.operations.freeze import freeze
import platform
import subprocess
import sys
import time
import pwd

# General implementation
today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
print(f'This script was run on {today}')
print(f'This is a {platform.system()} machine')
name = platform.node()
print(f'Its name is {name}')
if platform.system() == 'Linux':
    if int(platform.python_version()[2]) >= 7:
        OS = distro.linux_distribution()[0]
        version = distro.linux_distribution()[1]
    else:
        OS = platform.linux_distribution()[0]
        version = platform.linux_distribution()[1]
    print(f'Its OS is {OS}')
    print(f'Its OS version is {version}')
elif platform.system() == 'Windows':
    OS = platform.release()
    print(f'Its OS is {OS}')
elif platform.system() == 'Darwin':
    macOS_vers = {
        '10.11': 'El Capitan',
        '10.12': 'Sierra',
        '10.13': 'High Sierra',
        '10.14': 'Mojave',
        '10.15': 'Catalina',
        '10.16': 'Big Sur',
    }
    OS = macOS_vers[platform.mac_ver()[0][:5]]
    print(f'Its OS is macOS {OS}')
    print(f'Its OS version is {platform.mac_ver()[0]}')
py = platform.python_version()
print(f'Its Python version is {py}')
path = sys.executable
print(f'Python is being run from {path}')
user = pwd.getpwuid(os.getuid())[0]
print(f'The user is {user}')
process = subprocess.Popen(
    ['git', 'rev-parse', 'HEAD'], shell=False, stdout=subprocess.PIPE
)
git_hash = process.communicate()[0].strip()
print(f'The git hash is {git_hash}')
print('The installed packages are:')
for requirement in freeze(local_only=True):
    print(requirement)

# Specific stuff
print('\n\n')
if platform.system() == 'Linux':
    print('\nWorks on:')
    print('┌────────────┬────────────────┬───────────────┬──────────────────┐')
    print(f'│ {today:10} │ {OS} {version}   │ Python {py:6} │ {path:16} │')
    print('└────────────┴────────────────┴───────────────┴──────────────────┘')
elif platform.system() == 'Darwin':
    print(f'Running with Python {py} on {name}, a macOS {OS} machine, ' +
          f'by user {user}')
    print('\nWorks on:')
    if len(sys.executable) > 28:
        path = '...' + sys.executable[-24:]
    else:
        path = sys.executable
    print('┌────────────┬────────────────┬───────────────┬' + '─' * 29 + '┐')
    print(f'│ {today} │ macOS {OS:8} │ Python {py}  │ {path:24} │')
    print('└────────────┴────────────────┴───────────────┴' + '─' * 29 + '┘')
