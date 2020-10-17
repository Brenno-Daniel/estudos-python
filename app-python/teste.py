import shutil

texto = 'Primeira linha\nSegunda linha'

file = open('arquivo.txt', 'w')

file.write(texto)

file.close()

shutil.copy('arquivo.txt', 'backup.txt')

texto_split = texto.split('\n')