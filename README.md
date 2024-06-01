# todo-fastapi


CREATE USER 'todo_user'@'%' IDENTIFIED BY 'todo_pass';
GRANT ALL PRIVILEGES ON todo_db.* TO 'todo_user'@'%';
FLUSH PRIVILEGES;