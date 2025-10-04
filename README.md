# Praktikum Modul 1 Jarkom

|No|Nama anggota|NRP|
|---|---|---|
|1. | Tasya Aulia Darmawan | 5027241009|
|2. | Ahmad Rafi Rafi F D | 5027241068|

## Soal 1
![assets/no1.jpg](assets/no1.png)
```
> **CLI CONFIGS**

> eru
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

> clients
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
> **GUI CONFIGS**

> in Eru
edit config > `up iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE -s 192.227.0.0/16`
```
## Soal 2
![assets/no2.jpg](assets/no2.png)
```
soal 2 (same as number 1)
```
## Soal 3
![assets/no3.jpg](assets/no3.png)
![assets/no3.2.jpg](assets/no3.2.png)
```
soal 3 (same as number 1)
```
## Soal 4
![assets/no4.jpg](assets/no4.png)
```
soal 4 (same as number 1)
```
## Soal 5
![assets/no5.jpg](assets/no5.png)
![assets/no5.2.jpg](assets/no5.2.png)
![assets/no5.3.jpg](assets/no5.3.png)
```
soal 5 (same as number 1)
```
## Soal 6

```
> in manwe
wget --no-check-certificate "https://drive.google.com/uc?export=download&id=1bE3kF1Nclw0VyKq4bL2VtOOt53IC7lG5" -O traffic.zip

unzip traffic.zip

chmod +x traffic.zip

>> go to wireshark
start capture > manwe -> eru 

./traffic.sh
```
## Soal 7
![assets/no7.jpg](assets/no7.png)
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
## Soal 8
![assets/no8.1.jpg](assets/no8.1.png)
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
## Soal 9
![assets/no9.1.jpg](assets/no9.1.png)
![assets/no9.2.jpg](assets/no9.2.png)
![assets/no9.3.jpg](assets/no9.3.png)
![assets/no9.4.jpg](assets/no9.4.png)
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
## Soal 10
![assets/no10.jpg](assets/no10.png)
```
>> go to wireshark / GNS Client
start capture > melkor -> eru

> go to melkor
ping 192.227.1.1 -c 200

Analyze if theres a packet loss (it can be from capture result or the ping result)
```
## Soal 11
![assets/no11.jpg](assets/no11.png)
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
## Soal 12
![assets/no12.jpg](assets/no12.png)
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
## Soal 13
![assets/no13.jpg](assets/no13.png)
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
---

## Soal 14
```c
nc 10.15.43.32 3401
```
### Question 1
How many packets are recorded in the pcapng file?
Format: int
#### Step 1
Directly look at the bottom of the Wireshark. It shows how many packets in the PCAP file.
![assets/s14q1.jpg](assets/s14q1.jpg)
#### Answer
```c
500358
```
### Question 2
What are the user that successfully logged in?
Format: user:pass
#### Step 1
Use display filter.
```c
frame contains "success"
```
![assets/s14q2-1.jpg](assets/s14q2.jpg)
#### Step 2
Open the packet using Follow > TCP Stream.
![assets/s14q2-2.jpg](assets/s14q2-2.jpg)
#### Answer
```c
n1enna:y4v4nn4_k3m3nt4r1
```
### Question 3
In which stream were the credentials found?
Format: int
#### Step 1
Look at the "Filter". It shows tcp.stream eq [stream]
#### Answer
```c
41824
```
![assets/s14q3.jpg](assets/s14q3.jpg)
### Question 4
What tools are used for brute force?
Format: Hydra v1.8.0-dev
#### Step 1
From the same 'Follow TCP Stream', we can also notice that the tools used for brute force is
#### Answer
```c
Fuzz Faster U Fool v2.1.0-dev
```
![assets/s14q2-1.jpg](assets/s14q2-2.jpg)
### Flag
```c
Congratulations! Here is your flag: KOMJAR25{Brut3_F0rc3_N7f6C7vdFVA5f8Rn7I7O7g7nS}
```
![assets/flag14.jpg](assets/flag14.jpg)

