import asyncio
import asyncpg


async def main():
    async with asyncpg.connect('postgresql://unit2147@localhost/test') as conn:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS goods(
                brand text,
                count integer,
                price numeric
            )
        ''')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main)