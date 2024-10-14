from aiohttp import web
from urls import routes
import logging


logger = logging.getLogger(__name__)


app = web.Application()
app.add_routes(routes)


if __name__ == '__main__':
    logging.basicConfig(filename='my_site.log', level=logging.INFO)
    logger.info('Started')
    web.run_app(app)
    logger.info('Finished')