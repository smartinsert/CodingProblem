from enum import Enum
from abc import ABC, abstractmethod


class ConnectionInvitationStatus(Enum):
    Pending = 'Pending'
    Accepted = 'Accepted'
    Declined = 'Declined'
    Cancelled = 'Cancelled'


class AccountStatus(Enum):
    Active = 'Active'
    BlackListed = 'Blacklisted'
    Closed = 'Closed'
    Cancelled = 'Cancelled'


class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country


class Account:
    def __init__(self, account_id, password, status=AccountStatus.Active):
        self.account_id = account_id
        self.password = password
        self.status = status

    def reset_password(self):
        raise  NotImplementedError


class Person(ABC):
    def __init__(self, name: str, address: Address, phone_number: str, email: str):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.email = email


class Member(Person):
    def __init__(self, name: str, address: Address, phone_number: str, email: str,
                 date_of_joining: str, headline: str, photo):
        super(Member, self).__init__(name, address, phone_number, email)
        self.date_of_joining = date_of_joining
        self.headline = headline
        self.photo = photo
        self.profile = Profile()
        self.connections = list()
        self.suggestions = list()
        self.group_follows = list()
        self.member_follows = list()

    def send_message(self, message: Message):
        raise NotImplementedError

    def send_connection_invitation(self, connection_invitation: ConnectionInvitation):
        raise NotImplementedError

    def create_post(self, post: Post):
        raise NotImplementedError


class Admin(Person):
    def __init__(self, name: str, address: Address, phone_number: str, email: str):
        super(Admin, self).__init__(name, address, phone_number, email)

    def block_user(self, member):
        raise NotImplementedError

    def unblock_user(self, member):
        raise NotImplementedError

class Stats:
    def __init__(self):
        self.total_likes = 0
        self.total_connections = 0
        self.search_appearances = 0

class Post:
    def __init__(self, text):
        self.text = text
        self.total_likes = 0
        self.total_shares = 0

    def update_post(self, text):
        self.text = text


class ConnectionInvitation:
    def __init__(self, connection_invitation_status):