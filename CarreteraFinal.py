
"""
El siguiente programa busca simular un SATV(Sistema Autonomo de Trafico Vehicular) mediante una 
programacion en python, se programa un sensor de conteo el mismo que tiene que estar activado para 
poder realizar su función, se instanciaran clases para poder manejar ciertos parametros de una manera
un poco mas sencilla,de esta manera se busca un programa funcional para futuros proeyctos

Autores:
Jose Sanmartin
Verisión:
Ver. 1.1
"""
import os
class sistema_automatico:
    """
    Esta clase representa un sistema automático de trafico vehicular SATV la cual tiene un estado,una 
    localización, un sensor de conteo y un costo, a través de los cuales se puede activar o desactivar 
    
    Métodos
    ----------
    Carretera(self,localizacion, estado, costo, sensor, estadoObjetivo)
    Define los parametros del sensor para despúes poder implementarlos en el programa   
    """
    
    def Carretera(self,localizacion, estado, costo, sensor, estadoObjetivo):
        """
        Este método define la localización, el estado, el costo y el sensor de conteo en la carretera,estos 
        parámetros servirán para realizar el análisis correspondiente para saber si se debe activar o no el 
        sensor de conteo en la autopista

        Parametros
        -----------
            localizacion (str): Indica la ubicacion del sensor, en que carretera esta ubicado.
            estado (str): Indica el estado del sensor activado o desactivado.
            costo (int): Indica el costo de las acciones realizadas por el sensor de conteo.
            sensor (str): Describe si el sensor se encuentra dentro del rango de accion de la carretera.
            estadoObjetivo (diccionario): Proporciona el estado objetivo de las carreteras evaluadas.

        Returns:
            costo: Retorna el costo total de las acciones realizadas por el sensor de conteo del SATV.
        """
        # Se inicia el control de excepciones
        try:
            # Se asigna la ubicacion del sensor de conteo.
            self.localizacion = localizacion
            # Se asigna el estado del sensor de conteo (Activado o Desactivado).
            self.estado = estado
            # Se asigna el costo actual de las acciones realizada por el sensor.
            self.costo = costo
            # Se asigna el estado en cuanto a rando del sensor de conteo.
            self.sensor = sensor
            
            # Si el sensor esta dentro del rango de accion de la carretera analizada.
            if sensor == 's' or sensor == 'S':
                # Imprime la ubicación del sensor de conteo
                print("El sensor se encuentra en  ", localizacion)
                # Si el estado de el sensor es desactivado.
                if(estado == '1'):
                    # Imprime el estado del sensor.
                    print("El sensor de la ", localizacion, " esta desactivado")
                    # Se asigna el nuevo estado del sensor de la localizacion correspondiente.
                    estadoObjetivo[localizacion] = '0'
                    # Se incrementa el costo en 1
                    costo += 1
                    # Se imprime el nuevo costo de la activacion del sensor.
                    print("El costo de activar el sensor de conteo es: ", costo)
                    # Se imprime el nuevo estado de la puerta inteligente.
                    print("El sensor se encuentra activado")
                    # Se retorna el costo actual de las acciones realizadas por el sensor.
                    return costo
                
                # Si el estado del sensor es activado entonces.
                else:
                    # Imprime el estado del sensor de conteo de la SATV.
                    print("El sensor en la ", localizacion, " esta activo")
                    # Se muestra un mensaje informactivo de las acciones realizadas por el sensor.
                    print("No se realizo ninguna acción")
                    #Se imprime el costo actual de la accion realizada por el sensor.
                    print("El costo de activar el sensor es de: ", costo)
                    # Se retorna el costo actual de las acciones realizadas por el sensor de conteo.
                    return costo
                
            # Si el sensor no se encuentra dentro del rango de la carretera a anlizar.
            else:
                # Imprime un mensaje indicando que el sensor no se encuentra dentro del rango de accion de la carretera.
                print("El sensor de conteo no se encuentra en el rango adecuado para ejecutarse")
                # Se retorna el costo actual de las acciones realizadas por la puerta inteligente.
                return costo
            
        # Se captura la excepcion.
        except Exception as e:  
            # Se imprime el mensaje de la excepcion.
            print(e)    

