import os
from aiohttp import web


TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')


def read_file(page_name):
  page_path = os.path.join(TEMPLATES_DIR, page_name)
  with open(f"{page_path}.html", "r") as f:
    return f.read()


def render_page(request, page_name):
  html = read_file(page_name)
  return web.Response(text=html, content_type="text/html")