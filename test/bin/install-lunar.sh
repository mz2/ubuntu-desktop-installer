#!/bin/bash

# Accept the "scenario" as a command line argument
scenario=$1
echo $scenario

set -e pipefail

cp spicy-settings ~/.config/spicy/settings

# if an image does not exist at ~/images/lunar-desktop-amd64.iso
# or its modification time is older than yesterday,
# then download an image from
# https://cdimage.ubuntu.com/ubuntu/daily-live/current/lunar-desktop-amd64.iso
if [ ! -f ~/images/lunar-desktop-amd64.iso ] || [ $(find ~/images/lunar-desktop-amd64.iso -mtime +1) ]; then
  echo "Downloading lunar-desktop-amd64.iso"
  curl -L https://cdimage.ubuntu.com/ubuntu/daily-live/current/lunar-desktop-amd64.iso -o ~/images/lunar-desktop-amd64.iso
fi

if [ ! -f ./lunar-desktop-amd64.iso ]; then
  echo "Missing iso (symlink it in, please, and try again)."
  exit 1
fi

if [ -z "${SIKULIX_JAR}" ]; then
  echo "Missing 'SIKULIX_JAR' environment variable (point it at your sikulixide jar, please, and try again)."
  exit 1
fi


# Choose the lunar.conf file based on the "scenario" provided
case "$scenario" in
  "win11")
    config_file="lunar-win11.conf"
    ;;
  "win11-bitlocker")
    config_file="lunar-win11-bitlocker.conf"
    ;;
  "blank")
    config_file="lunar.conf"
    rm -rf vm/lunar.*
    ;;
  *)
    echo "Unknown scenario: $scenario"
    exit 1
    ;;
esac

killall -9 $scenario || /bin/true

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

echo "Lunar installer until partitioning"
java -jar $SIKULIX_JAR -r lunar-installer-until-partitioning.sikuli

echo "LVM with encryption"
java -jar $SIKULIX_JAR -r lvm-with-encryption.sikuli

echo "Security key"
java -jar $SIKULIX_JAR -r security-key.sikuli

echo "Start installing"
java -jar $SIKULIX_JAR -r start-installing.sikuli

echo "Lunar installer after partitioning"
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

echo "Post-install boot menu with Ubuntu installed"
java -jar $SIKULIX_JAR -r post-install-boot-menu-with-ubuntu.sikuli

echo "Enter encryption passphrase"
java -jar $SIKULIX_JAR -r enter-encryption-passphrase.sikuli

echo "Lunar post-install"
java -jar $SIKULIX_JAR -r lunar-post-install.sikuli

SIKULI_EXIT=$?

echo "Finished sikulix"

set e pipefail
killall lunar || /bin/true

exit $SIKULI_EXIT
