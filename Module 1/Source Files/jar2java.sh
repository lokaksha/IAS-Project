#!/bin/bash

read jar
unzip -d $jar.tmp $jar
pushd $jar.tmp
for f in `find . -name '*.class'`; do
	javap -c $f >> new.java
done
popd
