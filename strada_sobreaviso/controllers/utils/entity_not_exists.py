from fastapi import HTTPException, status

from functools import wraps


def entity_not_exists(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPException:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Item não encontrado',
            )

    return inner
