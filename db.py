from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def createConnection(dbPath):
	db = QSqlDatabase.addDatabase('QSQLITE')

	if not dbPath:
		db.setDatabaseName(':memory:')

	if not db.open():
		return False

	query = QSqlQuery()
	query.exec_("create table user(id int primary key, name varchar(20), email varchar(128))")
	query.exec_("insert into user values(1, 'Ivan', 'i@i.ru')")
	query.exec_("insert into user values(2, 'Petr', 'p@i.ru')")
	query.exec_("insert into user values(5, 'Zoja', 'z@i.ru')")
	query.exec_("insert into user values(101, 'Sergey', 's@s.com')")

	return True