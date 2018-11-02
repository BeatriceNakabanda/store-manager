import psycopg2
from psycopg2.extras import RealDictCursor
from database.tables import tables_list

class Database:
    def __init__(self):
        self.db = "store_manager_beatrice"
        self.user = "postgres"
        self.host = "localhost"
        self.password = "admin"
        self.port = 5432

        # self.db = "deivon7io7dggi"
        # self.user = "bzczspnlfokryx"
        # self.host = "ec2-107-22-189-136.compute-1.amazonaws.com"
        # self.password = "a9731e743be4e474fba0cd5bee49ff57f136d35956c58c41f298a5e662e7e9ac"
        # self.port = 5432

        try:
            self.connection = psycopg2.connect(dbname=self.db,user=self.user,\
                                password=self.password, host=self.host,port=self.port)
            self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
            self.connection.autocommit = True
            # print("Connected successfully")
            for query in tables_list:
                self.cursor.execute(query)
        except Exception as error:
             print("Connection Failed {}".format(error))
    
    def delete_table(self, table_name):
        query = """
        DROP TABLE IF EXISTS {}
        """.format(table_name)
        return self.cursor.execute(query)
