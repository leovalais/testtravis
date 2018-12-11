#!/bin/bash
set -x

# Requires: wget, git, opam, html_of_wiki, jq, comm, find, awk

wget https://raw.githubusercontent.com/ocaml/ocaml-travisci-skeleton/master/.travis-ocaml.sh
bash -ex .travis-ocaml.sh

eval $(opam env)

git clone -b ohow --single-branch https://github.com/ocsigen/html_of_wiki.git
opam pin add -y html_of_wiki html_of_wiki

# wget https://raw.githubusercontent.com/ocsigen/ocsigen.github.io/master/template.wiki 
wget https://raw.githubusercontent.com/ocsigen/ocsigen.github.io/e6b93e987b75be99e8ef30601460f60028c615fd/template.wiki

f=$(mktemp)
cat >f <<EOF
{
    "api": "api",
    "menu": true,
    "templates": ["template.wiki"],
    "manual": "manual",
    "assets": "manual/files",
    "images": "manual/files"
}
EOF
quickdop -f doc _doc -t json -c X -viu
