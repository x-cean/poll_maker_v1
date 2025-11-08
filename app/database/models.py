import uuid


from datetime import datetime
from pydantic import EmailStr, model_validator
from sqlmodel import Field, Relationship, SQLModel


class Polls(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    question: str
    options: list["PollOptions"] = Relationship(back_populates="poll", cascade_delete=True)
    created_at: datetime = Field(default_factory=datetime.now)
    is_private: bool = False

    def __repr__(self):
        return f"Poll(id: {self.id}, question: {self.question}, created_at: {self.created_at})"

    def __str__(self):
        return f"Poll(id: {self.id}, question: {self.question}, created_at: {self.created_at})"


class PollOptions(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    poll_id: uuid.UUID = Field(foreign_key="polls.id", nullable=False, ondelete="CASCADE")
    option_text: str
    vote_count: int = 0
    poll: Polls = Relationship(back_populates="options")

    def __repr__(self):
        return f"PollOptions(id: {self.id}, option_text: {self.option_text}, votes: {self.votes})"

    def __str__(self):
        return f"PollOptions(id: {self.id}, option_text: {self.option_text}, votes: {self.votes})"