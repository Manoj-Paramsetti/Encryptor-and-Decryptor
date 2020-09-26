import time
print('''                                 uuuuu
                                uu   uu
                                uu   uu
                                uu   uu
                              uuuuuuuuuuu
                              uuuuuuuuuuu
                              uuuuuuuuuuu
                              uuuuuuuuuuu

EEEEEEEEE  NNN    NN  CCCCCCCCC  RRRRRRR   YY     YY  PPPPPP   TTTTTTTTTT
EE         NNNN   NN  CC         RR    RR   YY   YY   PP   PP      TT
EE         NN NN  NN  CC         RR    RR    YY YY    PP   PP      TT
EEEEEEEEE  NN  NN NN  CC         RRRRRRRR     YYY     PPPPPP       TT
EE         NN   NNNN  CC         RR   RR       Y      PP           TT
EE         NN    NNN  CC         RR    RR      Y      PP           TT
EEEEEEEEE  NN     NN  CCCCCCCCC  RR    RR      Y      PP           TT''')

time.sleep(1)
print("\n\n                     ###CREATED BY MANOJ PARAMSETTI###")
Output=''
time.sleep(1)
A='3892'
B='5495'
C='3849'
D='8340'
E='8590'
D='9058'
F='8034'
G='4389'
H='1900'
I='3289'
J='4940'
K='3490'
l='9340'
m='1200'
n='4000'
o='4032'
p='1934'
q='2900'
r='9600'
s='9033'
t='4905'
u='4304'
v='4944'
w='2930'
x='2394'
y='8394'
z='3909'
space='1010'
one='1179'
two='7334'
three='2903'
four='4943'
five='4444'
six='8941'
seven='3303'
eight='5555'
nine='9022'
zero='3039'
dot='3933'
comma='3399'
exclam='3330'
quote='1001'
Dquote='3030'
colon='3902'
semicolon='3903'
Hash='3806'
divide='4689'
at='3802'
percent='5906'
power='1920'
And='2092'
asterick='9050'
sub='5690'
underscore='8934'
equal='3355'
add='3833'
quest='9999'

IN= input("Do you want to encrypt[Y/N]\n--> ")
print("\nOkay Fine! I think you came to decrypt\n")
IN=IN.lower()
if (IN in ("yes", "y", "ok", "okay", "yeah", "vrai")):
	print("INFO : Encrypter only support A-Z, 1-0 and symbol only with !@#%^&*_-+=/\":;.,'")
	Coder=input("Enter Text to encrypt: ")
	Coder=Coder.lower()
	for Code in Coder:
		if Code == "a":
			Output+=A
		if Code == "b":
			Output+=B
		if Code == "c":
			Output+=C
		if Code == "d":
			Output+=D
		if Code == "e":
			Output+=E
		if Code == "f":
			Output+=F
		if Code == "g":
			Output+=G
		if Code == "h":
			Output+=H
		if Code == "i":
			Output+=I
		if Code == "j":
			Output+=J
		if Code == "k":
			Output+=K
		if Code == "l":
			Output+=l
		if Code == "m":
			Output+=m
		if Code == "n":
			Output+=n
		if Code == "o":
			Output+=o
		if Code == "p":
			Output+=p
		if Code == "q":
			Output+=q
		if Code == "r":
			Output+=r
		if Code == "s":
			Output+=s
		if Code == "t":
			Output+=t
		if Code == "u":
			Output+=u
		if Code == "v":
			Output+=v
		if Code == "w":
			Output+=w
		if Code == "x":
			Output+=x
		if Code == "y":
			Output+=y
		if Code == "z":
			Output+=z
		if Code == " ":
			Output+=space
		if Code == "1":
			Output+=one
		if Code == "2":
			Output+=two
		if Code == "3":
			Output+=three
		if Code == "4":
			Output+=four
		if Code == "5":
			Output+=five
		if Code == "6":
			Output+=six
		if Code == "7":
			Output+=seven
		if Code == "8":
			Output+=eight
		if Code == "9":
			Output+=nine
		if Code == "0":
			Output+=zero
		if Code == ".":
			Output+=dot
		if Code ==",":
			Output+=comma
		if Code == "!":
			Output+=exclam
		if Code == "'":
			Output+=quote
		if Code == '"':
			Output+=Dquote
		if Code == ":":
			Output+=colon
		if Code == ";":
			Output+=semicolon
		if Code == "#":
			Output+=Hash
		if Code == "/":
			Output+=divide
		if Code == "@":
			Output+=at
		if Code == "%":
			Output+=percent
		if Code == "^":
			Output+=power
		if Code == "&":
			Output+=And
		if Code == "*":
			Output+=asterick
		if Code == "-":
			Output+=sub
		if Code == "_":
			Output+=underscore
		if Code == "=":
			Output+=equal
		if Code == "+":
			Output+=add
		if Code == "?":
			Output+=quest
