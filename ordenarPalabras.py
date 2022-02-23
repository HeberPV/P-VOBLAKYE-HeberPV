try:
    archivoEntrada = open('input.in.txt')
    listaPalabras = archivoEntrada.read().splitlines()
    archivoEntrada.close()
    casos = int(listaPalabras[0])
    if casos > 0:
        listaPalabras = listaPalabras[1:]
        inicioCaso = 0
        finCaso = 0
        listaOutput = []
        for i in range(casos):
            letrasSimilares = 0
            letrasFinales = []
            try:
                finCaso+=int(listaPalabras[inicioCaso])+1
                inicioCaso+=1
                nuevasPalabras = sorted(listaPalabras[inicioCaso:finCaso])
                for p in nuevasPalabras:
                    letrasFinales.append(p[-1])
                
                for x in nuevasPalabras:
                    if x[0] in letrasFinales:
                        letrasSimilares += 1
                
                if letrasSimilares >= len(letrasFinales) - 1:
                    listaOutput.append('Es posible ordenar')
                else:
                    listaOutput.append('No es posible ordenar')
                if finCaso <= len(listaPalabras):
                    inicioCaso=finCaso
            except IndexError:
                listaOutput.append('Error en el numero de casos')
            except ValueError:
                if finCaso >= len(listaPalabras):
                    listaOutput.append('Error en el numero palabras, linea '+str(inicioCaso+1))
                else:
                    listaOutput.append('Error en el numero palabras, linea '+str(inicioCaso - 1))

        archivo = open("output.out.txt", "w")
        for o in listaOutput:
            archivo.write(o + '\n')
        archivo.close()
    else:
        archivo = open("output.out.txt", "w")
        archivo.write('Error en el numero de casos, debe ser mayor a 0')
        archivo.close()
except:
    archivo = open("output.out.txt", "w")
    archivo.write('No existe el archivo de entrada')
    archivo.close()
