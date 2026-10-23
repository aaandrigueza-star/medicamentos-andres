# API CRUD de Medicamentos

API REST desarrollada con FastAPI para consultar, registrar, actualizar y eliminar medicamentos. Los datos se guardan en memoria; al reiniciar el servidor, vuelve la información inicial.

## Requisitos

- Python 3.10 o superior
- PowerShell en Windows

## Instalación

Desde esta carpeta, crea y activa el entorno virtual:

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

Si PowerShell bloquea la activación, permite scripts solo en la terminal actual y vuelve a activarlo:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\Activate.ps1
```

Instala las dependencias:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Ejecutar

```powershell
uvicorn main:app --reload
```

La documentación interactiva está disponible en <http://127.0.0.1:8000/docs>.

## Rutas

| Método | Ruta | Acción |
| --- | --- | --- |
| GET | `/api/v1/medicamentos` | Listar medicamentos |
| GET | `/api/v1/medicamentos/{medicamento_id}` | Consultar un medicamento |
| POST | `/api/v1/medicamentos` | Crear un medicamento |
| PUT | `/api/v1/medicamentos/{medicamento_id}` | Actualizar un medicamento |
| DELETE | `/api/v1/medicamentos/{medicamento_id}` | Eliminar un medicamento |

Ejemplo de cuerpo para crear un medicamento:

```json
{
  "id": 3,
  "nombre": "Ibuprofeno",
  "pricipio_activo": "Ibuprofeno",
  "precio": 8.5,
  "requiere_formula": false
}
```