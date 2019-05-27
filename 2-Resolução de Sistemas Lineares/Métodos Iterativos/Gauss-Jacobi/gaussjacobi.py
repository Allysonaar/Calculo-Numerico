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
	
	if d < erro:
		return resultado
	else:
		return gauss_jacobi(matriz,linhas,colunas,resultado,erro,resultado)		#Recursividade para continuar o algoritmo


#Main	

#Entradas######################################################
matriz = [[ 3,   1,  2],			#Matriz de entrada
		  [ 2,   5, -3]]

linhas = 2							#Linhas da matriz de entrada
colunas = 3							#Colunas da matriz de entrada

x0 = [0, 0, 0]				#x0 de entrada
xn = x0.copy()						#Cópia do x0
resultado = [0]*linhas				#x final

erro = 0.05							#Erro de entrada
#Entradas######################################################
final = gauss_jacobi(matriz,linhas,colunas,xn,erro,resultado)		#Lista com o resultado final

print(final)
