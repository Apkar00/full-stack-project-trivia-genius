from database_config import connection


def get_name_by_id(user_id):
    with connection.cursor() as cursor:
        query = f"SELECT username" \
                f" FROM users" \
                f" WHERE id = {user_id}"
        cursor.execute(query)
        result = cursor.fetchone()
        return result.get('username')


def get_top_5_of_all_categories():
    categories = get_all_categories()
    return [{category: get_top_5(category)} for category in categories]



def get_all_categories():
    with connection.cursor() as cursor:
        query = f"SELECT DISTINCT category" \
                f" FROM scores"
        cursor.execute(query)
        result = cursor.fetchall()
        return [item.get('category') for item in result]


def get_top_5_same_user(user_id):
    with connection.cursor() as cursor:
        query = f"Select DISTINCT category" \
            f" From scores"
        cursor.execute(query)
        categories = cursor.fetchall()
        categories = [category.get('category') for category in categories]
        top5 = {}
        for category in categories:
            top5[category] = get_top_5(category, user_id)
        return top5




def get_top_5(category, user_id=None):
    with connection.cursor() as cursor:
        if user_id:
            query = f"Select category, score" \
                    f" From scores Where category='{category}'" \
                    f" AND user_id={user_id}"
        else:
            query = f"Select user_id, score" \
                f" From scores Where category='{category}'"
        cursor.execute(query)
        all_entries = cursor.fetchall()
        all_entries = list(all_entries)
        all_entries.sort(key=lambda x: x.get("score", 0),  reverse=True)
        top5 = []
        list_of_names = []
        for entry in all_entries:
            entry['score'] = str(entry['score'])
            name = entry.get("user_id")
            if user_id:
                name = get_name_by_id(user_id)
            else:
                name = get_name_by_id(name)
                entry['user_id'] = name
            #entry['user_id'] = name
            if name not in list_of_names:
                top5.append(entry)
                list_of_names.append(name)
                if len(top5) == 5:
                    break
        while len(top5) < 5:
            top5.append({})
        return top5

