class User:
    def __init__(self, id, email, name, created_at):
        self.id = id
        self.name = name
        self.email = email
        self.created_at = created_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at':self.created_at
        }

# CREATE TABLE users(
#   id INT PRIMARY KEY NOT NULL,
#   name TEXT NOT NULL, 
#   email TEXT NOT NULL,
#   created_at datetime default current_created_at
# );