# Ejecucion del programa.
if __name__ == '__main__':
    # Se inicia el control de excepciones 
    try:
        # Se crea el diccionario de la ubicacion del sensor de SATV.
        estadoObjetivo = {'RUMINAHUI': '0', 'OCCIDENTAL': '0', 'SIMONBOLIVAR': '0','ALOAG': '0'}
        
        # Se crea una instancia de la clase SATV.
        sistema = sistema_automatico()

        # Se define un bucle para el ingreso de una localizacion valida.
        while True:
            # Se inicializa el costo
            costo = 0
            # Se imprime el menu de opciones.
            print("\n**************Siste Automatico de Transito Vehicular************** \nUbicaciones disponibles: \nRUMINAHUI\nOCCIDENTAL \nSIMONBOLIVAR \nALOAG \n Introduzca la palabra 'SALIR' para salir del sistema")
            # Se pide la carretera del sensor de conteo .
            localizacion = input("Por favor ingrese la locacion del sensor que se desea activar,recuerda que debe estar en MAYUSCULAS\n")
            # Si la localizacion ingresada se encuentra fuera del rango de las ubicaciones disponibles.
            if localizacion != 'RUMINAHUI' and localizacion != 'OCCIDENTAL' and localizacion != 'SIMONBOLIVAR' and localizacion != 'ALOAG'  and localizacion != 'SALIR':
                print("Error ,La carretera ingresada no fue encontrada, recuerda que debe estar en la lista y en MAYUSCULAS\n")
                
            # Si la localizacion ingresada es igual a la palabra 'SALIR'.
            elif localizacion== 'SALIR' or localizacion=="salir" :
                # Se imprime un mensaje de despedida.
                print("Gracias por usar el sistema, Regrese Pronto")
                os.system("pause")
                # Se termina el bucle para el ingreso de una localizacion valida.
                break
            
            # Si la localizacion ingresada es correcta.
            else:
                # Se define un bucle para el ingreso de un estado valido
                while True:
                    # Se solicita el ingreso del estado de la puerta inteligente en la ubicación indicada.
                    estado = input("Por favor ingrese el estado de el sensor, Porfavor Ingrese '0' (para indicar que el sensor esta activado) o '1' (Para indicar que el sensor esta desactivado) \n Introduzca la palabra 'SALIR' para salir del sistema\n")
                    
                    # Si el estado ingresado es diferente a 0 o 1.
                    if estado != '0' and estado != '1'and estado != 'salir'and estado != 'SALIR':
                        # Se imprime un mensaje de error.
                        print("Opcion Incorrecta, por favor intente de nuevo\n")
                        
                    # Si el estado ingresado es igual a SALIR.
                    elif estado == 'SALIR' or estado=="salir":
                        # Se imprime un mensaje de despedida.
                        print("Gracias por usar el sistema")
                        os.system("pause")
                        # Se termina el bucle para el ingreso de un estado valido.
                        break
                    
                    # Si el estado ingresado es correcto.
                    else:
                        # Se define un bucle para el ingreso de una llave valida.
                        while True:
                            # Se solicita el ingreso del sensor, si se encuentra dentro de la ubicacion requerida 
                            sensor = input("Por favor ingrese si el sensor de conteo se encuentra dentro de la carretera solicitada , Porfavor Ingrese 's' (Si este se encuentra dentro de la carretera) o 'n' (NO se encuentras dentro de la carretera) \n Introduzca la palabra 'SALIR' para salir del sistema\n")
                            
                            # Si la opcion ingresada es incorrecta.
                            if sensor != 's' and sensor != 'S' and sensor != 'n' and sensor != 'N' and sensor != 'SALIR'and sensor != 'salir':
                                # Se imprime un mensaje de error.
                                print("Error, opcion no valida por favor inente de nuevo\n")
                                
                            # Si la opcion ingresada  ingresada es igual a SALIR.
                            elif sensor == 'SALIR' or sensor=="salir":
                                # Se imprime un mensaje de despedida.
                                print("Gracias por usar el sistema")
                                # Se termina el bucle para el ingreso de una llave valida.
                                os.system("pause")
                                break
                            
                            # Si la llave ingresada es correcta.
                            else:
                                # Se realiza las acciones correspondientes para la localizacoin y estado ingresados por el usuario.
                                costo = int(sistema.Carretera(localizacion,estado,costo,sensor,estadoObjetivo))
                                
                                # Se establece un bucle que recorre el diccionario con la ubicaciones.
                                for key, value in estadoObjetivo.items():
                                    # Si la localizacion obtenida en el bucle es diferente a la ingresada por el usuario.
                                    if key != localizacion:
                                        # Se establece un bucle para el ingreso de un estado valido.
                                        while True:
                                            # Se imprime la localizacion actual
                                            print("\nRedirigiendo a  ", key)
                                            # Se solicita el ingreso del estado del sensor de conteo.
                                            estados = input("Por favor ingrese el estado del sensor de coteo, Porfavor Ingrese '0' (para indicar que esta activado) o '1' (Para indicar que esta desactivado) \n Introduzca la palabra 'SALIR' para salir del sistema\n")
                                            # Si el estado ingresado es diferente a 0 o 1.
                                            if estados != '0' and estados != '1' and estados != 'SALIR':
                                                # Se imprime un mensaje de error.
                                                print("El estado no es correcto, Por favor intente de nuevo\n")
                                                
                                            # Si el estado ingresado es igual a SALIR.
                                            elif estados == 'SALIR':
                                                # Se imprime un mensaje de despedida.
                                                print("Gracias por usar el sistema")
                                                os.system("pause")
                                                # Se termina el bucle para el ingreso de un estado valido.
                                                break
                                            # Si el estado ingresado es correcto.
                                            else:
                                                # Se define un bucle para el ingreso de un sensor valido.
                                                while True:
                                                    # Se solicita el ingreso del sensor, saber si este se encuentra dentro de la carretera esepecificada .
                                                    sensor = input("Por favor ingrese si el sensor se encuentra dentro de la carretera especificada, Porfavor Ingrese 's' (si se encuentra dentro de la carretera) o 'n' (no se encuentra dentro de la carretera \n Introduzca la palabra 'SALIR' para salir del sistema\n")
                                                    # Si la opcion ingresada no es correcta.
                                                    if sensor != 's' and sensor != 'S' and sensor!= 'n' and sensor != 'N' and sensor != 'SALIR':
                                                        # Se imprime un mensaje de error.
                                                        print("La llave no es correcta, Por favor intente de nuevo\n")

                                                    # Si la opcion ingresada es igual a SALIR.
                                                    elif sensor == 'SALIR':
                                                        # Se imprime un mensaje de despedida.
                                                        print("Gracias por usar el sistema")
                                                        os.system("pause")
                                                        # Se termina el bucle para el ingreso de una llave valida.
                                                        break
                                                    
                                                    # Si la llave ingresada es correcta.
                                                    else:
                                                        # Se realiza las acciones correspondientes para localizacion y estado indicados en el bucle.
                                                        costo = int(sistema.Carretera(key,estados,costo,sensor,estadoObjetivo))
                                                        # Se termina el bucle para el ingreso de una llave valida.
                                                        break
                                                # Se termina el bucle para el ingreso de un estado valido.
                                                break
                                # Se imprime el costo total.    
                                print("\nEl costo total de abrir las puertas es de ", costo, " \n")
                                # Se imprime un mensaje informativo.
                                print("Estados de la puerta: \n")
                                # Se imprime el estado objetivo de la puerta en cada ubicación.
                                print(estadoObjetivo,"Todos los sensores estan activados")
                                # Se termina el bucle para el ingreso de una llave valida.
                                break
                        # Se termina el bucle para el ingreso de un estado valido.
                        break
    # Se captura la excepcion.           
    except Exception as e: 
        # Se imprime el mensaje de error.
        print(e)  
        