from src.person_dao import Person, Email, PersonDAO
import pytest

@pytest.fixture
def person_dao():
    return PersonDAO()

def test_valid_person(person_dao):
    emails = [Email(1, "teste@example.com")]
    person = Person(1, "João Silva", 25, emails)
    errors = person_dao.isValidToInclude(person)
    assert len(errors) == 0

def test_invalid_name(person_dao):
    emails = [Email(1, "teste@example.com")]
    person = Person(1, "João", 25, emails)  # Nome com apenas uma parte
    errors = person_dao.isValidToInclude(person)
    assert "O nome deve conter pelo menos duas partes e ser composto por letras" in errors

def test_invalid_age(person_dao):
    emails = [Email(1, "teste@example.com")]
    person = Person(1, "João Silva", 250, emails)  # Idade fora do intervalo
    errors = person_dao.isValidToInclude(person)
    assert "A idade deve estar entre 1 e 200" in errors

def test_no_emails(person_dao):
    person = Person(1, "João Silva", 25, [])  # Nenhum email associado
    errors = person_dao.isValidToInclude(person)
    assert "A pessoa deve ter pelo menos um e-mail associado" in errors

def test_invalid_email_format(person_dao):
    emails = [Email(1, "emailinvalido.com")]  # Email inválido
    person = Person(1, "João Silva", 25, emails)
    errors = person_dao.isValidToInclude(person)
    assert "O e-mail deve estar no formato '____@____.___'" in errors