## Soal 15
```c
nc 10.15.43.32 3402
```
### Question 1
What device does Melkor use?
Format: string
#### Step 1
Look for GET DESCRIPTOR Response DEVICE packet. Look for fields named iManufacturer, iProduct, or iSerialNumber, then I found iProduct: 2 which means it’s in the index 2 of GET DESCRIPTOR Response STRING.
![assets/s15q1.jpg](assets/s15q1.jpg)
#### Answer
```c
Keyboard
```
### Question 2
What did Melkor write?
Format: string
#### Step 1
Use filter 
```c
usb.transfer_type == 0x01
```
0x01 is from the device decription.
#### Step 2
Save, File > Export Packet Dissections as Plain Text.
#### Step 3
Run the decode_hid.py, then decode the hex.
```c
python3 decode_hid.py hid_packets.txt > decoded.txt
```
![assets/s15q2.jpg](assets/s15q2.jpg)
#### Answer
```c
UGx6X3ByMHYxZGVfeTB1cl91czNybjRtZV80bmRfcDRzc3cwcmQ=
```
### Question 3
What is Melkor's secret message?
Format: string
#### Step 1
Just decode the encoded message from question 2 above.
```c
echo "UGx6X3ByMHYxZGVfeTB1cl91czNybjRtZV80bmRfcDRzc3cwcmQ=" | base64 --decode
```
![assets/s15q3.jpg](assets/s15q3.jpg)
#### Answer
```c
Plz_pr0v1de_y0ur_us3rn4me_4nd_p4ssw0rd
```
### Flag
```c
Congratulations! Here is your flag: KOMJAR25{K3yb0ard_W4rr10r_BRxsRQ8etjElDYMOJBbksIR0d}
```
![assets/flag15.jpg](assets/flag15.jpg)
## Soal 16
```c
nc 10.15.43.32 3403
```
### Question 1
What credential did the attacker use to log in?
Format: user:pass
#### Step 1
Use display filter.
```c
ftp.request.command== "USER" || ftp.request.command == "PASS"
```
![assets/s16q1.jpg](assets/s16q1.jpg)
#### Answer
```c
ind@psg420.com:{6r_6e#TfT1p
```
### Question 2
How many files are suspected of containing malware?
Format: int
#### Step 1
Click Follow > TCP Stream from the previous way. There are q.exe, w.exe, e.exe, r.exe, t.exe. 
![assets/s16q2.jpg](assets/s16q2.jpg)
#### Answer
```c
5
```
### Question 3
What is the hash of the first file (q.exe)?
Format: sha256
#### Step 1
![assets/s16q2.jpg](assets/s16q2.jpg)
If we look at the "Follow TCP Stream", it shows like this

PASV

