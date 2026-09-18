from fastapi import FastAPI

# Routers
from app.routers.users import router as users_router
from app.routers.books import router as books_router


app = FastAPI(
    title="API de Usuarios y Libros",
    description="API CRUD para gestionar usuarios y libros.",
    version="1.0.0",
)


app.include_router(users_router)
app.include_router(books_router)


@app.get("/")
def read_root():
    return {
        "message": "API funcionando correctamente",
        "entidades": ["usuarios", "libros"],
        "endpoints": ["/users", "/books"],
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
