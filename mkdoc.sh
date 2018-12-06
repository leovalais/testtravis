#!/bin/bash
cp -r doc _doc
find _doc -name '*.wiki' -exec ohow {} \; -exec rm {} \;
