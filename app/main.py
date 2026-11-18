from fastapi import FastAPI

app = FastAPI(title="My Test App")

@app.get("/")
def root():
    return {"message": "Привет! Приложение работает new deploys yesss 🚀"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Привет, {name}!"}