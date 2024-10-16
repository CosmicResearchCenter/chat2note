from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool



from alembic import context

from dotenv import load_dotenv
import os


# 加载 .env 文件
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# 从环境变量中获取数据库连接信息
MYSQL_IP = os.getenv("MYSQL_IP", "localhost")
MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
MYSQL_BASE = os.getenv("MYSQL_BASE", "chat2note")
MYSQL_USER = os.getenv("MYSQL_USER", "chat2note")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "chat2note")

# 构建 SQLAlchemy 的数据库连接 URL
DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_IP}:{MYSQL_PORT}/{MYSQL_BASE}"

# Alembic 配置
config = context.config
config.set_main_option("sqlalchemy.url", DATABASE_URL)


from models.llm_info import Base
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
