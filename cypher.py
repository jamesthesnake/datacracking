import base64
import binascii
#base 64 message
dataText64="bHRzbmV0Lm5ldC9jaGFsbGVuZ2U=bHRzbmV0Lm5ldC9jaGFsbGVuZ2U=bHRzbmV0Lm5ldC9jaGFsbGVuZ2U="
#secert key message in base 64
cypherData64 ="JwUTMy5NG3UfPnQrIQx3KyMIEicuAhY5DmEbeDZmHD82TRd+CE1jJT\
cKbUo0FGYyNmcCPR8SAXwgBBdb"
#theyellow string in base 64
dataTextTwo64="RmluZExUUw=="
 #the yellow stirng in binary
dataTextBinaryTwo="01000110011010010110111001100100010011000101010001010011"
#bsae 64 in binary
dataTextBinary="01101100011101000111001101101110011001010111010000101110 01101110011001010111010000101111011000110110100001100001011011000110110001100101011011100110011101100101"
#key in binary
keyDataBinaryOne= 001001110000010100010011001100110010111001001101000110110111010100011111001111100111010000101011001000010000110001110111001010110010001100001000000100100010011100101110000000100001011000111001000011100110000100011011011110000011011001100110000111000011111100110110010011010001011101111110000010000100110101100011001001010011011100001010011011010100101000110100000101000110011000110010001101100110011100000010001111010001111100010010000000010111110000100000000001000001011101011011
keyDataBinary=str(keyDataBinaryOne)
#secert message
keyDataHex="270513332e4d1b751f3e742b210c772b230812272e0216390e611b7836661c3f364d177e084d6325370a6d4a341466323667023d1f12017c2004175b"
#ascii  based on secert messge
asCypher= binascii.unhexlify(keyDataHex)
print(len(asCypher))
print(len(dataText64))
print(dataText64[26])
data = base64.b64decode(cypherData64)
key = dataText64
binaryString=""
binaryStringTwo=""
j=1
m=1
for k in range( 1,len(asCypher)-1):
   # print(ord(keyData64[k]),ord(dataTextTwo64[k]))
    #print(keyDataBinary[1:64],dataTextBinaryTwo)
 
#    sum=ord(dataTextBinaryTwo[m])^ord(keyDataBinary[k])
#    sumly= ord(cypherData64[j])^ord(asCypher[k])
     
    sumly= ord(dataText64[j])^ord(asCypher[k])
    print(chr(sumly))
    
    sumly= chr(sumly)
    binaryString=binaryString+str(sumly)+" "
 #   binaryStringTwo=binaryStringTwo+str(sum)
    if m==len(dataTextBinaryTwo):
        m=1
    else:
        m=m+1
    if j==len(dataText64)-1:
        j=1
    else:
        j=j+1
#    print(sumly,chr(sumly))
print(binaryString)
#print(binaryStringTwo)
print(sumly)
print(ord(cypherData64)^ord(asCypher))
#print(binascii.b2a_base64(sumly))
sumlyTwo= ord(dataTextBinary)^ord(keyDataBinary)
print(char(sumlyTwo))
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
