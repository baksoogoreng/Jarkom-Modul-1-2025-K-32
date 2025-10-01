# Modul 1 Praktikum Jarkom
## hi, im persephone.
### this is the things that u/i need to do JARKOM MD 1 (1-13)

#### Configs (CLI and GUI)

> **CLI CONFIGS**

> eru
```
apt update
apt install -y iptables
apt install -y wget
apt install -y unzip
apt install -y vsftpd
apt install -y netcat-traditional
apt install -y ftp
apt install -y telnet
apt install -y openssh-server	
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE -s 192.227.0.0/16
echo nameserver 192.168.122.1 > /etc/resolv.conf
```

> clients
```
apt update
apt-get install -y wget
apt-get install -y unzip
apt-get install -y vsftpd
apt-get install -y netcat-traditional
apt-get install -y ftp
apt-get install -y openbsd-inetd telnetd
apt-get install -y telnet
apt-get install -y apache2
apt-get install -y openssh-server
echo nameserver 192.168.122.1 > /etc/resolv.conf

> MUST [source /root/.bashrc] after login, idk it's installed but not unpacked.
```
> **GUI CONFIGS**

> in Eru
edit config > `up iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE -s 192.227.0.0/16`

`telnet 10.15.43.32 5***` <-- for connecting to nodes

---

#### Number 6-13

> NUMBER 6
```
> in manwe
wget --no-check-certificate "https://drive.google.com/uc?export=download&id=1bE3kF1Nclw0VyKq4bL2VtOOt53IC7lG5" -O traffic.zip

unzip traffic.zip

chmod +x traffic.zip

>> go to wireshark
start capture > manwe -> eru 

./traffic.sh
```

> NUMBER 7
```
> in eru
apt update && apt-get install vsftpd -y && apt install ftp -y (if its not installed yet)

mkdir -p /srv/ftp/shared

adduser ainur
adduser melkor
usermod -d /srv/ftp/shared ainur
chown ainur:ainur /srv/ftp/shared
chmod 755 /srv/ftp/shared
usermod -d /srv/ftp/shared melkor

> config the vsftpd
nano /etc/vsftpd.conf

listen=YES
listen_ipv6=NO
anonymous_enable=NO
local_enable=YES
write_enable=YES
chroot_local_user=YES
allow_writeable_chroot=YES
userlist_enable=YES
userlist_file=/etc/vsftpd.user_list
userlist_deny=YES

> add melkor to userlist
echo "melkor" > /etc/vsftpd.user_list

/usr/sbin/vsftpd /etc/vsftpd.conf & (to run)
netstat -tulnp | grep :21 (check if running)
pkill vsftpd (kill run)

> in eru (still)
echo "hi" > test.txt

ftp 192.227.1.1
login > ainur -> has to be logged in (can GET PUT ls)
PUT test.txt (to test)

login > melkor -> CANT logged in
```

> NUMBER 8
```
> in ulmo
login ftp > ftp 192.227.2.1
wget --no-check-certificate "https://drive.google.com/uc?export=download&id=11ra_yTV_adsPIXeIPMSt0vrxCBZu0r33" -O ramalan-cuaca.zip
unzip ramalan-cuaca.zip

> go to eru
service vsftpd start

>> on wireshark
start capture > Ulmo -> eru

> go back to ulmo
put <ramalan_cuaca files>
```

> Number 9
```
> in eru
wget --no-check-certificate "https://drive.google.com/uc?export=download&id=11ua2KgBu3MnHEIjhBnzqqv2RMEiJsILY" -O kitab_penciptaan.zip
unzip kitab_penciptaan.zip

login ftp > ftp 192.227.1.1 with ainur
put kitab_penciptaan.txt

service vsftpd start (klo mati/blm nyala)

>> on wireshark
start capture > manwe -> eru

> go to manwe
login ftp > ftp 192.227.1.1 with ainur
get kitab_penciptaan.txt

> go back to eru 
chown root:root /srv/ftp/shared
chmod 555 /srv/ftp/shared

> config the vsftpd
nano /etc/vsftpd.conf

listen=YES
listen_ipv6=NO
anonymous_enable=NO
local_enable=YES
write_enable=NO   <--- this one
chroot_local_user=YES
allow_writeable_chroot=YES
userlist_enable=YES
userlist_file=/etc/vsftpd.user_list
userlist_deny=YES

pkill vsftpd
/usr/sbin/vsftpd /etc/vsftpd.conf &
netstat -tulnp | grep :21

> go back to manwe (e.g)
echo "hiii" > test2.txt
login ftp > ftp 192.227.1.1 with ainur (it should be -xr)
put test2.txt -> should be 500 permission denied
```

> Number 10
```
>> go to wireshark / GNS Client
start capture > melkor -> eru

> go to melkor
ping 192.227.1.1 -c 200

Analyze if theres a packet loss (it can be from capture result or the ping result)
```

> Number 11
```
> on melkor
apt update
apt install openbsd-inetd telnetd -y || which telnetd <-- IT HAS TO BE `openbsd- `

> config inet.conf
nano /etc/inetd.conf
telnet  stream  tcp     nowait  root    /usr/sbin/tcpd  /usr/sbin/telnetd

pkill inetd 2>/dev/null 
/usr/sbin/inetd /etc/inetd.conf &  || service openbsd-inetd start
netstat -tulnp | grep :23

adduser <tester>
passwd <tester>

>> on wireshark
start capture : eru -> melkor
with filter : telnet

> go back to eru
sudo apt install -y telnet || which telnet 

telnet 192.227.1.2
login telnet -> new user

Analyze the capture of telnet
```

> Number 12
```
> in eru
apt-get install netcat-traditional

> go to melkor
apt update && apt install vsftpd
apt update && apt install apache2 -y

service vsftpd start
service apache2 start

> go back to eru
nc -zv 192.227.1.2 21 80 666
```

> Number 13
```
> in eru
apt update && apt install -y openssh-server (if haven't installed)

service ssh start || /etc/init.d/ssh start
service ssh status || netstat -tulnp | grep :22

adduser <tester>
passwd <tester>

>> on wireshark
start capture : eru -> verda

> go back to verda
apt install -y openssh-client (if haven't installed)
ssh <tester>@192.227.1/2.1
```

`Well goodbye for now, farewell. 07 - persephone`
