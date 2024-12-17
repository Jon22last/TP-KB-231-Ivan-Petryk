class Student:
    def __init__(self, name, phone, email, group):
        self.name = name
        self.phone = phone
        self.email = email
        self.group = group

    def __str__(self):
        return f"{self.name} - {self.phone}, {self.email}, {self.group}"

    def to_dict(self):
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "group": self.group
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['phone'], data['email'], data['group'])
