import re

class Person:
    def __init__(self, id, name, age, emails):
        self.id = id
        self.name = name
        self.age = age
        self.emails = emails

class Email:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class PersonDAO:
    def save(self, person):
        pass

    def isValidToInclude(self, person):
        errors = []

        if len(person.name.split()) < 2 or not all(part.isalpha() for part in person.name.split()):
            errors.append("O nome deve conter pelo menos duas partes e ser composto por letras")

        if not (1 <= person.age <= 200):
            errors.append("A idade deve estar entre 1 e 200")

        if not person.emails:
            errors.append("A pessoa deve ter pelo menos um e-mail associado")
        else:
            email_regex = r'^[^@]+@[^@]+\.[^@]+$'
            for email in person.emails:
                if not re.match(email_regex, email.name):
                    errors.append("O e-mail deve estar no formato '____@____.___'")
        return errors
