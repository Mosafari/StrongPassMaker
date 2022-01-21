import  random
from randomnamechanger import namechanger

a=['$','@','_','/']
b=[]
wpass=input('Enter a weak password to make it strong : ')
mode=input('choose the mode :(A strong pass without changing the letter order\n                  B strong pass with randomnamechanger \n                  C is combinition of A and B)\n mode : ')
#mode A without replace index
if mode=='A':
	b=list(wpass.strip())
	for i in range(len(b)-(len(b)//2)):
		b[int(random.														 choice(range(len(b))))]=a[int(random.						choice(range(len(a))))]
#mode B using randomnamechanger
elif mode=='B':	
	b=namechanger(wpass)
#mode C combinition of both
elif mode=='C':
	b=namechanger(wpass)
	b=list(b)
	for i in range(len(b)-(len(b)//2)):
		b[int(random.														 choice(range(len(b))))]=a[int(random.						choice(range(len(a))))]


Spass=''
Spass=Spass.join(b)
print('Strong Pass is Ready --> ',Spass)