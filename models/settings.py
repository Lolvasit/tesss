from peewee import CharField, Model, SqliteDatabase, IntegrityError, IntegerField, AutoField

database = SqliteDatabase("database.sqlite3")


class BaseModel(Model):
    class Meta:
        database = database


class Setting(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField()
    value = CharField(default=None, null=True)
    step = IntegerField(null=False, default=0)

    def __repr__(self) -> str:
        return f"<Setting {self.name}:{self.value}>"

    class Meta:
        table_name = "settings"

    @classmethod
    def get_many(cls, names, step=0):
        lst = [cls.get_or_none(name=name,step=step) for name in names]
        return [item.value if item else None for item in lst]

    @classmethod
    def set_many(cls, kwargs, step=0):
        for name, value in kwargs.items():
            cls.update({cls.value:value}).where((cls.name == name) & (cls.step == step)).execute()
