#! /usr/bin/env bash

HOST='fotobox'

set -e

cd $(dirname $0)

ansible-playbook -i "$HOST", -e "cwd=$(pwd)" deploy/ansible_deploy.yml
