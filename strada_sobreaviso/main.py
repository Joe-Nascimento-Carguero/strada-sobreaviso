from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from strada_sobreaviso.rotas import router

app = FastAPI()
app.include_router(router, prefix='')


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request, exc: RequestValidationError
):
    """Tratando mensagem de erro HTTP 400"""
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {
                'status': 'error',
                'status_code': 400,
                'message': 'O parâmetro informado não é um inteiro',
                'detail': RequestValidationError.errors,
                'method': 'GET',
                'resource': '/squads/{id}',
            }
        ),
    )
