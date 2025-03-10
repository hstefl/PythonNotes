from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker, declarative_base

# Create an engine and base class
engine = create_engine('sqlite:///:memory:')
Base = declarative_base()


# Define a model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return f"<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>"


# Create all tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create and add a new user
new_user = User(name='John', fullname='John Doe', nickname='johnny')
session.add(new_user)
session.commit()

# Query the database
our_user = session.query(User).filter_by(name='John').first()
print(our_user)
