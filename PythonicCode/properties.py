"""Properties are the equivalent of getters and setters in other languages"""

import re
EMAIL_FORMAT = re.compile(r"[^@]+@[^@]+\.[^@]+")


def is_valid_email(potentially_valid_email: str):
    return re.match(EMAIL_FORMAT, potentially_valid_email) is not None


class User:
    def __init__(self, username):
        self.username = username
        self._email = None

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if not is_valid_email(new_email):
            raise ValueError(f"Can't set {new_email} as it's not avalid email")
        self._email = new_email


if __name__ == '__main__':
    user = User("Yzemzgui")
    user_email = user.email
    user.email = "yzemzgui@gmail.com"
    print()
