from  modulo_matematicas import Calculadora
import modulo_cuento as mc
import modulo_utilidades as mu

def main():
    new_calculadora = Calculadora()
    print(mu.saludar("Jose"))
    
    print("Suma de 5 + 3 =", new_calculadora.sumar(5, 3))
    print("Resta de 10 - 4 =", new_calculadora.restar(10, 4))
    print("Multiplicación de 6 * 7 =", new_calculadora.multiplicar(6, 7))
    print("División de 10 / 2 =", new_calculadora.dividir(10, 2))
    print()
    mc.imprimir_cuento()
    print()
    print(mu.despedir("Jose"))

if __name__ == "__main__":
    main()
