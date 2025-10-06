"""10º Escribe un programa que recoja un número y muestre un triángulo formado por
secuencias decrecientes de números impares. Por ejemplo, si se introduce el
5 se debe mostrar:"""

numero = int(input("Introduce un número: "))
mostrar = 1;

for i in range(numero):
    for j in range(i+1):
        if mostrar > 9:
            mostrar = 1;
        print(mostrar, end=" ")
        mostrar += 2
    print()

"""var numero = parseInt(prompt("Introduce un número entero: "));
var mostrar = 1;

if (isNaN(numero))
{
    document.writeln("ERROR: No es un número entero.");

} else 
{
    for (let i = 0; i < numero; i++)
    {
        for (let j = 0; j < i+1; j++)
        {
            if (mostrar > 9)
            {
                mostrar = 1;
            }

            document.writeln(mostrar + " ");
            mostrar += 2;
        }
        document.writeln("<br>");
    }
}"""