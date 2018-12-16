#!/bin/bash

#$1 == name of new component; $2 == filepath to inherit from.
TARGET_NAME=$1
TARGET=./src/components/$1

mkdir -p $TARGET

cp -f ./components/genericComponent.js $TARGET/$TARGET_NAME.js
sed -e "s/genericComponent/$TARGET_NAME/g" $TARGET_NAME.js

cp -f ./components/genericComponent.css $TARGET/$TARGET_NAME.css
sed -e "s/genericComponent/$TARGET_NAME/g" $TARGET_NAME.css
