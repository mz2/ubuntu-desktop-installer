#!/bin/bash

set -e pipefail

if [ -f ./vm/lunar.qcow2 ]; then
  echo "kinetic VM already exists at ./vm/lunar.qcow2. Remove it and try again."
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
java -jar $SIKULIX_JAR -r lunar-installer-until-partitioning.sikuli
java -jar $SIKULIX_JAR -r lvm-with-encryption.sikuli
java -jar $SIKULIX_JAR -r start-installing.sikuli
java -jar $SIKULIX_JAR -r lunar-installer-after-partitioning.sikuli

echo "Check post-install state"
killall -9 lunar || /bin/true
sleep 5

quickemu --vm lunar.conf --display spice
java -jar $SIKULIX_JAR -r post-install-boot-menu.sikuli
sleep 5

killall -9 lunar || /bin/true
sleep 5

quickemu --vm lunar.conf --display spice
java -jar $SIKULIX_JAR -r post-install-boot-menu-with-ubuntu.sikuli
java -jar $SIKULIX_JAR -r enter-encryption-passphrase.sikuli
java -jar $SIKULIX_JAR -r lunar-post-install.sikuli

SIKULI_EXIT=$?

echo "Finished sikulix"

set e pipefail
killall lunar || /bin/true

exit $SIKULI_EXIT
