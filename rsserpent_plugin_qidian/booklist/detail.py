from typing import Any, Dict

from pyquery import PyQuery

from rsserpent.utils import HTTPClient

path = "/qidian/booklist/detail/{id}"


async def provider(id: int) -> Dict[str, Any]:
    url = "https://book.qidian.com/" + path.replace("/qidian", "").format(id=id)
    async with HTTPClient() as client:
        resp = await client.get(url)
    dom = PyQuery(resp.text)
    title = dom("b#j-bookListTitle").text()
    desc = dom("p#j-bookListIntro").text()
    dom("div.btn-wrap").remove()
    dom("div.text-wrap").remove()
    items = dom("dd[data-rid]").items()

    return {
        "title": title,
        "link": url,
        "description": desc,
        "items": [
            {
                "title": item("a.j-bookName").text(),
                "description": item.html().replace("//", "https://"),
            }
            for item in items
        ],
    }
