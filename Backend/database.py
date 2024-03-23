import os
import pymysql
from dotenv import load_dotenv
from sql_utils import run_sql_file


class Database:

    NUM_OF_DEVS = 4
    def __init__(self):
        """
            Chargez les variables d'environnement de votre fichier .env, puis complétez les lignes 15 à 19 afin de récupérer les valeurs de ces variables
        """
        load_dotenv("environment.env")
        self.host = os.environ.get("HOST")
        self.port = int( os.environ.get("PORT") )
        self.database = os.environ.get("DATABASE")
        self.user = os.environ.get("USER")
        self.password = os.environ.get("PASSWORD")



        self._open_sql_connection()

        self.migration_counter = 0

    def _open_sql_connection(self):
        self.connection = pymysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            db=self.database,
            autocommit=True
        )

        self.cursor = self.connection.cursor()

    def push_migration(self):
        migration_to_push = self.migration_counter
        migration_files = f"db_scripts/migrations"
        name = os.listdir(migration_files)[migration_to_push % Database.NUM_OF_DEVS]
        migration_file = "db_scripts/migrations/" + name + f"/migrate/migrate_{name}_{(migration_to_push//Database.NUM_OF_DEVS)+1}.sql"
        print(f"migration: {name} {(migration_to_push//Database.NUM_OF_DEVS)+1}")
        run_sql_file(self.cursor, migration_file , accept_empty=False)
        self.migration_counter += 1
        print(f"migration: {name} {(migration_to_push // Database.NUM_OF_DEVS) + 1} is done")

    def rollback(self):
        if self.migration_counter < 1:
            raise ValueError("There are no rollbacks in the rollback stack.")
        rollback_to_push = self.migration_counter - 1
        migration_files = f"db_scripts/migrations"
        name = os.listdir(migration_files)[(rollback_to_push) % Database.NUM_OF_DEVS]
        rollback_file = "db_scripts/migrations/" + name + f"/rollback/rollback_{name}_{(rollback_to_push // Database.NUM_OF_DEVS)+1}.sql"
        print(f"rollback: {name} {(rollback_to_push // Database.NUM_OF_DEVS)+1}")
        run_sql_file(self.cursor, rollback_file, accept_empty=False)
        self.migration_counter -= 1
        print(f"rollback: {name} {(self.migration_counter  // Database.NUM_OF_DEVS) + 1} is done")


    def up(self):
        self.drop()
        run_sql_file(self.cursor, "db_scripts/up.sql")

    def drop(self):
        run_sql_file(self.cursor, "db_scripts/drop.sql")
        self.migration_counter = 0

    def get_table_names(self):
        req = f"SELECT table_name FROM INFORMATION_SCHEMA.TABLES WHERE table_type = 'BASE TABLE' AND table_schema = '{self.database}';"
        self.cursor.execute(req)

        res = [x[0] for x in self.cursor.fetchall()]

        return res

    def get_table_column_names(self, table):
        req = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table}' AND TABLE_SCHEMA = '{self.database}' ORDER BY ORDINAL_POSITION;"
        self.cursor.execute(req)

        res = [x[0] for x in self.cursor.fetchall()]

        return res

    def get_table_data(self, table):
        req = f"SELECT * FROM {table};"
        self.cursor.execute(req)

        return [list(x) for x in self.cursor.fetchall()]

    def get_table_primary_key(self, table):
        req = f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_SCHEMA = '{self.database}' AND TABLE_NAME = '{table}' AND CONSTRAINT_NAME = 'PRIMARY';"
        self.cursor.execute(req)

        return self.cursor.fetchone()

    def get_table_foreign_keys(self, table):
        req = f"SELECT COLUMN_NAME,REFERENCED_TABLE_NAME,REFERENCED_COLUMN_NAME FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE WHERE TABLE_SCHEMA = '{self.database}' AND TABLE_NAME = '{table}' AND CONSTRAINT_NAME != 'PRIMARY';"
        self.cursor.execute(req)

        foreign_keys = []
        for foreign_key in self.cursor.fetchall():
            foreign_keys.append({
                "column_name": foreign_key[0],
                "referenced_table_name": foreign_key[1],
                "referenced_column_name": foreign_key[2]
            })

        return foreign_keys

    def get_cursor(self):
        return self.cursor

    def get_connection(self):
        return self.connection

    def get_migration_stack_size(self):
        return self.migration_counter
