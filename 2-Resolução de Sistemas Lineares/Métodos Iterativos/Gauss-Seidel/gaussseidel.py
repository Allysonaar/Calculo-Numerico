def printar_matriz(matriz,linhas,colunas):								#Função para printar a matriz de maneira bonita
	
	i = 0
	while i < linhas:
		
		j = 0
		while j < colunas:
			
			print("{:8.3f}".format(matriz[i][j]), end = "")
			
			
			j +=1
		i += 1
		print()															#...

def gauss_jacobi(matriz,linhas,colunas,xn,erro,xanterior):						#Função que resolve o sitema pelo metódo de Gauss Jacobi
	
	
	i=0
	while i < linhas:
		

		xn[i] = matriz[i][colunas-1]/matriz[i][i]		#Colocando na posição xi do resultado o b/aii
		j = 0
		while j < colunas-1:
			
			if j != i:
				xn[i] -= matriz[i][j]*xn[j]/matriz[i][i]		#Fazendo o xi somar com o restante da sua própria linha
			j += 1
		i += 1
	
	#print(xn)
	#print(xanterior)
	
	#Teste de erro
	i = 0							
	maior = 0
	while i < linhas:
	
		d = abs(xn[i]-xanterior[i])
		if d > maior:
			maior = d
		
		i += 1
	
	d = maior/abs(max(xn, key=abs))
	#Teste de erro
	
	
	print(xn)
	
	if d < erro:
		return xn
	else:
		return gauss_jacobi(matriz,linhas,colunas,xn,erro,xn.copy())		#Recursividade para continuar o algoritmo


#Main	

#Entradas######################################################
#Primeira entrada##########
matriz1 = [[ 3,   1,  2],			#Matriz de entrada
		  [ 2,   5, -3]]
		  

linhas1 = 2							#Linhas da matriz de entrada
colunas1 = 3							#Colunas da matriz de entrada

x01 = [0, 0]				#x0 de entrada
xn1 = x01.copy()						#Cópia do x0
xanterior1 = x01.copy()				#Cópia de um x para usar no erro

erro1 = 0.0000010							#Erro de entrada
#Segunda entrada##########
matriz2 = [[ 5,   3,  1,  1],			#Matriz de entrada
		   [ 5,   6,  1,  2],
		   [ 1,   6,  7,  3]]
		  

linhas2 = 3							#Linhas da matriz de entrada
colunas2 = 4							#Colunas da matriz de entrada

x02 = [0, 0, 0]				#x0 de entrada
xn2 = x02.copy()						#Cópia do x0
xanterior2 = x02.copy()				#Cópia de um x para usar no erro

erro2 = 0.05							#Erro de entrada
#Terceira entrada##########
matriz3 = [[ 5,   1,  1,  5],			#Matriz de entrada
		   [ 3,   4,  1,  6],
		   [ 3,   3,  6,  0]]
		  

linhas3 = 3							#Linhas da matriz de entrada
colunas3 = 4							#Colunas da matriz de entrada

x03 = [0, 0, 0]				#x0 de entrada
xn3 = x03.copy()						#Cópia do x0
xanterior3 = x03.copy()				#Cópia de um x para usar no erro

erro3 = 0.05							#Erro de entrada
#Entradas######################################################
final = gauss_jacobi(matriz1,linhas1,colunas1,xn1,erro1,xanterior1)		#Lista com o resultado final
print(final)
