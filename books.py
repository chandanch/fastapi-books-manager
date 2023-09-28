from fastapi import FastAPI

app = FastAPI()


# first API
@app.get("/healthcheck")
async def health_check():
    return {"status": "OK", "message": "Service is up!"}
