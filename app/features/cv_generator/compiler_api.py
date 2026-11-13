"""Private HTTP endpoint for the isolated CV compiler container."""

import shutil

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response

from app.features.cv_generator.compiler import MAX_TEX_BYTES, LocalCvCompiler
from app.features.cv_generator.schemas import CvGenerationError

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
compiler = LocalCvCompiler()


@app.get("/health")
async def health():
    if shutil.which("latexmk") is None:
        return JSONResponse({"status": "unavailable"}, status_code=503)
    return {"status": "ok"}


@app.post("/compile")
async def compile_cv(request: Request):
    body = bytearray()
    async for chunk in request.stream():
        body.extend(chunk)
        if len(body) > MAX_TEX_BYTES:
            return JSONResponse({"code": "INVALID_INPUT"}, status_code=413)
    try:
        tex = body.decode("utf-8")
        pdf = await compiler.compile(tex)
        return Response(pdf, media_type="application/pdf")
    except UnicodeDecodeError:
        return JSONResponse({"code": "INVALID_INPUT"}, status_code=400)
    except CvGenerationError as exc:
        status = 429 if exc.code == "BUSY" else 503 if exc.code == "COMPILER_UNAVAILABLE" else 422
        return JSONResponse({"code": exc.code}, status_code=status)
