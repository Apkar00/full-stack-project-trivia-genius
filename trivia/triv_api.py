import requests
import random

CORRECT_ANSWERS = {}
BASE_URL = 'https://opentdb.com/api.php?amount=10'

def get_token():

    url = 'https://opentdb.com/api_token.php?command=request'
    token = requests.get(url).json().get('token')
    if token is None:
        #TODO raise error
        pass
    return token

def get_fixed_data(token, data, url):
    code = data.get('response_code')
    if code == 0:
        return data
    if code == 1:
        #TODO raise error "You asked for more than what the api has"
        return
    if code == 2:
        #TODO raise error "Invalid Parameter"
        return
    if code == 3 or code == 4:
        token = get_token()
        url = url[:url.index("&token=")]+f"&token={token}"
        return requests.get(url).json()

def get_categories_dict():
    url = 'https://opentdb.com/api_category.php'
    data = requests.get(url).json()
    categories = data.get('trivia_categories')
    #TODO throw error incase categories is empty
    return {cat['name']: cat['id'] for cat in categories}

def get_categories(categories = get_categories_dict()):
    return list(categories.keys())


def get_category_url(category):
    if category is None:
        cat_url = ""
    else:
        cat_dict = get_categories_dict()
        cat_id = cat_dict.get(category, None)
        if cat_id is None:
            #TODO throw error because of wrong connection
            pass
        cat_url = f"&category={cat_id}"
    return cat_url

def get_difficulty_url(difficulty):
    if difficulty is None:
        diff_url = ""
    else:
        diff_url = f"&difficulty={difficulty}"
    return diff_url

def get_type_url(type):
    if type is None:
        type_url = ""
    elif type not in ("multiple", "boolean"):
        #TODO raise error because of wrong type
        pass
    else:
        type_url = f"&type={type}"
    return type_url

def get_question(id, token=get_token(), category=None, difficulty=None, type=None, category_dict = get_categories_dict()):
    #TODO A problem may appear from using get_token() as a default value
    cat_url = get_category_url(category)
    diff_url = get_difficulty_url(difficulty)
    type_url = get_type_url(type)
    token_url = f"&token={token}"
    url = BASE_URL + cat_url + diff_url + type_url + token_url
    data = requests.get(url).json()
    data = get_fixed_data(token, data, url)
    results = data.get("results")
    all_questions = []
    CORRECT_ANSWERS[id] = []
    for result in results:
        question_dict = {}
        question_dict['question'] = result.get("question")
        question_dict['answers'] = []
        question_dict['answers'].append(result.get('correct_answer'))
        question_dict['answers'] += (result.get("incorrect_answers"))
        random.shuffle(question_dict['answers'])
        CORRECT_ANSWERS[id].append(question_dict['answers'].index(result.get('correct_answer')))
        all_questions.append(question_dict)
    return all_questions

print(get_question(1))
print(len(get_question(1)))
print(get_question(2))
print(CORRECT_ANSWERS)
