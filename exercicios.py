with open("tarefas.txt", r, encoding='utf'-8) as 
arquivo:
linhas = len(arquivo.readlines())
print(f"O arquivo possui {linhas} linhas")