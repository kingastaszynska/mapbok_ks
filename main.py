users: list =[
    {'name':'Kinga','posts':1,'city':'Warszawa'},
    {'name':'Dominik','posts':3,'city':'Poznań'},
    {'name':'Szymon z wąsem','posts':5,'city':'Inowrocław'},
    {'name':'Szymon','posts':7,'city':'Białograd'},
    {'name':'Patryk','posts':9,'city':'Łódź'},
]
print(f'Witaj {users[0]['name']}!')
for user in users [1:]:
    print(f'Twój znajomy {user['name']}, z miejscowości {user['city']} opublikował {user['posts']} postów.')

# for idx, _ in enumerate(users[1:]):
#     print(f'Twój znajomy {users[idx]}, opublikował {posts[idx]} postów')
