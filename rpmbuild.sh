#!/bin/bash

set -e

# Expects $1 to be the version to build
if [ "x$1" = "x" ]; then
    echo "Expecting version number as argument"
    exit 1 
fi

git clone https://github.com/indigo-dc/opie -b $1 /tmp/opie 

pushd /tmp/opie
python setup.py sdist
cp dist/opie-$1.tar.gz /home/builder/rpmbuild/SOURCES/ 
popd 

rpmbuild -ba /home/builder/rpmbuild/SPECS/opie.spec
