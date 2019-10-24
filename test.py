rows = 0
cols = 0
global_c = 0
suer_y = 0
teclado = []
palabra = []

pos_x, pos_y, netx_x, next_y = [0,0,0,0] 

#LEER EL ARCHIVO
fil=open("/Users/jonathan/Documents/notas.txt", "r")
if fil.mode == 'r':
    #obtener el contenido
    lines =fil.readlines()
    c = 1
    l = 0
    #recorrer los renglones
    for line in lines:

        #encontrar el primer renglón
        if c == 1:
            row_col = line.split(' ')
            print(row_col[0], ' - ' , row_col[1])
            rows = int(row_col[0])
            cols = int(row_col[1])
        
        #encontrar las letras del teclado
        if c > 1 and c <= (rows+1):
            letters = list(line)
            letters.pop()
            teclado.append(letters)

        if c == rows+2:
            palabra = list(line)
            
            palabra.append('*')


        c+=1

#PROCEDIMIENTO DE BÚSQUEDA
for x in palabra:
    print (x)
    for i in range(rows):
        for j in range(cols):
            if(x == teclado[i][j]):
                print(teclado[i][j],end = '')
                #CALCULO 
        print("")

#imprimir resultados 