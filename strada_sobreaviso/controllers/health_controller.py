from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def health_check() -> dict:
    """Health Check possibilita verificar o conteúdo de requisições e respostas para checar se um determinado recurso HTTP está funcionando corretamente.
    Examples:
        >>> health_check()
        {'status': 'ok'}

    Returns:
        dict: Retorna o status_code 200 da api com response status ok
    """
    return {'status': 'ok'}
