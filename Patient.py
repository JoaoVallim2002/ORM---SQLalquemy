from Connection import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    telephone = Column(String)
    fk_id_address = Column(Integer, ForeignKey('addresses.id'))
    
    address = relationship('Address', back_populates='patient')
    record = relationship('Record', back_populates='patient')

    def __init__(self, name, telephone, Address):
        self.name = name
        self.telephone = telephone
        self.address = Address


