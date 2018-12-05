#!/bin/bash
cp -r doc _doc
find _doc -name '*.wiki' -exec ./html_of_wiki/ohow.byte {} \; -exec rm {} \;
