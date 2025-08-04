# FastAPIGroup07042025

-  python -m venv venv 
- .\venv\Scripts\activate     
-  pip install "fastapi[all]"   
- pip freeze > requirements.txt 
- uvicorn main:app   
- uvicorn main:app --reload

gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
