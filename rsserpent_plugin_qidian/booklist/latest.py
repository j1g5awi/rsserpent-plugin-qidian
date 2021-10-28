from typing import Any, Dict

from pyquery import PyQuery
from rsserpent.utils import HTTPClient


path = "/qidian/booklist/latest"


async def provider() -> Dict[str, Any]:
    url = "https://book.qidian.com/" + path.replace("/qidian", "")
    async with HTTPClient() as client:
        resp = await client.get(url)
    dom = PyQuery(resp.text)
    desc = ""
    items = dom("dd").items()

    return {
        "title": "最新书单_起点中文网",
        "link": url,
        "description": desc,
        "items": [
            {
                "title": item("h3 a[target=_blank]").text(),
                "description": item("p").text(),
                "author": item("a i").text()
            }
            for item in items
        ],
    }
