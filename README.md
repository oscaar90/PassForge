# 🔐 PassForge

Generador local de contraseñas seguras, memorizables y personalizables.  
Diseñado para usarse desde el navegador o desde la terminal, sin depender de webs externas ni servicios cloud.

> 🧠 100 % local, sin telemetría, sin postureo. Tu herramienta, a tu gusto.

---

## 🚀 Características

- ✅ Generación de contraseñas aleatorias seguras (`secrets`)
- ✅ Contraseñas memorizables estilo Diceware
- ✅ Personalización completa:
  - Longitud
  - Uso de mayúsculas/minúsculas
  - Números y símbolos
- ✅ Interfaz web local con modo oscuro
- ✅ Copiar al portapapeles desde la web
- ✅ CLI (`--length`, `--symbols`, `--copy`, etc.)
- ✅ Sin dependencias externas ni conexión a Internet
- ✅ Código abierto y fácilmente extensible

---

## 🖼️ Capturas

> *(Aquí puedes poner 1 o 2 capturas cuando tengas la interfaz lista)*

---

## 🛠️ Tecnologías utilizadas

| Componente     | Descripción                        |
|----------------|------------------------------------|
| 🐍 Python       | Backend + CLI                      |
| ⚙️ Flask        | Servidor web local                 |
| 🎨 HTML/CSS     | Interfaz limpia y responsive       |
| 💡 JavaScript   | Copiado al portapapeles, interactividad |
| 🔐 secrets      | Generación segura de contraseñas   |
| 📋 pyperclip    | Copiado en CLI (opcional)          |

---

## 🧪 Cómo usar

### 1. Ejecutar en modo web

```bash
python app.py
```
Abre en tu navegador: http://localhost:5000

2. Usar desde la terminal (CLI)
```bash
python app.py --length 20 --symbols --copy
```
Parámetros disponibles:

--length: longitud de la contraseña

--symbols: incluir símbolos (!@#...)

--numbers: incluir números

--memorable: usar palabras aleatorias (modo diceware)

--copy: copiar directamente al portapapeles

🧩 Ejemplos
```bash
# Generar una contraseña de 16 caracteres con símbolos
python app.py --length 16 --symbols

# Generar contraseña memorizable tipo diceware
python app.py --memorable

# Generar y copiar al portapapeles
python app.py --length 20 --symbols --copy
```
📦 Instalación
Clona el repositorio:

```bash
git clone https://github.com/tuusuario/passforge.git
cd passforge
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

Lanza el modo web:

```bash
python app.py
```
🧠 Por qué lo hice
Porque todos los días necesito generar contraseñas y me cansé de usar páginas de terceros.
Esta herramienta me permite controlar todo el proceso, asegurarme de que es local, y adaptar la interfaz a mi gusto.

Además, me sirve como ejemplo práctico para enseñar Flask, CLI y diseño limpio.
Y ahora también puede ser tuya.

📄 Licencia
MIT. Úsala, modifícala, compártela.
Solo no seas un vendehumo que le cambia el logo y la sube como startup.

✍️ Autor
Hecha con Python y ganas de mejorar mi flujo diario por @sysoscar