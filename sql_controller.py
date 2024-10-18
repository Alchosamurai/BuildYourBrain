import sqlite3

# Подключение к базе данных
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# Чтение SQL-скрипта из файла
with open('words-russian-nouns.sql', 'r', encoding='utf-8') as file:
    sql_script = file.read()

cursor.execute("""CREATE TABLE IF NOT EXISTS `nouns` (
  `IID` int(11) NOT NULL AUTOINCREMENT,
  `word` varchar(60) NOT NULL,
  `code` int(11) NOT NULL,
  `code_parent` int(11) NOT NULL,
  `gender` enum('муж','жен','ср','общ') DEFAULT NULL,
  `wcase` enum('им') DEFAULT NULL,
  `soul` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`IID`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8 AUTOINCREMENT=4159395 ;""")
# Разделение скрипта на команды
# commands = sql_script.split(';')

# # Выполнение каждой команды отдельно
# for command in commands:
#     command = command.strip()
#     if command:  # Игнорировать пустые строки
#         try:
#             cursor.execute(command)
#         except sqlite3.Error as e:
#             print(f"Ошибка при выполнении команды: {command}\n{e}")

# Закрытие подключения
connection.commit()
connection.close()