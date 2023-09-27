from fastapi import FastAPI

app = FastAPI()


@app.get("/healthcheck")
def health_check():
    return {"status": "OK", "message": "Service is up!"}
