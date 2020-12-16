from database_config import connection


def get_top_5(category):
    with connection.cursor() as cursor:
        query = f"Select user_id, score" \
            f"From Scores Where category={category}"
        cursor.execute(query)
        all_entries = cursor.fetchall()
        all_entries.sort(key=lambda x: x.get("score", 0),  reverse=True)
        top5 = []
        for entry in all_entries:
            name = entry.get("name")
            if name not in top5:
                top5.append(name)
                if len(top5) == 5:
                    break
        while len(top5) < 5:
            top5.append({})
        return top5

