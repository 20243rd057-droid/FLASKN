ident = "Emiliano |4 B | Azul "

def encontrar_color(ident):
    partes = ident.split('|')      
    color = partes[-1].strip()     
    return color

resultado = encontrar_color(ident)
print(resultado)