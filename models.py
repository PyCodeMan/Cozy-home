import asyncio
import asyncpg
import config as cfg
import logging


data_for_connection = {
    'host': cfg.HOST,
    'port': cfg.PORT,
    'user': cfg.USER,
    'database': cfg.DATABASE,
    'password': cfg.PASSWORD
}


async def tables_initialisation():
    async with asyncpg.connect(*data_for_connection) as conn:
        try:
            async with conn.transaction():
                await conn.execute('''
                    CREATE TABLE IF NOT EXISTS Categories(
                    ID INT AUTO-INCREMENT PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL
                    )
                ''')
                await conn.execute('''
                    CREATE TABLE IF NOT EXISTS Goods(
                    ID INT AUTO-INCREMENT PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL,
                    Description TEXT,
                    Price DECIMAL(10,2) NOT NULL,
                    Image VARCHAR(255),
                    Category INT,
                    FOREIGN KEY (Category) REFERENCES Categories(ID)
                    )
                ''')
                await conn.execute('''
                    CREATE TABLE IF NOT EXISTS Characters(
                    ID INT AUTO-INCREMENT PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL
                    )
                ''')
                await conn.execute('''
                    CREATE TABLE IF NOT EXISTS Characters_values(
                    ID INT AUTO-INCREMENT PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL,
                    Character INT
                    FOREIGN KEY (Character) REFERENCES Characters(ID)
                    )
                ''')
                await conn.execute('''
                    CREATE TABLE IF NOT EXISTS Goods_characters(
                    Good INT,
                    Value INT,
                    Amount INT NOT NULL,
                    PRIMARY KEY (Good, Value)
                    FOREIGN KEY (Good) REFERENCES Goods(ID)
                    FOREIGN KEY (Value) REFERENCES Characters_values(ID)
                    )
                ''')
                await conn.execute('''
                    CREATE TABLE IF NOT EXISTS Groups(
                    ID INT AUTO-INCREMENT PRIMARY KEY,
                    Name VARCHAR(255) NOT NULL
                    )
                ''')
                await conn.execute('''
                    CREATE TABLE IF NOT EXISTS Groups_goods(
                    Group INT,
                    Value INT,
                    PRIMARY KEY (Group, Value),
                    FOREIGN KEY (Group) REFERENCES Groups(ID)
                    FOREIGN KEY (Value) REFERENCES Characters_values(ID)
                    )
                ''')
        except Exception:
            logging.exception('Transaction error')


async def filling_up_tables(tablename, values):
    async with asyncpg.connect(*data_for_connection) as conn:
        try:
            async with conn.transaction():
                columns = ', '.join(f'"{column}"' for column in values[0]._fields)
                placeholders = ', '.join(['$' + str(i + 1) for i in range(len(values[0]._fields))])
                sql = f"INSERT INTO {tablename} ({columns}) VALUES ({placeholders})"
                await conn.executemany(sql, values)
        except Exception:
            logging.exception('Transaction error')



async def get_information_from_table(tablename):
    async with asyncpg.connect(*data_for_connection) as conn:
        try:
            rows = asyncpg.fetch("SELECT * FROM TABLENAME=%s", tablename)
            async for data in conn.cursor(rows):
                pass # I should send this information anywhere...
        except Exception:
            logging.exception('Could not get requested information')


async def main():
    await tables_initialisation()


if __name__ == '__main__':
    logging.basicConfig(filename='my_database.log', level=logging.INFO)
    asyncio.get_event_loop().run_until_complete(main)