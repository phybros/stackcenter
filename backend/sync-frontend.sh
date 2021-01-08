#!/bin/bash

set -eux

mkdir -p static
rm -rf static/*

pushd ../frontend
yarn build

popd

cp -a ../frontend/dist/* static/
