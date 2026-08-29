from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from urllib.parse import quote_plus

password = "Adity@6288"

DATABASE_URL = f"postgresql://postgres:{quote_plus(password)}@localhost:5432/athena"

engine = create_engine(DATABASE_URL)

Base = declarative_base()


class CandidateDB(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    role = Column(String)
    experience = Column(String)


Base.metadata.create_all(engine)