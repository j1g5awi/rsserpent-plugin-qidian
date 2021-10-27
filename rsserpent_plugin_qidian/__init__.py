from rsserpent.models import Persona, Plugin

from . import booklist


plugin = Plugin(
    name="rsserpent-plugin-qidian",
    author=Persona(
        name="Jigsaw",
        link="https://github.com/j1g5awi",
        email="j1g5aw@foxmail.com",
    ),
    prefix="/qidian",
    repository="https://github.com/Jigsaw/rsserpent-plugin-qidian",
    routers={booklist.detail.path:booklist.detail.provider},
)
