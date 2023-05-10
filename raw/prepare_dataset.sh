#!/bin/bash

fake='rumours'
dst_fake="dataset/fake"
dst_true="dataset/true"

openssl enc -d -aes256 -in dataset.enc -pbkdf2 -pass file:dataset.key | tar -xzf -
dirs=$(find raw_dataset -mindepth 2 -maxdepth 2 -type d)

mkdir -p $dst_fake $dst_true

for dir in $dirs; do
  type=$(basename $dir)
  if [ $type == $fake ]; then
    mv $dir/* $dst_fake
  else
    mv $dir/* $dst_true
  fi
done

rm -rf raw_dataset
