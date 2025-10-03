run:
	uvicorn src.fibonacci.__main__:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest