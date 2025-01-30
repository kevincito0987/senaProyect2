# 🎯 Cálculo de Figuras y Procesamiento de Datos en JavaScript

## 📌 Introducción

Este proyecto desarrolla soluciones a varios problemas matemáticos y de procesamiento de datos utilizando **JavaScript**. Se incluyen programas para:

- Calcular áreas y perímetros de figuras planas.
- Analizar edades en un grupo de personas.
- Procesar datos numéricos.
- Gestionar información de artistas musicales.

## 📑 Tabla de Contenidos

- 📌 Introducción
- 💻 Instalación
- 🚀 Uso
- ⚙️ Funciones Principales
- 🔍 Ejemplos
- 📋 Requisitos
- 👥 Contribuidores
- 📜 Licencia

## 💻 Instalación

1. Clona este repositorio:

   ```
   bash
   
   
   CopiarEditar
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```

2. Navega al directorio del proyecto:

   ```
   bash
   
   
   CopiarEditar
   cd tu-repositorio
   ```

3. Abre el archivo principal en un navegador o ejecuta el código con Node.js.

## 🚀 Uso

### 1️⃣ Cálculo de Área y Perímetro de Figuras Planas

El programa permite calcular el **área** y **perímetro** de figuras como:

- 🔺 Triángulo
- 🟦 Rectángulo
- ⬛ Cuadrado
- ⚫ Círculo

### 2️⃣ Análisis de Edades

- Se almacenan las edades de 10 personas en un vector.
- Se determina la cantidad de menores, mayores y el adulto de mayor edad.
- Se validan edades en un rango de 1 a 120 años.

### 3️⃣ Procesamiento de Datos Numéricos

- Se ingresan 10 valores en un vector.
- Se calculan la media y los valores mayores/menores que la media.

### 4️⃣ Gestión de Artistas y Canciones

- Se registra información de artistas musicales (nombre, año de nacimiento, género, ciudad).
- Se almacenan hasta 3 canciones favoritas por artista.
- Se permite agregar y mostrar información específica de cada artista.

## ⚙️ Funciones Principales

- `calcularArea(figura, valores)`: Calcula el área de una figura dada.
- `calcularPerimetro(figura, valores)`: Calcula el perímetro de una figura dada.
- `procesarEdades(edades)`: Procesa y analiza la lista de edades ingresadas.
- `calcularMedia(datos)`: Calcula la media de un conjunto de valores.
- `gestionarArtistas(artistas)`: Maneja la información de artistas y sus canciones.

## 🔍 Ejemplos

Ejemplo de cálculo de área y perímetro de un rectángulo:

```
javascriptCopiarEditarconst base = 5;
const altura = 10;
console.log("Área:", calcularArea("rectangulo", [base, altura]));
console.log("Perímetro:", calcularPerimetro("rectangulo", [base, altura]));
```

Ejemplo de análisis de edades:

```
javascriptCopiarEditarconst edades = [23, 45, 17, 60, 10, 35, 80, 21, 18, 50];
procesarEdades(edades);
```

## 📋 Requisitos

- 🖥️ Node.js (Opcional para ejecutar en entorno local)
- 🌍 Navegador con soporte para JavaScript

## 👥 Contribuidores

- 🚀 [Tu Nombre](https://github.com/tu-usuario)

Si deseas contribuir, ¡haz un pull request! 🛠️

## 📜 Licencia

Este proyecto está bajo la licencia **MIT**. Puedes ver más detalles en el archivo `LICENSE`.