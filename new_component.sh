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

#!/bin/bash

#$1 == name of new component; $2 == filepath to inherit from.
TARGET_NAME=$1
TARGET=./src/components/$1
INHERIT_FROM=$2
SOURCE_NAME=$(basename $2)

mkdir -p $TARGET

cp -f ../$INHERIT_FROM/$SOURCE_NAME.html $TARGET/$TARGET_NAME.html

cp -f ../$INHERIT_FROM/_$SOURCE_NAME.html $TARGET/_$TARGET_NAME.html

cp -f ../$INHERIT_FROM/$SOURCE_NAME.js $TARGET/$TARGET_NAME.js

cp -f ../$INHERIT_FROM/$SOURCE_NAME.css $TARGET/$TARGET_NAME.css

