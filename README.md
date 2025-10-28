# Proyecto Colaborativo en Python

Este repositorio fue creado para practicar la colaboración en GitHub.
El proyecto está compuesto por tres módulos principales y un script principal.

## Estructura del proyecto

```
proyecto-colaborativo-python/
├── main.py
├── modulo_matematicas.py
├── modulo_cuento.py
├── modulo_utilidades.py
└── README.md
```

## Módulos

1. **modulo_matematicas.py**  
   Contiene funciones para operaciones básicas: `sumar`, `restar`, `multiplicar` y `dividir`.

2. **modulo_cuento.py**  
   Contiene la función `imprimir_cuento()` que imprime un cuento corto.

3. **modulo_utilidades.py**  
   Funciones auxiliares como `saludar(nombre)` y `despedir(nombre)`.

## Ejecutar el proyecto

1. Clonar el repositorio:
```bash
git clone https://github.com/<tu-usuario>/proyecto-colaborativo-python.git
cd proyecto-colaborativo-python
```

2. (Opcional) Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate    # Windows
```

3. Ejecutar:
```bash
python main.py
```

## Flujo de colaboración sugerido

1. Cada miembro crea una rama:
   ```bash
   git checkout -b nombre-rama
   ```

2. Hacer cambios, commitear y pushear:
   ```bash
   git add .
   git commit -m "Descripción del cambio"
   git push origin nombre-rama
   ```

3. Crear un Pull Request en GitHub y pedir revisión de otro miembro.

## Colaboradores

- Jose Chang
- María González
- Pedro Rivera

## Notas

- Cada integrante debe hacer al menos un Pull Request y revisar el código de otros miembros.
- Puedes editar el README.md para agregar instrucciones específicas de tu equipo.
