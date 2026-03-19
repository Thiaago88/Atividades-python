from pathlib import Path
import shutil
#Exercicio 1
#criar pasta de arquivos importantes
# pasta_importantes = Path("Arquivos_importantes")
# pasta_importantes.mkdir(exist_ok=True)
   


# Path("arquivo.txt").touch(exist_ok=True)
# Path("arquivo.pdf").touch(exist_ok=True)
# Path("arquivo.xlsx").touch(exist_ok=True)


# shutil.move("arquivo.txt", pasta_importantes)
# shutil.move("arquivo.pdf", pasta_importantes)
# shutil.move("arquivo.xlsx", pasta_importantes)

# shutil.copytree(pasta_importantes, 'backup_arquivos')



#Execicio 2
# relatorio = Path("relatorio.txt")
# if not relatorio.exists():
#   relatorio.touch(exist_ok=True)


# if not relatorios_antigos.exists():

#  relatorios_antigos.mkdir(exist_ok=True)

# shutil.move(relatorio, relatorios_antigos/"backup_relatorio.txt")

# Exercicio 3



#shutil.make_archive("backup/backup_arquivos","zip", "Arquivos_importantes"  )


#Execicio 4

#shutil.unpack_archive("backup/backup_arquivos.zip", "extraido" )

for arquivo in Path("extraido").glob("*"):
    print(arquivo.stem)

for arquivo in Path("extraido").i)
 