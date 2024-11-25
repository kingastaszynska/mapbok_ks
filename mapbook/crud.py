
def hello(user:str)->None:
        print(f'Witaj {user}!')

def read_users(users:list)->None:
        for user in users[1:]:
            print(f'Twój znajomy {user['name']}, z miejscowości {user['city']} opublikował {user['posts']} postów.')
