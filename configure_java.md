##Configure Java on the AWS ubuntu machine

The following commands were used to install java on aws machine
```
scp  -i beertag.pem jdk-7u79-linux-i586.tar.gz   ubuntu@xxx.xxx.xxx.xxx:
sudo apt-get update
sudo mkdir /usr/local/java
sudo cp jdk-7u79-linux-i586.tar.gz /usr/local/java/
sudo tar xvzf jdk-7u79-linux-i586.tar.gz
mv jdk1.7.0_79/ jdk1.7

sudo update-alternatives --install "/usr/bin/java" "java" "/usr/local/java/jdk1.7/jre/bin/java" 1
sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/local/java/jdk1.7/bin/javac" 1
sudo update-alternatives --set java /usr/local/java/jdk1.7/jre/bin/java
sudo update-alternatives --set javac /usr/local/java/jdk1.7/bin/javac 
sudo apt-get install libc6-i386
```
