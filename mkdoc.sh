#!/bin/bash
set -x

wget https://raw.githubusercontent.com/ocaml/ocaml-travisci-skeleton/master/.travis-ocaml.sh
bash -ex .travis-ocaml.sh

eval $(opam env)

git clone -b ohow --single-branch https://github.com/ocsigen/html_of_wiki.git
opam pin add -y html_of_wiki html_of_wiki

cp -r doc _doc
find _doc -name '*.wiki' -exec ohow {} \; -exec rm {} \;
