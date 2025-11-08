from sqlalchemy import create_engine


class SQLManager:
    """SQLAlchemy engine and session manager."""

    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)