227 Entering Passive Mode (216,55,163,106,199,145)
227 Entering Passive Mode (h1,h2,h3,h4,p1,p2)
h1,h2,h3,h4 = IP address of the server
p1,p2 = two bytes that form the TCP port
#### Step 2
Calculate the port for filtering, by the formula
```
port = (p1*256) + p2
```
which means (for q3)
port = (199*256)+145 = 51089
#### Step 3
Do filtering with:
```c
ip.addr == 216.55.163.106 && tcp.port == 51089
```
#### Step 4
Follow > TCP Stream > Save as raw, name it q.exe
#### Step 5
Do hash sha256, with the command:
```c
sha256 q.exe
```
#### Answer
```c
ca34b0926cdc3242bbfad1c4a0b42cc2750d90db9a272d92cfb6cb7034d2a3bd
```
![assets/s16q3.jpg](assets/s16q3.jpg)
### Question 4
What is the hash of the second file (w.exe)?
Format: sha256
#### Step 1
Doing the same way as before. Do filtering with:
```c
ip.addr == 216.55.163.106 && tcp.port == 59785
```
#### Step 2
Do hash sha256, with the command:
```c
sha256 w.exe
```
#### Answer
```c
08eb941447078ef2c6ad8d91bb2f52256c09657ecd3d5344023edccf7291e9fc
```
![assets/s16q4.jpg](assets/s16q4.jpg)
### Question 5
What is the hash of the third file (e.exe)?
Format: sha256
#### Step 1
Doing the same way as before. Do filtering with:
```c
ip.addr == 216.55.163.106 && tcp.port == 49506
```
#### Step 2
Do hash sha256, with the command:
```c
sha256 e.exe
```
#### Answer
```c
32e1b3732cd779af1bf7730d0ec8a7a87a084319f6a0870dc7362a15ddbd3199
```
![assets/s16q5.jpg](assets/s16q5.jpg)
### Question 6
What is the hash of the third file (r.exe)?
Format: sha256
#### Step 1
Doing the same way as before. Do filtering with:
```c
ip.addr == 216.55.163.106 && tcp.port == 60899
```
Do hash sha256, with the command:
```c
sha256 r.exe
```
#### Answer
```c
4ebd58007ee933a0a8348aee2922904a7110b7fb6a316b1c7fb2c6677e613884
```
![assets/s16q6.jpg](assets/s16q6.jpg)
### Question 7
What is the hash of the third file (t.exe)?
Format: sha256
#### Step 1
Doing the same way as before. Do filtering with:
```c
ip.addr == 216.55.163.106 && tcp.port == 50157
```
Do hash sha256, with the command:
```c
sha256 t.exe
```
#### Answer
```c
10ce4b79180a2ddd924fdc95951d968191af2ee3b7dfc96dd6a5714dbeae613a
```
![assets/s16q7.jpg](assets/s16q7.jpg)
### Flag
```c
Congratulations! Here is your flag: KOMJAR25{Y0u_4r3_4_g00d_4nalyz3r_iDYON1mAHIfDzG2S49awKOBRm}
```
![assets/flag16.jpg](assets/flag16.jpg)
## Soal 17
```c
nc 10.15.43.32 3404
```
### Question 1
What is the name of the first suspicious file?
Format: file.exe
#### Step 1
File > Export Objects > HTTP
#### Step 2
There will be 3 files. Including the Invoice&MSO-Request.doc
![assets/s17q1.jpg](assets/s17q1.jpg)
#### Answer
```c
Invoice&MSO-Request.doc
```
### Question 2
What is the name of the second suspicious file?
Format: file.exe
#### Step 1
Use the same way as the previous question, there will be 3 files. Including the knr.exe
![assets/s17q2.jpg](assets/s17q2.jpg)
#### Answer
```c
knr.exe
```
### Question 3
What is the hash of the second suspicious file (knr.exe)?
Format: sha256
#### Step 1
File > Export Objects > HTTP > Save
#### Step 2
Do hash 256, with the command:
```c
sha256 knr.exe
```
![assets/s17q3.jpg](assets/s17q3.jpg)
#### Answer
```c
749e161661290e8a2d190b1a66469744127bc25bf46e5d0c6f2e835f4b92db18
```
### Flag
```c
Congratulations! Here is your flag: KOMJAR25{M4ster_4n4lyzer_1xcg3WUUjKpux80gm8tEdFgL0}
```
![assets/flag17.jpg](assets/flag17.jpg)
## Soal 18
```c
nc 10.15.43.32 3405
```
### Question 1
How many files are suspected of containing malware?
Format: int
#### Step 1
File > Export Objects > SMB
#### Step 2
If we look at the files, there are 2 files with the name of %5cWINDOWS%5c...
![assets/s18q1.jpg](assets/s18q1.jpg)
Some malware uses URL encoding (%5c) to obfuscate or trick antivirus, firewalls, or web filters and normal files or applications don’t use URL-encoded paths in names. So, their presence almost always suggests something crafted for exploit or stealth purposes.
#### Answer
```c
2
```
### Question 2
What is the name of the first malicious file?
Format: file.exe
#### Step 1
Look at those 2 files and the answer is:
#### Answer
```c
d0p2nc6ka3f_fixhohlycj4ovqfcy_smchzo_ub83urjpphrwahjwhv_o5c0fvf6.exe
```
### Question 3
Apa nama file berbahaya yang kedua?
Format: file.exe
#### Step 1
Look at those 2 files and the answer is:
#### Answer
```c
oiku9bu68cxqenfmcsos2aek6t07_guuisgxhllixv8dx2eemqddnhyh46l8n_di.exe
```
### Question 4
What is the hash of the first malicious file?
Format: sha256
#### Step 1
Do hash 256, with the command:
```c
sha256 %5cWINDOWS%5cd0p2nc6ka3f_fixhohlycj4ovqfcy_smchzo_ub83urjpphrwahjwhv_o5c0fvf6.exe
```
![assets/s18q4.jpg](assets/s18q4.jpg)
#### Answer
```c
59896ae5f3edcb999243c7bfdc0b17eb7fe28f3a66259d797386ea470c010040
```
### Question 5
What is the hash of the second malicious file?
Format: sha256
#### Step 1
Do hash 256, with the command:
```c
sha256 %5cWINDOWS%5coiku9bu68cxqenfmcsos2aek6t07_guuisgxhllixv8dx2eemqddnhyh46l8n_di.exe
```
![assets/s18q5.jpg](assets/s18q5.jpg)
#### Answer
```c
cf99990bee6c378cbf56239b3cc88276eec348d82740f84e9d5c343751f82560
```
### Flag
```c
Congratulations! Here is your flag: KOMJAR25{Y0u_4re_g0dl1ke_e8XQLgCWiRzzsqZm9XqENF6bY}
```
![assets/flag18.jpg](assets/flag18.jpg)
## Soal 19
```c
nc 10.15.43.32 3406
```
### Question 1
Who sent the threatening message?
Format: string (name)
#### Step 1
Look at the SMTP (Simple Mail Transfer Protocol) because it's the technique to send and receive email, by clicking the "Protocol".
#### Step 2
Do Follow > TCP Stream.
![assets/s19q1.jpg](assets/s19q1.jpg)
#### Answer
```c
Your Life
```
### Question 2
How much ransom did the attacker demand ($)?
Format: int
#### Step 1
By the same way as the previous question, the question could be easily answered by reading the content of the email.
![assets/s19q2.jpg](assets/s19q2.jpg)
#### Answer
```c
1600
```
### Question 3
What is the attacker's bitcoin wallet?
Format: string
#### Step 1
By the same way as the previous question, the question could be easily answered by reading the content of the email.
![assets/s19q3.jpg](assets/s19q2.jpg)
#### Answer
```c
1CWHmuF8dHt7HBGx5RKKLgg9QA2GmE3UyL
```
### Flag
```c
Congratulations! Here is your flag: KOMJAR25{Y0u_4re_J4rk0m_G0d_uYgq9qyc7cdrJ2F5gyBt0otqK}
```
![assets/flag19.jpg](assets/flag19.jpg)
## Soal 20
```c
nc 10.15.43.32 3407
```
### Question 1
What encryption method is used?
Format: string
#### Step 1
Identify the protocol first, it seems like it's using TLS.
#### Step 2
Use display filter.
```c
tls.handshake.type == 2
```
becuase it is when server picks the TLS version and the single cipher suite used for the session, and returns selected key_share info.
![assets/s20q1.jpg](assets/s20q1.jpg)
#### Answer
```c
TLS
```
### Question 2
What is the name of the malicious file placed by the attacker?
Format: file.exe
#### Step 1
From the folders given by the assistant, we also got keylogs.txt. Then click Wireshark > Preferences > Protocol (look for TLS) > Browse (insert the keylogs.txt). keylogs.txt is a pre-master secret log file that contains session keys generated by the browser (or attacker’s machine) during TLS handshakes. In other words:
It holds the “passwords” Wireshark needs to decrypt HTTPS traffic.
#### Step 2
Use display filter
```c
http.response.code == 200
```
Looking for 200/ success. Follow > TCP Stream, scroll up, then we can see that from the HTTP GET, there's a file named invest_20.dll
![assets/s20q2.jpg](assets/s20q2.jpg)
#### Answer
```c
invest_20.dll
```
### Question 3
What is the hash of the file containing the malware?
Format: sha256
#### Step 1
After the file has been saved (from the previous question), do hash sha256 with the command:
```c
sha256 invest_20.dll
```
![assets/s20q3.jpg](assets/s20q3.jpg)
#### Answer
```c
31cf42b2a7c5c558f44cfc67684cc344c17d4946d3a1e0b2cecb8eb58173cb2f
```
### Flag
```c
Congratulations! Here is your flag: KOMJAR25{B3ware_0f_M4lw4re_Q1lBjLY0oJ3rCllqfcUS8GO4a}
```
![assets/flag20.jpg](assets/flag20.jpg)
