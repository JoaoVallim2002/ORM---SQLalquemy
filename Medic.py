from Connection import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Medic(Base):
    __tablename__ = 'medics'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fk_id_specialism = Column(Integer, ForeignKey('specialisms.id'))
    
    specialism = relationship('Specialism', back_populates='medic')
    record = relationship('Record', back_populates='medic')

    def __init__(self, name, Specialism):
        self.name = name
        self.specialism = Specialism


