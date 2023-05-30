qt_passageiros, tipo_trans = input().split()
qt_passageiros = int(qt_passageiros)
#C para Canoa, V para voadeira e B para barco
if tipo_trans == "C":
    print(f"Para transportar {qt_passageiros} passageiros de canoa sairá R$ {qt_passageiros * 60:.2f}.")
if tipo_trans == "V":
    print(f"Para transportar {qt_passageiros} passageiros de voadeira sairá R$ {qt_passageiros * 120:.2f}.")
if tipo_trans == "B":
    print(f"Para transportar {qt_passageiros} passageiros de barco sairá R$ {qt_passageiros * 40 + (65*qt_passageiros):.2f}.")