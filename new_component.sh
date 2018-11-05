#!/bin/bash

TARGET=./src/components/$1
mkdir -p $TARGET
component=$(basename $1)
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"

cp -f $DIR/data/generic_component.html $TARGET/index.html
sed -i -e 's/MyComponent/'"$component"'/g' $TARGET/index.html

cp -f $DIR/data/generic_component_virtual.html $TARGET/_index.html
sed -i -e 's/MyComponent/'"$component"'/g' $TARGET/_index.html

cp -f $DIR/data/generic_component.js $TARGET/driver.js
sed -i -e 's/MyComponent/'"$component"'/g' $TARGET/driver.js

cp -f $DIR/data/generic_component.css $TARGET/style.css
sed -i -e 's/MyComponent/'"$component"'/g' $TARGET/style.css
