#!/usr/bin/env python3

import os
import pathlib
from jinja2 import Environment, FileSystemLoader
from datetime import datetime

__here__ = pathlib.Path(__file__).resolve().parent

env = Environment(loader = FileSystemLoader(str(__here__ / "templates")))

if not os.path.isdir(__here__ / "public"):
    os.mkdir(__here__ / "public")

date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# index -------------------------------------------------------------------------------------------

p = __here__ / "public" / "index.html"
template = env.get_template('index.html')
with open(p, 'w') as fh:
    fh.write(template.render(title="yaq", date=date))

# pages without arguments -------------------------------------------------------------------------

names = ["clients", "daemons"]

for name in names:

    if not os.path.isdir(__here__ / "public" / name):
        os.mkdir(__here__ / "public" / name)

    p = __here__ / "public" / name / "index.html"
    template = env.get_template(name + '.html')
    with open(p, 'w') as fh:
        fh.write(template.render(title=name, date=date))

# css ---------------------------------------------------------------------------------------------

for d, _, _ in os.walk(__here__ / "public", topdown=False):
    template = env.get_template('style.css')
    with open(os.path.join(d, "style.css"), 'w') as fh:
        fh.write(template.render())
