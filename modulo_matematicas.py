class Calculadora:
    def __init__(self):
        # Lista para guardar las operaciones realizadas
        self.historial = []

    def _generar_historial(self, a, b, resultado, op):
        """Guarda una operación en el historial."""
        self.historial.append({
            "a": a,
            "b": b,
            "resultado": resultado,
            "op": op
        })

    def imprimir_historial(self):
        """Muestra el historial de operaciones."""
        if not self.historial:
            print("No hay historial disponible.")
        else:
            print("=== Historial de operaciones ===")
            for op in self.historial:
                print(f'{op["a"]} {op["op"]} {op["b"]} = {op["resultado"]}')
            print("================================")

    def borrar_historial(self):
        """Borra todo el historial."""
        self.historial.clear()
        print("Historial borrado con éxito.")

    # ---------- Operaciones ----------
    def sumar(self, a, b):
        resultado = a + b
        self._generar_historial(a, b, resultado, "+")
        return resultado

    def restar(self, a, b):
        resultado = a - b
        self._generar_historial(a, b, resultado, "-")
        return resultado

    def multiplicar(self, a, b):
        resultado = a * b
        self._generar_historial(a, b, resultado, "*")
        return resultado

    def dividir(self, a, b):
        if b == 0:
            print("Error: No se puede dividir entre cero.")
            return None
        resultado = a / b
        self._generar_historial(a, b, resultado, "/")
        return resultado
