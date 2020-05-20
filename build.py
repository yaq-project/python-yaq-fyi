#!/usr/bin/env python3

from datetime import datetime
from dataclasses import dataclass
import pathlib

import jinja2
import markdown

__here__ = pathlib.Path(__file__).resolve().parent

env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(__here__ / "templates")))

(__here__ / "public").mkdir(exist_ok=True)

date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

extension_configs = {"toc": {"permalink": " ¶"}}
md = markdown.Markdown(
    extensions=["meta", "toc", "extra"], extension_configs=extension_configs
)


@dataclass
class Post:
    id: str
    title: str
    content: str


posts = []
for post in (__here__ / "posts").iterdir():
    with open(post, "r") as f:
        s = f.read()
        content = md.convert(s)
        kwargs = {
            "id": md.Meta["id"][0],
            "title": md.Meta["title"][0],
            "content": content,
        }
        posts.append(Post(**kwargs))

posts.sort(key=lambda y: y.title.lower())

p = __here__ / "public" / "index.html"
template = env.get_template("index.html")
with open(p, "w") as fh:
    fh.write(template.render(posts=posts, date=date))


template = env.get_template("post.html")
for post in posts:
    (__here__ / "public" / post.id).mkdir(exist_ok=True)

    with open(__here__ / "public" / post.id / "index.html", "w") as f:
        f.write(template.render(post=post, title=post.title, date=date))

# css ---------------------------------------------------------------------------------------------

template = env.get_template("style.css")
with open(__here__ / "public" / "style.css", "w") as fh:
    fh.write(template.render())
for d in (__here__ / "public").iterdir():
    if not d.is_dir():
        continue
    with open(d / "style.css", "w") as fh:
        fh.write(template.render())
