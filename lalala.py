
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

# n=input("Cuantas peliculas deseas agregar: ");

# for i in range(n):
# 	print i;
# 	pelicula= raw_input("Ingresa una pelicula: \n");
# 	lista.append(pelicula);

# print("\nLas peliculas agregadas son:\n")
# for list in lista:
# 	print list;

# print len(lista);

#Primer comparacion
for i in range(len(lista)):
	lista[i] = lista[i].lower();	
	# print i;	
	# print lista[i];
	if(i==0):
		cadena = lista[i];
	for c in range(i, len(lista)-1):
		# print c;
		lista[c] = lista[c].lower();
 		# print lista[i];
		h = len(lista[i])-1;
		# print h;
# 		# print "Ultima letra: " + lista[i][h];
# 		# cadena = lista[i];
		if(c!=i):
			# print ("Son diferentes");
			# print lista[c];
			# print c;
			# print lista[i][h];
			# print lista[c][0];
			if(lista[i][h]==lista[c][0]):
# 				# print "Primera Letra: " + lista[c][0];
				aux = lista[i+1];
				lista[i+1]=lista[c];
				lista[c]=aux;
				# print "Lo hizo";
				# cadena = cadena + lista[c];
				# print lista;
				# print cadena;
				cadena = cadena + lista[i+1];
	# cadena = cadena + lala;		
print cadena;				
				# cadena = cadena + lista[] + lista[]

# for j in range(len(lista)-1):
# 	lista[j] = lista[j].lower();
# 	# print lista[j];
# 	if(j==0):
# 		h = len(lista[j])-1 #Ultima letra del arreglo
# 		# print "Ultima letra: " + lista[j][h];
# 		# print "Primera letra:" + lista[j][0];#Primera letra
# 		cadena = '';
# 	else:
# 		h = len(lista[j-1])-1;
# 		# print "Ultima letra pasada: " + lista[j-1][h];
# 		# print "Primera letra actual: " + lista[j][0];
# 		if(lista[j-1][h]==lista[j][0]):
# 			# print lista[j];
# 			# print lista[j-1];
# 			# print "Son iguales";
# 			cadena = cadena + lista[j-1]+lista[j];
			
			
# print cadena;
archivo.close();
