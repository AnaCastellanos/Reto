
lista = [ ];
cadena = '';
#Leer Archivo
# book = xlrd.open_workbook("movies.xls");
# hoja = book.sheet_by_index(0);
# columnas = hoja.ncols;
# print columnas;

archivo = open("movies.txt");
linea=archivo.readline();
while linea != '':
		linea= archivo.readline()[:-1];
		lista.append(linea);

for i in range(len(lista)):
	lista[i] = lista[i].lower();
	if(i==0):
		cadena = lista[i];
	for c in range(i, len(lista)-1):
		lista[c] = lista[c].lower();
		h = len(lista[i])-1;
		if(c!=i):
			if(lista[i][h]==lista[c][0]):
				aux = lista[i+1];
				lista[i+1]=lista[c];
				lista[c]=aux;
				cadena = cadena + lista[i+1];
print cadena;
archivo.close();
