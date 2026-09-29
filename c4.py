nums = ['uno','dos','Tres','Cuatro','cinco','Seis','Siete','Ocho','Nueve','Diez']
colors = ['Rojo','Verde','Azul','Negro','Blanco','Rosa','Gris','cafe','Morado','Naranja']
#print (nums)
#colors.append ('Violeta')
#colors.extend (['violeta','purpura'])
#colors.insert(0,'neon')
#colors.clear()
#colors.append('neon')
#colors_1 = colors.copy()
#print (colors_1)
nums.reverse()
nueva_lista = []
for num in nums:
    indice = nums.index(num)
    color = colors[indice]

    nueva_lista.append([num,color])
print(nueva_lista)

    #output = f"[{num},{colors[nums.index(num)]}]"
    #print (output)

# Actividad ahora invierte la lista de nums para poder ver los elementos de la lista ['Diez','Rojo']
#Al final crear una nueva lista Ambos elementos e imprimir la nueva lista