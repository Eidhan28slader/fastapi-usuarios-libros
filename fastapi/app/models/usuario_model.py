from app.schemas.user import User


# Por ahora `usuario_model` simplemente expone el Pydantic `User`.
# Aquí podríamos añadir modelos ORM en el futuro.
Usuario = User
