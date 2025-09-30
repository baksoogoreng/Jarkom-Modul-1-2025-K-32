# Praktikum Modul 1 Jarkom

|No|Nama anggota|NRP|
|---|---|---|
|1. | Tasya Aulia Darmawan | 5027241009|
|2. | Ahmad Rafi Rafi F D | 5027241068|

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
http.request.method == "POST"
```
![assets/s14q2-1.jpg](assets/s14q2-1.jpg)
#### Step 2
Open the packet using Follow > TCP Stream.
#### Explanation
At first I opened the first packet from the bottom, but it's still the invalid credentials. Then, I go click the second packet from the bottom and it shows the correct credentials.
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
![assets/s14q2-1.jpg](assets/s14q2-1.jpg)
### Flag
```c
Congratulations! Here is your flag: KOMJAR25{Brut3_F0rc3_N7f6C7vdFVA5f8Rn7I7O7g7nS}
```

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
### Flag
```c

```
