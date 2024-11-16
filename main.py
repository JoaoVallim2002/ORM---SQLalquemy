from Hospital import *


while True:
    show_menu()
    option = input("Escolha sua opção: ").upper()

    if option == '1':
        add_patient()
    elif option == '2':
        add_medic()
    elif option == '3':
        add_record()
    elif option == '4':
        data_show()
    elif option == '5':
        clean()
    elif option == 'EXIT':
        break
    else:
        print(color_text("\nInforme opção válida\n", 33))
        sleep(2)