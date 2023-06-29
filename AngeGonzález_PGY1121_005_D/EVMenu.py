"""Menú principal"""
import EVfunciones as fn

opc = 0
jugadores = []
while opc != 4:
    opc = fn.imprimirMenu()
    if opc == 1:
        fn.grabarJugador(jugadores)
    if opc == 2:
        fn.buscarParticipante(jugadores)
    if opc == 3:
        fn.imprimirPareja(jugadores)
print("Adios")
print("Ángel González")