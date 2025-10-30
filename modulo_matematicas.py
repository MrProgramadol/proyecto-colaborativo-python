class Calculadora:
    def __init__(self):
        self.historial = []
    
    def _generar_historia(self, a, b, resultado, op):
        self.historial.append({
            "a":a,
            "b":b,
            "resultado":resultado,
            "op":op
        })
        
    def imprimir_historial(self):
        if len(self.historial) == 0:
            print("No hay historial")
        else:
            for operacion in self.historial:
                print(f'{operacion["a"]}{operacion["op"]}{operacion["b"]}={operacion["resultado"]}')
        
    def _borrar_historial(self):
        self.historial.clear()
        
    def sumar(self, a, b):
        resultado = a + b
        self._generar_historia(a,b, resultado, "+")
        return resultado

    def restar(self, a, b):
        resultado = a - b
        self._generar_historia(a,b, resultado, "-")
        return resultado
    
    def multiplicar(self, a, b):
        resultado = a * b
        self._generar_historia(a,b, resultado, "*")
        return resultado

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Error: división entre cero")
        resultado = a / b
        self._generar_historia(a,b, resultado, "/")
        return resultado
