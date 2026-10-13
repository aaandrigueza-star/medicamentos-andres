from typing import List
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(
    title="API Medicamento - ADSO",
    description="API REST con operaciones CRUD para administrar medicamentos.",
    version="2.0.0",
)

# Modelo de Datos para Medicamento
class Medicamento(BaseModel):
    id: int
    nombre: str
    pricipio_activo: str
    precio: float
    requiere_formula: bool = True

# Modelo auxiliar para actualizaciones
class MedicamentoUpdate(BaseModel):
    nombre: str
    pricipio_activo: str
    precio: float
    requiere_formula: bool

# Base de datos simulada en memoria
db_medicamentos: List[Medicamento] = [
    Medicamento(
        id=1,
        nombre="Paracetamol",
        pricipio_activo="Acetaminofén",
        precio=5.50,
        requiere_formula=False,
    ),
    Medicamento(
        id=2,
        nombre="Amoxicilina",
        pricipio_activo="Amoxicilina trihidratada",
        precio=12.00,
        requiere_formula=True,
    ),
]

# 1. READ ALL (Obtener todos los medicamentos)
@app.get("/api/v1/medicamentos", response_model=List[Medicamento])
def obtener_todos_los_medicamentos():
    return db_medicamentos

# 2. READ ONE (Obtener un medicamento por ID)
@app.get("/api/v1/medicamentos/{medicamento_id}", response_model=Medicamento)
def obtener_medicamento_por_id(medicamento_id: int):
    for medicamento in db_medicamentos:
        if medicamento.id == medicamento_id:
            return medicamento

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"El medicamento con ID {medicamento_id} no existe en el inventario.",
    )

# 3. CREATE (Registrar un nuevo medicamento)
@app.post(
    "/api/v1/medicamentos",
    response_model=Medicamento,
    status_code=status.HTTP_201_CREATED,
)
def crear_nuevo_medicamento(medicamento: Medicamento):
    for medicamento_existente in db_medicamentos:
        if medicamento_existente.id == medicamento.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Ya existe un medicamento con el ID {medicamento.id}.",
            )

    db_medicamentos.append(medicamento)
    return medicamento

# 4. UPDATE (Actualizar un medicamento existente)
@app.put("/api/v1/medicamentos/{medicamento_id}", response_model=Medicamento)
def actualizar_medicamento(medicamento_id: int, datos_actualizados: MedicamentoUpdate):
    for index, medicamento in enumerate(db_medicamentos):
        if medicamento.id == medicamento_id:
            medicamento_modificado = Medicamento(
                id=medicamento_id,
                **datos_actualizados.dict(),
            )
            db_medicamentos[index] = medicamento_modificado
            return medicamento_modificado

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No se puede actualizar: el medicamento con ID {medicamento_id} no existe.",
    )

# 5. DELETE (Eliminar un medicamento)
@app.delete("/api/v1/medicamentos/{medicamento_id}")
def eliminar_medicamento(medicamento_id: int):
    for index, medicamento in enumerate(db_medicamentos):
        if medicamento.id == medicamento_id:
            db_medicamentos.pop(index)
            return {
                "mensaje": f"El medicamento con ID {medicamento_id} fue eliminado exitosamente."
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"No se puede eliminar: el medicamento con ID {medicamento_id} no existe.",
    )