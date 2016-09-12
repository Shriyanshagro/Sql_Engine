# Author = Shriyansh Agrawal

import re

SCHEMA_FILE = "metadata.txt"


class Database(object):
    def __init__(self,name,tables):
        # Database initialisation
        self.name = name
        self.tables = tables

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

    def load_contents(self):
        # load table records in database
        for i in range(len(self.tables)):
            name_table = self.tables[i]['name']
            name = name_table + '.csv'
            with open(name) as table:
                rows = table.readlines()

                rows = map(lambda x:x.strip(),rows)
                for j in range(len(rows)):
                    row = re.split(',',rows[j])
                    self.tables[i]['row'].append(row)

    def print_database(self):
        print '''
                *** Your Desireed Database ***
                    '''
        print 'Database name :',self.name
        for i in range(len(self.tables)):
            name_table = self.tables[i]['name']
            print '----------', name_table, '----------'
            for j in range(len(self.tables[i]['columns'])):
                print self.tables[i]['columns'][j],
            print

            for j in range(len(self.tables[i]['row'])):
                for k in range(len(self.tables[i]['row'][j])):
                    print self.tables[i]['row'][j][k],
                print

            print


    def get_table(self,tablename):
        # Returns the table whoose name is tablename.

        temp = filter(lambda x: x['name'] == tablename, self.tables)
        if temp == list():
            raise Exception("No such table")
        return temp[0]

    def delete_table(self, tablename):
        # Deletes a table from the database.
        self.tables = filter(lambda x: x['name'] != tablename, self.tables)
        print tablename, 'successfully deleted'
