from models.user import User

# Temporary credentials. 
users = []
u1 = User("hannah.sanders1@calhoun.edu", "Stella2022")
u2 = User("mason", "test")
users.append(u1)
users.append(u2)

def load_user(email, password):
    for user in users:
        if user.email == email and user.password == password:
            return user
        
