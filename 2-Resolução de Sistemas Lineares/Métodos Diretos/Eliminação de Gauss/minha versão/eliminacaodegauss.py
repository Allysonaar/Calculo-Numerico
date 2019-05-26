def printar_matriz(matriz,linhas,colunas):
	for i in range(linhas):
		for j in range(colunas):
			
			print("{: .3f}".format(matriz[i][j]), end = "   ")
		
		print()
		
		
def gauss(matriz, linhas, colunas):
	
	i = 0
	while i < linhas-1:
		
		j = i+1
		while j < linhas:
			multiplicador = matriz[j][i]/matriz[i][i]
			
			k = i
			while k < colunas:
				
				matriz[j][k] -= multiplicador*matriz[i][k]
				
				k += 1
			j += 1
		i += 1
	
def resolucao_sistema(matriz, linhas, colunas, solucao):
	
	i = linhas-1
	
	while i >= 0:
		
		j = i+1
		while j < colunas:
			
			if j == colunas-1:
				solucao[i] += matriz[i][j]/matriz[i][i]
			elif j<colunas-1:
				solucao[i] -= matriz[i][j]*solucao[j]/matriz[i][i]
			
			j += 1
		
		solucao[i] = round(solucao[i],3)
		
		i -= 1
	
matriz = [[3.0, 2.0, 4.0, 1.0],
		  [1.0, 1.0, 2.0, 2.0],
		  [4.0, 3.0, -2.0, 3.0]]

linhas = 3
colunas = 4
solucao = [0]*(colunas-1)

gauss(matriz, linhas, colunas)
printar_matriz(matriz,linhas,colunas)

resolucao_sistema(matriz, linhas, colunas, solucao)

print(solucao)
