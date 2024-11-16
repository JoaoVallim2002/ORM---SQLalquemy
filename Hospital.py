from Connection import Base, engine, session
from Address import Address
from Specialism import Specialism
from Medic import Medic
from Patient import Patient
from Record import Record
from time import sleep
from datetime import date


Base.metadata.create_all(engine)

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def show_menu():
    print(color_text("-------- MENU HOSPITAL --------", 36))
    print("1 - CADASTRAR PACIENTE")
    print("2 - CADASTRAR MÉDICO")
    print("3 - CADASTRAR CONSULTA")
    print("4 - CONSULTAR DADOS (Paciente, Médico ou consulta)")
    print("5 - LIMPAR TODAS AS TABELAS (Apaga os dados somente, estrutura permanece)\n")
    print(color_text("Digite EXIT para sair\n", 31))

def add_patient():
    name = input('Nome do paciente: ')
    telephone = input('Telefone: ')
    list_address = session.query(Address).all()
    if len(list_address) > 0:
        for addres in list_address:
            print(f"[{addres.id}] - {addres.street} {addres.number} {addres.district}")
    else:
        print("Nenhum endereço cadastrado :(")
    if input('Deseja cadastrar um endereço? (S) / (N): ').upper() == 'S':
        street = input('Rua: ')
        number = input('Número: ')
        district = input('Bairro: ')
        address_final = Address(street, number, district)
        session.add(address_final)
        session.commit()
    else:
        option = int(input('Selecione um endereço cadastrado das opções acima: '))
        address_final = session.query(Address).filter_by(id=option).first()
        if address_final is None:
            print(color_text("Erro: O endereço com esse ID não existe.\n", 31))
            sleep(2)
            return
    patient = Patient(name, telephone, address_final)
    session.add(patient)
    session.commit()
    print(color_text("Paciente cadastrado com sucesso!!\n\n", 32))
    sleep(2)

def add_medic():
    name_medic = input('Nome do médico: ')
    list_specialisms = session.query(Specialism).all()
    if len(list_specialisms) > 0:
        for specialism in list_specialisms:
            print(f"[{specialism.id}] - {specialism.name}")
    else:
        print("Nenhuma especialidade cadastrada :(")
    if input('Deseja cadastrar uma especialidade? (S) / (N): ').upper() == 'S':
        name = input('Especialidade: ')
        specialism_final = Specialism(name)
        session.add(specialism_final)
        session.commit()
    else:
        option = int(input('Selecione uma especialidade cadastrada das opções acima: '))
        specialism_final = session.query(Specialism).filter_by(id=option).first()
        if specialism_final is None:
            print(color_text("Erro: A especialidade com esse ID não existe.\n", 31))
            sleep(2)
            return
    medic = Medic(name_medic, specialism_final)
    session.add(medic)
    session.commit()
    print(color_text("Médico cadastrado com sucesso!!\n\n", 32))
    sleep(2)

def add_record():
    date_record = input('Qual a data da consulta? (DD/MM/YYYY): ')
    print()
    date_record = date_record.split('/')
    day = int(date_record[0])
    month = int(date_record[1])
    year = int(date_record[2])
    list_medics = session.query(Medic).all()
    for medic in list_medics:
        print(f"[{medic.id}] - {medic.name}")
    id_medic = int(input('Selecione o médico da consulta: '))
    print()
    id_medic = session.query(Medic).filter_by(id=id_medic).first()
    if id_medic is None:
        print(color_text("Erro: O médico com esse ID não existe.\n", 31))
        sleep(2)
        return
    list_patients = session.query(Patient).all()
    for patient in list_patients:
        print(f"[{patient.id}] - {patient.name}")
    id_patient = int(input('Selecione o paciente: '))
    print()
    id_patient = session.query(Patient).filter_by(id=id_patient).first()
    if id_patient is None:
        print(color_text("Erro: O paciente com esse ID não existe.\n", 31))
        sleep(2)
        return
    description = input('Descreva o motivo da consulta: ')
    record = Record(id_patient, id_medic, description, date(year, month, day))
    session.add(record)
    session.commit()
    print(color_text("Consulta marcada!!\n", 32))
    sleep(2)

def clean():
    list_records = session.query(Record).all()
    for record in list_records:
        session.delete(record)
        session.commit()

    list_patients = session.query(Patient).all()
    for patient in list_patients:
        session.delete(patient)
        session.commit()

    list_medics = session.query(Medic).all()
    for medic in list_medics:
        session.delete(medic)
        session.commit()

    list_specialisms = session.query(Specialism).all()
    for specialism in list_specialisms:
        session.delete(specialism)
        session.commit()

    list_addresses= session.query(Address).all()
    for address in list_addresses:
        session.delete(address)
        session.commit()
    print(color_text("Dados excluidos com sucesso!!", 32))
    sleep(2)

def data_show():
    print("\n1 - Mostrar Pacientes")
    print("2 - Mostrar Médicos")
    print("3 - Mostrar consultas\n")

    option = input("Escolha sua opção: ").upper()
    print()

    if option == '1':
        list_patients = session.query(Patient).all()
        for patient in list_patients:
            print(f"Código do paciente: {patient.id}")
            print(f"Nome: {patient.name}")
            print(f"Telefone: {patient.telephone}")
            print(f"Endereço: {patient.address.street} {patient.address.number} {patient.address.district}\n")
            sleep(2)
    elif option == '2':
        list_medics = session.query(Medic).all()
        for medic in list_medics:
            print(f"Código do médico: {medic.id}")
            print(f"Nome: {medic.name}")
            print(f"Especialidade: {medic.specialism.name}\n")
            sleep(2)
    elif option == '3':
        list_records = session.query(Record).all()
        for record in list_records:
            print(f"Consulta de N: {record.id}")
            print(f"Paciente: {record.patient.name}")
            print(f"Médico da consulta: {record.medic.name}")
            print(f"INDICAÇÕES: {record.description}")
            print(f"Data da consulta: {record.date}\n")
            sleep(2)
    else:
        print(color_text("OPÇÃO INVÁLIDA!!", 31))
        sleep(2)