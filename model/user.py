class User:
    def __init__(self, id, first_name, last_name, contact, username, password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.contact = contact
        self.username = username
        self.password = password

    def __str__(self):
        return """User(id={}, first_name={}, last_name={}, contact={},username={}, password={})""" \
            .format(self.id, self.first_name, self.last_name, 
            self.contact, self.username, self.password)