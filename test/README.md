## Prerequisites

1. Install [quickemu](https://github.com/quickemu-project/quickemu)

```
sudo apt-add-repository ppa:flexiondotorg/quickemu
sudo apt update
sudo apt install quickemu
```

- JRE (e.g. openjre / openjdk)

```
sudo apt install openjdk-11-jre-headless
```

- [SikuliX](https://launchpad.net/sikuli/sikulix/2.0.5/+download/sikulixide-2.0.5.jar) available at a point pointed at by $SIKULIX_JAR

- libopencv-core4.5d
- `apt install xdotool wmctrl`

```
sudo apt install libopencv-core406
```


## Running instructions

```bash
SIKULIX_JAR=$HOME/java/lib/sikulixide.jar ./bin/install-lunar.sh
```


