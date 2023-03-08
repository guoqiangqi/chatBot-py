import uuid

class User:
    def __init__(self, id, username, access):
        self.id = id
        self.name = username
        self.access = access

    def __str__(self):
        return f"User(id='{self.id}')"

userList = [User(uuid.uuid1(), "temporaryUser", ['request'])]

def createUser(username, access):
    users.append(User(uuid.uuid1(), username, access))

def indexUserWithUUID(userUUID):
    userMatch = [ user for user in userList if user.id == userUUID]
    if len(userMatch) == 0:
        print("Fail: user not found with uuid {}!".format(userUUID))
        return None
    return userMatch

def indexUserWithName(userName):
    userMatch = [ user for user in userList if user.name == userName]
    if len(userMatch) == 0:
        print("Fail: user not found with name {}!".format(userName))
        return None
    return userMatch