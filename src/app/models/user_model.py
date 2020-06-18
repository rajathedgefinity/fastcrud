from sqlalchemy import Table, String, CHAR, Column
from app.db.db import metadata

users = Table(
    "users",
    metadata,
    Column("id"        , String, primary_key=True), # noqa
    Column("username"  , String), # noqa
    Column("password"  , String), # noqa
    Column("first_name", String), # noqa
    Column("last_name" , String), # noqa
    Column("gender"    , CHAR), # noqa
    Column("create_at" , String), # noqa
    Column("status"    , CHAR), # noqa
)
