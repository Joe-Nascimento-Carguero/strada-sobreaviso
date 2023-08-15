# syntax=docker/dockerfile:1
FROM python:3.11

EXPOSE 80

WORKDIR /app

COPY . .

RUN \
    --mount=type=cache,target=/var/cache/apk \
    pip3 install --upgrade pip && pip3 install poetry \
    && poetry install

# RUN pip3 install --upgrade pip && pip3 install poetry \
#     && poetry install

COPY . .

CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0","--port", "80", "strada_sobreaviso.main:app"]