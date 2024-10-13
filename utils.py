import os
from aiohttp import web


def read_file(page_name):
    page_path = find_page_name(page_name)
    with open(f"{page_path}", "r") as f:
        return f.read()


def render_page(request, page_name):
    html = read_file(page_name)
    return web.Response(text=html, content_type="text/html")


def find_path_page_name(filename, startdir):
    if filename in os.listdir(startdir):
        page_name_path = os.path.join(startdir, filename)
        return page_name_path
    for root, dirs, files in os.walk(startdir):
        if filename in files:
            page_name_path = os.path.join(root, filename)
            return page_name_path


def find_page_name(page_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    page_path = find_path_page_name(page_name, current_dir)
    return page_path