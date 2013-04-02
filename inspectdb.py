#!/usr/bin/env python
#
# See: http://docs.python.org/2/library/sqlite3.html
#

import sqlite3

desc_sql = "PRAGMA table_info('{0}');";
tables_sql = "select name from sqlite_master where type = 'table';"
tab_sql = "select * FROM '{0}';";

# Print entries
def print_entries(tab_name, entries):			
	for ent in entries:
		line = tab_name + ": "			
		for idx in range(1, len(ent)):
			line += str(ent[idx]) + " | "
		print(line)

# Describe table
def describe_table(c, tab_name):		
	cols = c.execute(desc_sql.format(tab_name))
	desc = "|"
	for col in cols:
		desc += str(col[0] + 1) + " " + str(col[1]) + "|" 
	print desc + "\n"

# Display table
def display_table(c, tab_name):
	print "\n- " + tab_name + " TABLE -"	
	describe_table(c, tab_name)
	print_entries(tab_name, c.execute(tab_sql.format(tab_name)))

# Main
if __name__ == "__main__":

	conn = sqlite3.connect('.svn/wc.db')
	c = conn.cursor()

	print "\n- TABLES -\n"
	tables = c.execute(tables_sql)
	for tab in tables:
		print "Table: " + tab[0]


	display_table(c, "REPOSITORY")
	display_table(c, "NODES")
	display_table(c, "PRISTINE")
	display_table(c, "WCROOT")
	display_table(c, "EXTERNALS")
	display_table(c, "LOCK")
	display_table(c, "WC_LOCK")
	display_table(c, "WORK_QUEUE")
	display_table(c, "ACTUAL_NODE")

	c.close()