import uvicorn
from fastapi import FastAPI
from crawler_n import Crawler

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8002, reload=True)


