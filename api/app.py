from fastapi import FastAPI
from fastapi.responses import HTMLResponse,FileResponse
from common.enum import Response

APP = FastAPI()

@APP.get(
    "/health",
    tags=["Static"],
    summary="Health check",
    description="Used for health check",
    
)
def get():
    return Response.OK.response

@APP.get(
        "/cat",
        tags=["cat"],
        summary="cat check",
        description="Used for cat check",
)
def get_html_file():
    with open("cat.html", "r") as file:
        html_content = file.read()
        return FileResponse("./src/image.jpg")