def lists()->list:
	""" tegi listid failist
	"""
	palgad=[]
	with open("denjgi.txt", "r") as f1: #avame fail
		for s in f1:
			palgad.append(s.strip()) # tegi listid
	inimesed=[]
	with open ("inimesed.txt", "r") as inimene:
		for q in inimene:
			inimesed.append(q.strip())
	return palgad,inimesed

def dobavka():
	""" lisamine inimese ja palk
	"""
	aken=Tk()
	N=1
	palgad=[]
	inimesed=[]
	for n in range(N):
		nimi=Entry(aken,text="Siseta nimi: ")
		inimesed.append(nimi)
		palk=Entryut(aken,text="Siseta palgad: ")
		palgad.append(palk)
	with open("inimesed.txt", "a") as inimesed: #lisame nimi  
		inimesed.write(nimi+"\n")	
	with open("denjgi.txt", "a") as palgad: #lisame palk 
		palgad.write(palk+"\n")	

def udalenie():
	"""delete_inimene()
	"""
	palgad,inimesed=lists()  
	nimi=input("Siseta nimi: ")
	if nimi not in inimesed: # kontrollime kui nimi on listis
		print("Kas sa tahad lisada nimi ja palgad?") 
		c=input("Y = jah, N = ei")
		if c.upper=="Y":
			add_person() # kasutame funktsioon kus me registreerime nimi ja palk
		else:
			pass
	else:
		a=inimesed.index(nimi) # otsing  indeks
		inimesed.pop(a) 
		palgad.pop(a) 
	f=open("inimesed.txt", "w")
	for g in inimesed:
		f.write(g+"\n")
	f.close()
	d=open("denjgi.txt", "w")
	for i in palgad:
		d.write(i+"\n")
	d.close()

def mnogozp():
	"""Arvutamine suurim palk
	"""
	palgad,inimesed=lists()
	suurim=max(palgad) # indeks muutuja edasiseks kasutamiseks
	b=palgad.index(suurim) 
	print("kõike suured palga on "+inimesed[b]+" palga")

def malozp():
	"""arvumine kõige smal palk
	"""
	palgad,inimesed=lists()
	palgadS=palgad.copy()
	palgadS.sort()
	a=palgadS[0]
	b=palgad.index(a)
	print("kõike väiksem palga on "+inimesed[b]+" palga ja see on "+ palgadS[0]+" euro")

def nalog():
	"""
	"""
	palgad,inimesed=lists()
	nimi=input("Siseta nimi keda palk te tahate arvutada: ")
	if nimi in inimesed: 
		a=inimesed.index(nimi)
		b=palgad[a]
		b=float(b)
		if b<=1200:
			h=b-500
			if h==0 or h<0:
				ans="käes palk on "+str(round(b,2))
			else:
				d=h*0.2
				e=b-d
				ans="käes palk on"+str(round(e,2))
		elif b>=1200:
			e=500-0.55556*(b-1200)
			d=b-e
			c=d*0.2
			f=b-c	
			ans="käes palk on"+str(round(f,2))
		else:
			e=b*0.2
			a=b-e
			ans="käes palk on"+str(round(a,2))
		print(ans)