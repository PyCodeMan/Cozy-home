import asyncio
from aiohttp import web
from utils import render_page


routes = web.RouteTableDef()

@routes.get('/')
async def main_page(request):
  return await render_page(request, "main_page")

@routes.get('/about')
async def about_page(request):
  return await render_page(request, "about")

@routes.get('/catalog')
async def catalog_page(request):
  return await render_page(request, "catalog")

@routes.get('/actions')
async def actions_page(request):
  return await render_page(request, "actions")

@routes.get('/contacts')
async def contacts_page(request):
  return await render_page(request, "contacts")