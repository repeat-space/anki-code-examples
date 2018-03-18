#!/bin/sh

rm -rf data/profile/*
cp -R $HOME/.local/share/Anki2/anki-code/collection.anki2 $PWD/data/profile
