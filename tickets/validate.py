import re

def validate_email(email):
    email = email.strip()
    return re.search(r'^([a-zA-Z0-9-._]+@(?:\w+\.)?[a-zA-Z0-9-._]+'
                              r'\w+\.(?:edu|com|gm|uk|gov|net|org|us|ng))$',
                              email, flags=re.IGNORECASE.MULTILINE.DOTALL)


def validate_phone(phone):
    phone = phone.strip()
    return re.search(r'^((?:\+220|00220)? ?[235679]\d{2} ?\d{4})$', phone)


def validate_anydesk(anydesk):
    anydesk = anydesk.strip()
    return re.search(r'^(\d{3} ?\d{3} ?\d{3})$', anydesk)

def validate_name(name):
    name = name.strip()
    if len(name) > 30: return False
    return re.search(r'^([a-zA-Z ]+)$', name)
