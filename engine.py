# Author = Shriyansh Agrawal

import re

SCHEMA_FILE = "metadata.txt"


class Database(object):
    def __init__(self,name,tables):
        # Database initialisation
        self.name = name
        self.tables = tables
        print 'self :',self.name

    def __name__(self):
        # return database name
            return self.name

    def create_database(self):
        # create_database using metadata
        with open(SCHEMA_FILE) as schema:
            schema_lines = schema.readlines()

            schema_lines = map(lambda x:x.strip(),schema_lines)

            flag = -1
            exclude_strings = ['<begin_table>','<end_table>']
            columns = []
            table_name = ''

            for lines in schema_lines:
                if lines in exclude_strings:
                    flag *= -1
                    if table_name and columns:
                        # create table here, and insert into database
                        self.create_table(table_name,columns)
                        # print 'table_name = ', table_name
                        # print columns
                    columns = []
                    table_name = ''
                elif flag==1:
                    if not table_name:
                        table_name = lines
                    else:
                        columns.append(lines)

    def create_table(self,tablename,columns):
        # creates table into database
        # table = ['name','columns','row']
        Table = {'name':{},'columns':{},'row':{}}
        Table['name'] = tablename
        Table['columns'] = columns
        Table['row'] = []
        self.tables.append(Table)
        # print self.tables
