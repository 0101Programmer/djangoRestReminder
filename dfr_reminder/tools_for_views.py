from email_validator import validate_email, EmailNotValidError


def email_check(email):
    try:
        emailinfo = validate_email(email, check_deliverability=False)
        email = emailinfo.normalized
        return email
    except EmailNotValidError as e:
        print(str(e))
        return False
