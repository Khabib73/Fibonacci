import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Fibonacci", description="Fibonacci calculator", version="0.1.0")


@app.get("/get_fib/{n}")
def calculate_fib(n: int):
    "Return the n-th Fibonacci number."
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
