u"""
Produce meta information about the computer and Python.

Works on:
┌────────────┬────────────────┬───────────────┬───────────────────────────────┐
│ DATE       │ OS             │ VERSION       │ LOCATION                      │
├────────────┼────────────────┼───────────────┼───────────────────────────────┤
│ 2019-04-28 │ Ubuntu 18.04   │ Python 2.7.15 │ /usr/bin/python               │
│ 2019-05-14 │ macOS Sierra   │ Python 3.6.6  │ ...owan/miniconda3/bin/python │
│ 2019-04-28 │ Ubuntu 18.04   │ Python 3.6.7  │ /usr/bin/python3              │
│ 2019-07-23 │ macOS Sierra   │ Python 3.6.8  │ ...wan/miniconda3/bin/python3 │
│ 2020-06-06 │ Ubuntu 18.04   │ Python 3.6.9  │ /usr/bin/python3.6            │
│ 2020-06-06 │ Ubuntu 18.04   │ Python 3.8.0  │ /usr/bin/python3              │
│ 2020-06-07 │ macOS Catalina │ Python 3.8.2  │ .../Versions/3.8.2/bin/python │
│ 2020-09-06 │ Ubuntu 20.04   │ Python 3.8.2  │ /usr/bin/python3              │
│ 2021-08-31 │ macOS Big Sur  │ Python 3.9.6  │ ...Versions/3.9/bin/python3.9 │
│ 2022-01-08 │ Ubuntu 20.04   │ Python 3.9.5  │ /usr/bin/python3              │
│ 2022-01-08 │ Ubuntu 20.04   │ Python 3.10.1 │ /usr/local/bin/python3        │
│ 2023-12-05 │ Ubuntu 22.04   │ Python 3.12.0 │ /usr/local/bin/python3        │
│ 2023-12-05 │ macOS Sonoma   │ Python 3.12.0 │ ...rsions/3.12/bin/python3.12 │
└────────────┴────────────────┴───────────────┴───────────────────────────────┘
"""
import distro
import os
from pip._internal.operations.freeze import freeze
import platform
import subprocess
import sys
from datetime import date
import pwd

today = date.today()
print(f'This script was run on {today}')

# Information about the computer
core_os = platform.system()
print(f'This is a {core_os} machine')
if core_os == 'Linux':
    # Check which version of Python you are running
    major = platform.python_version().split('.')[0]
    minor = platform.python_version().split('.')[1]
    # Check which operating system you have
    if (int(major) == 3) & (int(minor) <= 4):
        # Python 3.4 or lower
        OS = platform.linux_distribution()[0]
        version = platform.linux_distribution()[1]
    else:
        # Check which version of the distro package you have installed
        major = distro.__version__.split('.')[0]
        minor = distro.__version__.split('.')[1]
        if (int(major) <= 1) & (int(minor) <= 4):
            # distro 1.4 or lower
            OS = distro.linux_distribution()[0]
            version = distro.linux_distribution()[1]
        else:
            # distro 1.5.0 or higher
            OS = distro.name()
            version = distro.version()
    print(f'Its OS is {OS}')
    print(f'Its OS version is {version}')
elif core_os == 'Windows':
    OS = platform.system()
    version = platform.release()
    print(f'Its OS version is {version}')
elif core_os == 'Darwin':
    # Check which version of macOS you have
    version = platform.mac_ver()[0]
    major = version.split('.')[0]
    minor = version.split('.')[1]
    if int(major) == 10:
        macOS_vers = {
            '10.11': 'El Capitan',
            '10.12': 'Sierra',
            '10.13': 'High Sierra',
            '10.14': 'Mojave',
            '10.15': 'Catalina',
        }
        OS = macOS_vers[f'{major}.{minor}']
    else:
        macOS_vers = {
            '11': 'Big Sur',
            '12': 'Monterey',
            '13': 'Ventura',
            '14': 'Sonoma',
        }
        OS = macOS_vers[major]
    print(f'Its OS is macOS {OS}')
    print(f'Its OS version is {platform.mac_ver()[0]}')
name = platform.node()
print(f'Its name is {name}')
user = pwd.getpwuid(os.getuid())[0]
print(f'The user is {user}')

# Information about the Git repo
process = subprocess.Popen(
    ['git', 'rev-parse', 'HEAD'], shell=False, stdout=subprocess.PIPE
)
git_hash = process.communicate()[0].strip()
print(f'The git hash is {git_hash}')

# Information about the Python installation
py = platform.python_version()
print(f'The Python version is {py}')
path = sys.executable
print(f'Python is being run from {path}')
print('The installed packages are:')
for requirement in freeze(local_only=True):
    print(requirement)

# Formatted output
print('\n\n')
if platform.system() == 'Linux':
    print(f'Running with Python {py} on {name}, an {OS} {version} machine, ' +
          f'by user {user}')
    print('\nWorks on:')
    print('┌────────────┬────────────────┬───────────────┬──' + '─' * 22 + '┐')
    print(f'│ {today} │ {OS} {version}   │ Python {py:6} │ {path:16} │')
    print('└────────────┴────────────────┴───────────────┴──' + '─' * 22 + '┘')
elif platform.system() == 'Darwin':
    print(f'Running with Python {py} on {name}, a macOS {OS} machine, ' +
          f'by user {user}')
    print('\nWorks on:')
    if len(sys.executable) > 28:
        path = '...' + sys.executable[-26:]
    else:
        path = sys.executable
    print('┌────────────┬────────────────┬───────────────┬──' + '─' * 29 + '┐')
    print(f'│ {today} │ macOS {OS:8} │ Python {py} │ {path:29} │')
    print('└────────────┴────────────────┴───────────────┴──' + '─' * 29 + '┘')
