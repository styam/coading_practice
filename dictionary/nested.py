import json


with open("data.json") as file:
    read_content = json.load(file)

# question_access = read_content['results']
#
#
# for question_data in question_access:
#     pass
#
# replies_access = question_data['replies']
#
# for replies_data in replies_access:
#     pass
#
# user_name = replies_data['user']['display_name']
#
# print(user_name)


def get_user_name():
    all_user_name = []
    question_access = read_content['results']
    for question_data in question_access:
        replies_access = question_data['replies']
        for replies_data in replies_access:
            user_name = replies_data['user']['display_name']
            all_user_name.append(user_name)
    with open("users.json", "w") as file:
        json.dump(all_user_name, file)
    return all_user_name


print(get_user_name())

