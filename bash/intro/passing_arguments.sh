#!/bin/bash

# echo "Hello"
# echo $1

# firstname="$2"
# echo "My first name is $firstname"

# if [[ $1 =~ ^(-f|--firstname) ]]
# then
#     firstname="$2"
# fi
# echo "My first name is $firstname"

# while [[ "$#" -gt 0 ]]
# do case $1 in
#     -f|--firstname) firstname="$2"
#     shift;;
#     -s|--secondname) secondname="$2"
# esac
# shift
# done
# echo "My name is $firstname $secondname"

# while [[ "$#" -gt 0 ]]
# do case $1 in
#     -f|--firstname) firstname="$2"
#     shift;;
#     -s|--secondname) secondname="$2"
#     shift;;
#     -a|--age) age=20;;
#     *) echo "Unknown parameter passed: $1"
#     exit 1;;
# esac
# shift
# done
# echo "My name is $firstname $secondname, age $age"

# firstname="Adam"
# secondname="& Eve"
# while [[ "$#" -gt 0 ]]
# do case $1 in
#     -f|--firstname) firstname="$2"
#     shift;;
#     -s|--secondname) secondname="$2"
#     shift;;
#     *) echo "Unknown parameter passed: $1"
#     exit 1;;
# esac
# shift
# done
# echo "My name is $firstname $secondname"

# if [ -z "$1" ]
# then
#     echo "Running in test mode"
#     firstname="Adam"
#     secondname="& Eve"
# else
#     while [[ "$#" -gt 0 ]]
#     do case $1 in
#         -f|--firstname) firstname="$2"
#         shift;;
#         -s|--secondname) secondname="$2"
#         shift;;
#         *) echo "Unknown parameter passed: $1"
#         exit 1;;
#     esac
#     shift
#     done
# fi
# echo "My name is $firstname $secondname"

read -p 'Enter your first name ' firstname
read -p 'Enter your second name ' secondname
echo "Your name is $firstname $secondname"
