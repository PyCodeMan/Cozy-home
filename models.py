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


async def tables_initialisation():
    async with asyncpg.connect(*data_for_connection) as conn:
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


async def filling_up_tables(tablename, values):
    async with asyncpg.connect(*data_for_connection) as conn:
        await conn.execute('''
            INSERT INTO TABLENAME=%s VALUES=%s
        ''', (tablename, values)
        )


async def main():
    await tables_initialisation()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main)