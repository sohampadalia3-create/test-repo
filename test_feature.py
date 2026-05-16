def login(user, password):
    query = f'SELECT * FROM users WHERE name={user}'
    return db.execute(query)
