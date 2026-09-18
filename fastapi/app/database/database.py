from typing import Generator


def get_db() -> Generator[None, None, None]:
    """
    Placeholder dependency for DB session.
    Actualmente no hay base de datos; se deja para futuras mejoras.
    """
    yield None
