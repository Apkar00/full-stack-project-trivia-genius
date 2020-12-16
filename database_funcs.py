from table_creation import connection

def add_user(username,password):
    with connection.cursor() as cursor:
           try:
               query = f"INSERT INTO users (username, password) VALUES ('{username}','{password}')"
               cursor.execute(query)
               connection.commit()
           except pymysql.InternalError as e:
               print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
           except pymysql.IntegrityError as e:
               print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

def check_user (username,password):
    with connection.cursor() as cursor:
        query = f"SELECT username" \
                f" FROM users" \
                f" WHERE username = '{username}'"\
                f"AND password = '{password}'"
        cursor.execute(query)
        return cursor.fetchone() is not None

def check_user_name (username):
    with connection.cursor() as cursor:
        query = f"SELECT username" \
                f" FROM users" \
                f" WHERE username = '{username}'"
        cursor.execute(query)
        return cursor.fetchone() is not None


def results_to_array(dict_, id_):
    return [item.get(id_) for item in dict_]


def fetch_one(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchone()


def fetch_all(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def get_user_id(username):
    query = f"SELECT id " \
            f" FROM users" \
            f" WHERE username = '{username}'"
    result = fetch_one(query)
    if not result:
        return None
    return result.get('id')


def get_quiz_id(category):
    query = f"SELECT id " \
            f" FROM quizzes" \
            f" WHERE category = '{category}'"
    result = fetch_one(query)
    if not result:
        return None
    return result.get('id')


def get_score_id(user_id, quiz_id):
    query = f"SELECT id " \
            f" FROM scores" \
            f" WHERE user_id = {user_id}" \
            f" AND quiz_id = {quiz_id}"
    result = fetch_one(query)
    if not result:
        return None
    return result.get('id')


def get_all_users_id():
    query = "SELECT id " \
            " FROM users"
    result = fetch_all(query)
    return results_to_array(result, 'id')


def get_all_quizzes_id():
    query = "SELECT id " \
            " FROM quizzes"
    result = fetch_all(query)
    return results_to_array(result, 'id')


def test():
    user_id = get_user_id('username')
    quiz_id = get_quiz_id('category')
    score_id = get_score_id(user_id, quiz_id)
    print(user_id)
    print(quiz_id)
    print(score_id)
    print(get_all_users_id())
    print(get_all_quizzes_id())
