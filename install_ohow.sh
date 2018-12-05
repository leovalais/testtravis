#!/bin/bash

set -e

git clone https://github.com/ocsigen/html_of_wiki
cd html_of_wiki
git checkout ohow
cd -
make -C html_of_wiki ohow
