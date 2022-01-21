import random 

def namechanger(name):
	ln=[]
	linx=[]
	liny=[]
	lengh = len(name)
	lname = list(name.strip())
	
	for i in range(lengh):
		linx.append(i)
		liny.append(i)

	for f in range(lengh):
		ln.append(' ')
	for i in range(lengh):	
		x = random.choice(linx)
		y = random.choice(liny)
		ln[x]=lname[y]
		linx.remove(x)
		liny.remove(y)
		
	cons = ''
	newname = cons.join(ln)
	return  newname
