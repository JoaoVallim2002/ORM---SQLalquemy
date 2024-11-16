from Connection import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Specialism(Base):
    __tablename__ = 'specialisms'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    medic = relationship('Medic', back_populates='specialism')

    def __init__(self, name):
        self.name = name

