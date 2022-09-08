users = [
    {
        'name': 'Hadiza',
     'age': 21,
     'gender': 'Female',
     'user_name': 'deezah',
     'is_verified': True,
     'tweets': [
         {'contents': 'PO for President', 'likes': 450, 'retweets': 233},
         {'contents': 'Atiku nis our man', 'likes': 4, 'retweets': 2},
                ]
     },
        {
        'name': 'Ibrahim',
     'age': 32,
     'gender': 'Male',
     'user_name': 'ibro',
     'is_verified': True,
     'tweets': [
         {'contents': 'Programming is fun', 'likes': 34, 'retweets': 12},
                ]
     },
        {
        'name': 'James',
     'age': 25,
     'gender': 'Male',
     'user_name': 'ames',
     'is_verified': True,
     'tweets': [
         {'contents': 'Love is life', 'likes': 450, 'retweets': 233},
         {'contents': 'Only Racheal I kmow', 'likes': 4, 'retweets': 2},
                ]
     },
        {
        'name': 'Racheal',
     'age': 21,
     'gender': 'Female',
     'user_name': 'betty',
     'is_verified': False,
     'tweets': [
         {'contents': '.', 'likes': 1450, 'retweets': 1330},
         {'contents': 'Thinking about ames', 'likes': 4, 'retweets': 2},
         {'contents': 'Amazing grace', 'likes': 2000, 'retweets': 10000},
                ]
     },
        {
        'name': 'Elijah',
     'age': 17,
     'gender': 'Male',
     'user_name': 'el_di_si',
     'is_verified': False,
     'tweets': [
         {'contents': '.', 'likes': 1450, 'retweets': 1330},
         {'contents': 'Thinking about ames', 'likes': 4, 'retweets': 2},
                ]
     },
        {
        'name': 'Dorris',
     'age': 16,
     'gender': 'Female',
     'user_name': 'anything',
     'is_verified': False,
     'tweets': [
         {'contents': 'I love Chimamanda', 'likes': 1450, 'retweets': 1330},
         {'contents': 'Feminism is the goal', 'likes': 45, 'retweets': 67},
                ]
     },
        {
        'name': 'Jacob',
     'age': 37,
     'gender': 'Male',
     'user_name': 'elder',
     'is_verified': True,
     'tweets': [
         {'contents': 'Reflection is my goal', 'likes': 50, 'retweets': 13},
         {'contents': 'How to get more likes on twitter', 'likes': 1, 'retweets': 5},
                ]
     },
        {
        'name': 'Derrick',
     'age': 29,
     'gender': 'Male',
     'user_name': 'standby_gen',
     'is_verified': False,
     'tweets': [
                ]
     },
{
        'name': 'Mubarak',
     'age': 47,
     'gender': 'Male',
     'user_name': 'whistle',
     'is_verified': True,
     'tweets': [
                ]
     },

]

no_of_users = len(users)
usernames = {user['user_name'] for user in users}
female_users = [user for user in users if user['gender']== 'Female']
inactive_users = [user for user in users if len(user['tweets'])== 0]
no_of_inactive_users = len([user for user in users if len(user['tweets'])== 0])
name_and_age = [{'name': user['name'], 'age': user['age']} for user in users]
avg_age_of_users = round(sum([user['age']for user in users]) / len(users))
# or avg_age_of_users = round(sum(user['age']for user in users) / len(users))
print(inactive_users)
print(female_users)
print(usernames)
print(no_of_inactive_users)
print(name_and_age)
print(avg_age_of_users)

]