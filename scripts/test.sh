#!/bin/sh

for test_file in src/tests/*_test.py; do
  ./scripts/copy-profile.sh
  echo "\nrunning $test_file\n"
  python3 $test_file
done

./scripts/copy-profile.sh
