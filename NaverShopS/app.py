from fastapi import FastAPI
from crawler_n import Crawler

app = FastAPI()
crawler = Crawler()

@app.get("/searchN/")
async def search(keyword: str):
    results = crawler.naver_shop_search(keyword)
    return results