from Connection import Base
from sqlalchemy import Column, Integer, ForeignKey, Text, Date
from sqlalchemy.orm import relationship

class Record(Base):
    __tablename__ = 'records'

    id = Column(Integer, primary_key=True)
    fk_id_patient = Column(Integer, ForeignKey('patients.id'))
    fk_id_medic = Column(Integer, ForeignKey('medics.id'))
    description = Column(Text)
    date = Column(Date)

    medic = relationship('Medic', back_populates='record')
    patient = relationship('Patient', back_populates='record')

    def __init__(self, Patient, Medic, description, date):
        self.patient = Patient
        self.medic = Medic
        self.description = description
        self.date = date


        

