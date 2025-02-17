import peewee


class AuthUser(peewee.Model):
    id = peewee.AutoField(primary_key=True)
    groupId = peewee.IntegerField()
    userId = peewee.IntegerField()
    type = peewee.CharField()


def add_auth_user(db, groupId, userId, type):
        with db.database:
            AuthUser.create(groupId=groupId, userId=userId, type=type)