import asyncio
import asyncpg
import config as cfg


data_for_connection = {
    'host': cfg.HOST,
    'port': cfg.PORT,
    'user': cfg.USER,
    'database': cfg.DATABASE,
    'password': cfg.PASSWORD
}


async def table_exists(name_of_table):
    async with asyncpg.connect(*data_for_connection) as conn:
        try:
            await conn.execute(f"SELECT 1 FROM {table_name} LIMIT 1")
            return True
        except Exception as exc:
            print(exc)
            return False


async def main():
    async with asyncpg.connect(*data_for_connection) as conn:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS goods(
                furniture_id SERIAL PRIMARY KEY
                sku VARCHAR(255)
                name VARCHAR(255)
                category VARCHAR(255)
                price DECIMAL(10,2)
                stock_quantity VARCHAR(255)
                image_url VARCHAR(255)
                manufacturer VARCHAR(255)
                material VARCHAR(255)
                color VARCHAR(255)
                style VARCHAR(255)
                dimensions TEXT
                created_at DATETIME
                updated_at DATETIME
            )
        ''')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main)