else:
	print("Enter Text to decrypt: ")
	Code=input("")
	Code=Code.replace(' ','')
	len=len(Code)
	print("Number of Charcter after correction",len)
	length=len/4
	length=int(length)
	for i in range (0,length):
		temp=''
		i*=4
		temp+=Code[i]
		temp+=Code[i+1]
		temp+=Code[i+2]
		temp+=Code[i+3]
		if temp == '3892':
			Output+='A'
		if temp == '5495':
			Output+='B'
		if temp == '3849':
			Output+='C'
		if temp == '8340':
			Output+='D'
		if temp == '8590':
			Output+='E'
		if temp == '9058':
			Output+='D'
		if temp == '8034':
			Output+='F'
		if temp == '4389':
			Output+='G'
		if temp == '1900':
			Output+='H'
		if temp == '3289':
			Output+='I'
		if temp == '4940':
			Output+='J'
		if temp == '3490':
			Output+='K'
		if temp == '9340':
			Output+='l'
		if temp == '1200':
			Output+='m'
		if temp == '4000':
			Output+='n'
		if temp == '4032':
			Output+='o'
		if temp == '1934':
			Output+='p'
		if temp == '2900':
			Output+='q'
		if temp == '9600':
			Output+='r'
		if temp == '9033':
			Output+='s'
		if temp == '4905':
			Output+='t'
		if temp == '4304':
			Output+='u'
		if temp == '4944':
			Output+='v'
		if temp == '2930':
			Output+='w'
		if temp == '2394':
			Output+='x'
		if temp == '8394':
			Output+='y'
		if temp == '3909':
			Output+='z'
		if temp == '1010':
			Output+=' '
		if temp == '1179':
			Output+='1'
		if temp == '7334':
			Output+='2'
		if temp == '2903':
			Output+='3'
		if temp == '4943':
			Output+='4'
		if temp == '4444':
			Output+='5'
		if temp == '8941':
			Output+='6'
		if temp == '3303':
			Output+='7'
		if temp == '5555':
			Output+='8'
		if temp == '9022':
			Output+='9'
		if temp == '3039':
			Output+='0'
		if temp == '3933':
			Output+='.'
		if temp == '3399':
			Output+=','
		if temp == '3330':
			Output+='!'
		if temp == '1001':
			Output+="'"
		if temp == '3030':
			Output+='"'
		if temp == '3902':
			Output+=':'
		if temp == '3903':
			Output+=';'
		if temp == '3806':
			Output+='#'
		if temp == '4689':
			Output+='/'
		if temp == '3802':
			Output+='@'
		if temp == '5906':
			Output+='%'
		if temp == '1920':
			Output+='^'
		if temp == '2092':
			Output+='&'
		if temp == '9050':
			Output+='*'
		if temp == '5690':
			Output+='-'
		if temp == '8934':
			Output+='_'
		if temp == '3355':
			Output+='='
		if temp == '3833':
			Output+='+'
		if temp == '9999':
			Output+='?'
		temp=''


if Output == '':
	print("You made some mistake")
else:
	print(Output.upper())
