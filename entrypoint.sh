#!/bin/bash
set -e

ROOT=$PWD
SCRIPT=artifacts/script.sh

# remember to pull if you're working on a local copy
if [ ! -d litex-buildenv.wiki ]; then
  git clone https://github.com/timvideos/litex-buildenv.wiki
fi
cp litex-buildenv.wiki/Zephyr.md artifacts

python3 -m pip install --user dataclasses
python3 -m pip install --user git+git://github.com/antmicro/tuttest

python3 extract.py artifacts/Zephyr.md > $SCRIPT

echo "Running following script extracted from tutorial:"
cat $ROOT/$SCRIPT
chmod +x $ROOT/$SCRIPT
$ROOT/$SCRIPT

