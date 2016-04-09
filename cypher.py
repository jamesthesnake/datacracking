import base64
import binascii
#base 64 message
dataText64="bHRzbmV0Lm5ldC9jaGFsbGVuZ2U"
#secert key message in base 64
keyData64 ="JwUTMy5NG3UfPnQrIQx3KyMIEicuAhY5DmEbeDZmHD82TRd+CE1jJT\
cKbUo0FGYyNmcCPR8SAXwgBBdb"
#theyellow string in base 64
dataTextTwo64="RmluZExUUw=="
 #the yellow stirng in binary
dataTextBinaryTwo="01000110011010010110111001100100010011000101010001010011"
#bsae 64 in binary
dataTextBinary="01101100 01110100 01110011 01101110 01100101 01110100 00101110 01101110 01100101 01110100 00101111 01100011 01101000 01100001 01101100 01101100 01100101 01101110 01100111 01100101"
#key in binary
keyDataBinary= "00100111 00000101 00010011 00110011 00101110 01001101 00011011 01110101 00011111 00111110 01110100 00101011 00100001 00001100 01110111 00101011 00100011 00001000 00010010 00100111 00101110 00000010 00010110 00111001 00001110 01100001 00011011 01111000 00110110 01100110 00011100 00111111 00110110 01001101 00010111 01111110 00001000 01001101 01100011 00100101 00110111 00001010 01101101 01001010 00110100 00010100 01100110 00110010 00110110 01100111 00000010 00111101 00011111 00010010 00000001 01111100 00100000 00000100 00010111 01011011"
#secert message
keyDataHex="270513332e4d1b751f3e742b210c772b230812272e0216390e611b7836661c3f364d177e084d6325370a6d4a341466323667023d1f12017c2004175b"
data = base64.b64decode(keyData64)
key = dataText64
binaryString=""
binaryStringTwo=""
j=1
m=1
for k in range( 1,len(keyData64)):
   # print(ord(keyData64[k]),ord(dataTextTwo64[k]))
    #print(keyDataBinary[1:64],dataTextBinaryTwo)

    sum=ord(dataTextBinaryTwo[m])^ord(keyDataBinary[k])
    sumly= ord(dataTextBinary[j])^ord(keyDataBinary[k])
    binaryString=binaryString+str(sumly)
    binaryStringTwo=binaryStringTwo+str(sum)
    if m==len(dataTextBinaryTwo):
        m=1
    else:
        m=m+1
    if j==len(dataTextBinary):
        j=1
    else:
        j=j+1
    print(sumly,chr(sumly))
print(binaryString)
print(binaryStringTwo)
print(binascii.b2a_base64(sumly))

S = range(256)
j = 0
out = []
sum=0
i=1
j=0
#while(i<len(keyData64)){
 # sum=ord(keyData64[i])-ord(dataTextTwo64[j])
  # print(ord(sum))
  
   #if(j!=11){
    # j++
   #}
   #else{
    # j=0
   #}


#}

#KSA Phase
for i in range(256):
    j = (j + S[i] + ord( key[i % len(key)] )) % 256
    S[i] , S[j] = S[j] , S[i]

#PRGA Phase
i = j = 0
for char in data:
    i = ( i + 1 ) % 256
    j = ( j + S[i] ) % 256
    S[i] , S[j] = S[j] , S[i]
    out.append(chr(ord(char) ^ S[(S[i] + S[j]) % 256]))

print ''.join(out)
