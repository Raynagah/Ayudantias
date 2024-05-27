"""
Matriz: es una estructura de datos que puede tener multiples dimensiones.
"""
"""
#Matriz unidimensional. pueden ser verticales y horizontales

matriz_1d=[1,2,3,4,5,67,8,9,100];
          #0,1,2,3,4,5,,6,7,8,9
elemento_especifico=matriz_1d[8];
print(elemento_especifico);

#modificar un elemento específico
matriz_1d[8]=10;
print(matriz_1d);

#agregar un nuevo elemento .append()

matriz_1d.append(20);
print(matriz_1d);

#eliminar o remover un elemento
matriz_1d.remove(20);
print(matriz_1d);

#ordenar una matriz de menor a mayor
matriz_1d.sort();
print(matriz_1d);

#ordenar una matriz de mayor a menor
matriz_1d.sort(reverse=True);
print(matriz_1d);


Matrices bidimensionales
    Es una lista de listas. Filas[] horizontales y columnas[] verticales.


matriz_2d=[
    [1,2,3,4],#0
    [5,6,7,8] #1
    #0,1,2,3 
];

#obtener un elemento específico dentro de la matriz

elemento_especifico_2d=matriz_2d[1][1];
print(elemento_especifico_2d);

#modificar un elemento

matriz_2d[1][3]=9;
print(matriz_2d);

#recorrer una matriz 2d
for fila in matriz_2d:
    for columna in fila:
        print(columna);

#matriz multidimensional

matriz_3d=[
    [#0
        [1,2,3,4,5,6,7,8,9,10],#0
        [11,12,13,14,15,16,17,18,19,20]#1
        #0,1,2,3,4,5,6,7,8,9,10
    ],
    [#1
        [21,22,23,24,25,26,27,28,29,30],#0
        [31,32,33,34,35,36,37,38,39,40]#1
        #0,1,2,3,4,5,6,7,8,9,10
    ]
]
#---piensa que son coordenadas de algún juego e.e
elemento_3d=matriz_3d[1][1][8];
print(elemento_3d);
#modificar
matriz_3d[1][1][8]=390;
print(matriz_3d);
"""

#ejercicios en clase

matriz_1=[1,2,3,4,5,6,7,8,9,10];
matriz_1[3]=15;
matriz_1.remove(1);
matriz_1.sort();
print(matriz_1);

matriz_2=[
    [1,2,3],#0
    [4,5,6],#1
    [7,8,9]#2
    #0,1,2
]
matriz_2[1][2]=20;
print(matriz_2);
for fila in matriz_2:
    for columna in fila:
        print(columna*2);


#el ejercicio pide crear una matriz tridimensional con 2 matrices bidimensionales de 2x3, 
#me faltó hacer esa parte :(
matriz_3=[
    [#0
        [1,2],#0
        [3,4],#1
        [5,6]#2
        #0,1
    ],
    [#1
        [1,2],#0
        [3,4],#1
        [5,6]#2
        #0,1
    ]
]
matriz_3[1][0][1]=50;
print(matriz_3);
for fila in matriz_3:
    for columna in fila:
        for gachapon in columna:
            print(gachapon+10);






