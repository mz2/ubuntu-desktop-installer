#!/bin/bash

set -e pipefail

if [ -f ./vm/lunar.qcow2 ]; then
  echo "kinetic VM already exists at ./vm/kinetic.qcow2. Remove it and try again."
  exit 1
fi

if [ ! -f ./lunar-desktop-amd64.iso ]; then
  echo "Missing ./kinetic-desktop-canary-amd64.iso (symlink it in, please, and try again)."
  exit 1
fi

if [ -z "${SIKULIX_JAR}" ]; then
  echo "Missing 'SIKULIX_JAR' environment variable (point it at your sikulixide jar, please, and try again)."
  exit 1
fi 

mkdir -p vm
sleep 1
quickemu --vm lunar.conf --display spice

echo "Starting sikulix"

echo "Setting up display"
java -jar $SIKULIX_JAR -r initialize.sikuli
sleep 5

echo "Boot menu..."
java -jar $SIKULIX_JAR -r boot-menu.sikuli
sleep 5

echo "Installer..."
java -jar $SIKULIX_JAR -r gnome-first-run.sikuli
java -jar $SIKULIX_JAR -r lunar-installer-automation.sikuli
# java -jar $SIKULIX_JAR -r installer-automation.sikuli
SIKULI_EXIT=$?

echo "Finished sikulix"

set e pipefail
killall lunar || /bin/true

exit $SIKULI_EXIT
