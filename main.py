import modulo_matematicas as mm
import modulo_cuento as mc
import modulo_utilidades as mu

def main():
    print(mu.saludar("Jose"))
    print("Suma de 5 + 3 =", mm.sumar(5, 3))
    print("Resta de 10 - 4 =", mm.restar(10, 4))
    print("Multiplicación de 6 * 7 =", mm.multiplicar(6, 7))
    print("División de 10 / 2 =", mm.dividir(10, 2))
    print()
    mc.imprimir_cuento()
    print()
    print(mu.despedir("Jose"))

if __name__ == "__main__":
    main()
