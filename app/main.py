from fastapi import FastAPI

app = FastAPI(title="inventory-service")

@app.get("/health")
def health():
    return {"service": "inventory-service", "status": "ok"}