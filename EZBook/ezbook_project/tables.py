# example/app/tables.py
from models import User
from table import Table
from table.columns import Column

class UserTable(Table):
    id = Column(field='id')
    user_pic = Column(field='user_pic')
    username = Column(field='username')
    password = Column(field='password')
    firstname = Column(field='firstname')
    middlename = Column(field='middlename')
    lastname = Column(field='lastname')
    age = Column(field='age')
    phone_number  = Column(field='phone_number ')
    email = Column(field='email')
    date_created = Column(field='date_created')
    class Meta:
        model = User