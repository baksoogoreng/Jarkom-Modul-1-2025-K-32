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
#### Step 2
Open the packet using Follow > TCP Stream.
##### Explanation
At first I opened the first packet from the bottom, but it's still the invalid credentials. Then, I go click the second packet from the bottom and it shows the correct credentials.
#### Answer
```c
n1enna:y4v4nn4_k3m3nt4r1
```
### Question 3
What tools are used for brute force?
Format: Hydra v1.8.0-dev
#### Step 1
From the same 'Follow TCP Stream', we can also notice that the tools used for brute force is
#### Answer
```c
Fuzz Faster U Fool v2.1.0-dev
```
