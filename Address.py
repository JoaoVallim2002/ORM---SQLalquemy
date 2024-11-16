from Connection import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True)
    street = Column(String)
    number = Column(Integer)
    district = Column(String)
    
    patient = relationship('Patient', back_populates='address')

    def __init__(self, street, number, district):
        self.street = street
        self.number = number
        self.district = district

