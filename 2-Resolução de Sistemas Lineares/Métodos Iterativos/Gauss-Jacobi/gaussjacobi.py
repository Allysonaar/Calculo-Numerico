def printar_matriz(matriz,linhas,colunas):								#Função para printar a matriz de maneira bonita
	
	i = 0
	while i < linhas:
		
		j = 0
		while j < colunas:
			
			print("{:8.3f}".format(matriz[i][j]), end = "")
			
			
			j +=1
		i += 1
		print()															#...

def gauss_jacobi(matriz,linhas,colunas,xn,erro,resultado):						#Função que resolve o sitema pelo metódo de Gauss Jacobi
	
	i=0
	while i < linhas:
		
		resultado[i] = matriz[i][colunas-1]/matriz[i][i]		#Colocando na posição xi do resultado o b/aii
		j = 0
		while j < colunas-1:
			
			if j != i:
				resultado[i] -= matriz[i][j]*xn[j]/matriz[i][i]		#Fazendo o xi somar com o restante da sua própria linha
			j += 1
		i += 1
	
	#Teste de erro
	i = 0							
	maior = 0
	while i < linhas:
	
		d = abs(resultado[i]-xn[i])
		if d > maior:
			maior = d
		
		i += 1
	
	d = maior/abs(max(resultado, key=abs))
	#Teste de erro
	
	print(resultado)
	
	if d < erro:
		return resultado
	else:
		return gauss_jacobi(matriz,linhas,colunas,resultado,erro,[0]*linhas)		#Recursividade para continuar o algoritmo


#Main	

#Entradas######################################################
#Primeira entrada#######
matriz1 = [[ 10,   2,  1,   7],			#Matriz de entrada
		  [  1,   5,  1,  -8],
		  [  2,   3, 10,   6]]

linhas1 = 3							#Linhas da matriz de entrada
colunas1 = 4							#Colunas da matriz de entrada

x01 = [0.7, -1.6, 0.6]			#x0 de entrada
xn1 = x01.copy()						#Cópia do x0
resultado1 = [0]*linhas1				#x final

erro1 = 0.05							#Erro de entrada
#Segunda Entrada#########
matriz2 = [[ 3,   1,    2],			#Matriz de entrada
		  [  2,   5,   -3]]

linhas2 = 2							#Linhas da matriz de entrada
colunas2 = 3							#Colunas da matriz de entrada

x02 = [0, 0]			#x0 de entrada
xn2 = x02.copy()						#Cópia do x0
resultado2 = [0]*linhas2				#x final

erro2 = 0.0000010							#Erro de entrada
#Entradas######################################################
final = gauss_jacobi(matriz2,linhas2,colunas2,xn2,erro2,resultado2)		#Lista com o resultado final

print(final)
