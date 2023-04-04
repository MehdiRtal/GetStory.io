from fastapi import FastAPI
import uvicorn
from fastapi.responses import ORJSONResponse
from fastapi.exceptions import HTTPException, RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from routers import instagram, accounts, proxies


app = FastAPI(title="GetStory.io", version="1.0.0", default_response_class=ORJSONResponse)

app.add_middleware(
    CORSMiddleware,
    allow_origins={"http://frontend:3000"},
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(HTTPException)
def http_exception_handler(request, exception: HTTPException):
    return ORJSONResponse({"status": "error", "message": exception.detail}, status_code=exception.status_code)

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exception: RequestValidationError):
    return ORJSONResponse({"status": "error", "message": exception.errors()}, status_code=422)

app.include_router(instagram.router)
app.include_router(accounts.router)
app.include_router(proxies.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, log_level="debug", reload=True)