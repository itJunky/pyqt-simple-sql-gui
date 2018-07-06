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

	query.exec_("create table subscribe(id int primary key, user_id int, name varchar(20))")
	query.exec_("insert into subscribe values(1, 1, 'gazetaru')")
	query.exec_("insert into subscribe values(2, 5, 'gazetaru')")
	query.exec_("insert into subscribe values(3, 101, 'gazetaru')")
	query.exec_("insert into subscribe values(4, 1, 'lxf')")

	return True