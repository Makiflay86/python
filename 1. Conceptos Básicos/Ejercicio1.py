# 1 Escriba un programa que recoja un valor 
# por teclado y muestre de qué tipo es.

valor = input("Introduce un valor: ")

try:
    valor_convertido = int(valor)
    tipo = type(valor_convertido)
except ValueError:
    try:
        valor_convertido = float(valor)
        tipo = type(valor_convertido)
    except ValueError:
        if valor.lower() in ['true', 'false']:
            valor_convertido = valor.lower() == 'true'
            tipo = type(valor_convertido)
        else:
            valor_convertido = valor
            tipo = type(valor_convertido)

print(f"El valor '{valor}' es de tipo: {tipo}")
