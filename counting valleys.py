
path='UDDDUDUU'

contador_valle=0
contador_U=0
contador_D=0

for i in path:
	if len(path)>0:
		if path[0]=='U':
		
			if i=='U':
				contador_U+=1
			elif i=='D':
				contador_D+=1

				if contador_U-contador_D==0:
					path=path[contador_U+contador_D:]
					
					contador_D=0
					contador_U=0

		elif path[0]=='D':
			if i=='D':
				contador_D+=1
			elif i=='U':
				contador_U+=1

				if contador_D-contador_U==0:
					path=path[contador_U+contador_D:]
					contador_valle+=1
					contador_D=0
					contador_U=0

print(contador_valle)




