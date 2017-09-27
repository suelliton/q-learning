
import numpy as np
from random import randint

gamma = 0.8
a = -1
j = 0
Q_max = -1

R =np.array([
	[-1,-1,-1,-1,0,-1],
	[-1,-1,-1,0,-1,100],
	[-1,-1,-1,0,-1,-1],
	[-1,0,0,-1,0,-1],
	[0,-1,-1,0,-1,100],
	[-1,0,-1,-1,0,100]	
	]).astype("float32")

Q = np.zeros_like(R)


for i in range(100):
	s = randint(0,len(Q[0])-1)	
	print "estado inicial : " + str(s)
	while s != 5:
		a = -1
		while a == -1:
			j = randint(0,len(Q[1])-1)
			a = R[s][j]
		a = j

		s_linha = a		
		print "while"
		print "estado : "+ str(s)
		print "acao : "+ str(a)
		print "recompensa : " + str(R[s,a])
		Q[s][a] = R[s][a]+gamma*max(Q[s_linha,:])
		s = s_linha
		print np.matrix(Q)


estado_inicial = int(input("digite um estado inicial de 0 a 5>>  "))

estado_atual = estado_inicial
print "estado de entrada:  "+ str(estado_atual)
while estado_atual != 5:
	a = max(Q[estado_atual][:])	
	for j in range(0,len(Q[1])):
		if a == Q[estado_atual,j]:
			b = j
			break;

	estado_atual = b
	print "estado/acao atual:  " + str(b)
	#print "estado proximo:  " + str(s)
print "estado final "+str(s)
		



	 				
			
		








