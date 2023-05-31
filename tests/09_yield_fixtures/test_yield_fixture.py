import pytest


class MailBox:
    def __init__(self):
        self.inbox = []

    def receive(self, email):
        self.inbox.append(email)

    def clear(self):
        self.inbox.clear()

    def size(self):
        return len(self.inbox)


class Email:
    def __init__(self, subject, body):
        self.subject = subject
        self.body = body


@pytest.fixture
def mail_box():
    # setup/preconditions may go here
    box = MailBox()
    yield box
    # teardown/postconditions may go here
    box.clear()
    print(box.size())


def test_email_received(mail_box):
    email = Email(subject="Hey!", body="How's it going?")
    mail_box.receive(email)
    assert mail_box.size() == 1

