from typing import Callable
def decorador(funcion:Callable) -> Callable:
    def puente():
        mensaje = input("Introduzca un texto para que decore el mensaje de la funcion: \n")
        print(mensaje)
        funcion()
    return puente

@decorador
def saludo() -> None:
    print("Funcion argumentos")

saludo()