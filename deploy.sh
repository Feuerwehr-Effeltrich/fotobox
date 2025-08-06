#! /usr/bin/env bash

HOST='fotobox'

ansible-playbook -i "$HOST", ansible.yml
