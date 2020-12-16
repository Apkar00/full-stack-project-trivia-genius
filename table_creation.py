from database_config import connection


def execute_query(table):
    with connection.cursor() as cursor:
        query = f"CREATE TABLE IF NOT EXISTS {table}"
        cursor.execute(query)
        connection.commit()


def create_users_table():
    table = "users (" \
            "       id INT AUTO_INCREMENT PRIMARY KEY," \
            "       username VARCHAR(32) UNIQUE," \
            "       password VARCHAR(32)" \
            "       )"
    execute_query(table)


def create_quizzes_table():
    table = "quizzes (" \
            "           id INT AUTO_INCREMENT PRIMARY KEY," \
            "           category VARCHAR(32) UNIQUE" \
            "           )"
    execute_query(table)


def create_scores_table():
    table = "scores (" \
            "       id INT AUTO_INCREMENT PRIMARY KEY," \
            "       user_id INT," \
            "       category VARCHAR(32)," \
            "       score INT," \
            "       FOREIGN KEY(user_id) REFERENCES users(id)" \
            "       )"
    execute_query(table)


def create_tables():
    create_users_table()
    create_quizzes_table()
    create_scores_table()


if __name__ == '__main__':
    create_tables()
