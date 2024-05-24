import copy
import os
import time
color_def='\033[0m'
amarillo='\033[93m'
azul='\033[94m'
morado='\033[95m'
rojo='\033[91m'
verde='\033[92m'

cuadro=chr(1)
cuadro1=chr(2)


class Cine:
    def __init__(self):
        self.matriz_panda = [[verde+cuadro]*9 for _ in range(9)]
        self.matriz_bufon = [[verde+cuadro]*9 for _ in range(9)]
        self.matriz_amigo = [[verde+cuadro]*9 for _ in range(9)]
        self.cont=0
        self.asientos_p = 0
        self.asientos_f = 0
        self.asientos_a = 0
        self.vali = 0
        self.butaca1 = []
        self.butaca2 = []
        self.butaca3 = []
        self.salir_1=0
        
    def reservar(self,pelicula):
        self.vali=0
        
        while self.vali==0:
            self.vali=0
            if pelicula==1:
                print(verde+"\n1.- Kung Fu Panda 4 (ESP)\n\nSigue a Po en sus aventuras por la antigua china, donde su amor por el kung fu solo es")
                print("compatible a su insaciable apetito.\n\n")
            if pelicula==2:
                print(morado+"\n2.-Bufon (ESP)\n\nUn malevolo ser conocido como el Bufon aterroriza a los habitantes de un peque�o pueblo en la noche de")
                print("halloween, incluyendo a dos hermanas separadas que deben unirse paraencontrar la manera de derrotar esta entidad.\n\n")
            if pelicula==3:
                print(amarillo+"\n3.-Amigos Imaginarios (ESP)\n\nSigue a una nina que pasa por una experiencia dificil y entonces empieza a ver a los ")
                print("amigos imaginarios de todo el mundo que se han quedado atras cuando sus amigos de la vida real han crecido.\n\n")
            regresar=input(color_def+"\nPresione (1) para regresar al menu y (2) para continuar: ")
            con=0
            self.validacion(regresar,con)
            os.system("cls")
            if(self.vali!=0):
                regresar=int(regresar)
        salir=0
        if regresar==2:
            salir=1
            
        while salir==1:
            if pelicula==1:
                matriz=self.matriz_panda.copy()
                print("\n**SALA 1  PELICULA: KUNG FU PANDA 4**\n")
            if pelicula==2:  
                matriz=self.matriz_bufon.copy()
                print("\n**SALA 2  PELICULA: BUFON**\n")
            if pelicula==3:
                matriz=self.matriz_amigo.copy()
                print("\n**SALA 3  PELICULA: AMIGOS IMAGINARIOS**\n")

            print("       1  2  3  4  5  6  7  8")
            for i in range (1,len(matriz)):
                print(color_def+"\n ",i, "  ", end=" ")
                for j in range (1,len(matriz[i])):
                    print(matriz[i][j], end="  ")
            self.vali=0
            while self.vali==0:
                self.vali=0
                fila=input(color_def+"\n\n Introduzca el numero de la fila: ")
                con=6
                self.validacion(fila,con)
                if(self.vali!=0):
                    fila=int(fila)

            self.vali=0
            while self.vali==0:
                self.vali=0
                colum=input("\n Introduzca el numero de la columna: ")
                con=6
                self.validacion(colum,con)
                if(self.vali!=0):
                    colum=int(colum)
                
            if(matriz[fila][colum]==verde+cuadro):
                matriz[fila][colum]=rojo+cuadro1
                
                print("\nReserva de asiento exitosa.\n")
                if pelicula==1:
                    self.asientos_p=self.asientos_p+1
                    self.butaca1.append("(")
                    self.butaca1.append(fila)
                    self.butaca1.append(colum)
                    self.butaca1.append(')')

                if pelicula==2:
                    self.asientos_f=self.asientos_f+1
                    self.butaca2.append('(')
                    self.butaca2.append(fila)
                    self.butaca2.append(colum)
                    self.butaca2.append(')')
                if pelicula==3:
                    self.asientos_a=self.asientos_a+1
                    self.butaca3.append('(')
                    self.butaca3.append(fila)
                    self.butaca3.append(colum)
                    self.butaca3.append(')')

            else:
                print("\nEl asiento ya ha sido reservado")
            self.vali=0
            while self.vali==0:
                self.vali=0
                salir=input("\nMarque (1) para reservar otro asiento y (2) para finalizar: ")
                con=0
                self.validacion(salir,con)
                if(self.vali!=0):
                    salir=int(salir)

            if salir==1:
                os.system("cls")
                if pelicula==1:
                    self.matriz_panda=matriz.copy()
                        
                if pelicula==2:
                    self.matriz_bufon=matriz.copy()
                        
                if pelicula==3:
                    self.matriz_amigo=matriz.copy()
            
                                
    def butaca(self,fila,colum,nombre):
        self.butacas=nombre
        num=1
        num1=0
        self.cont=0
        num3=0
        while num!=0 :
            num2=self.butacas.count(fila)
            num=self.butacas.index(fila,num1)
            num3=num3+1
            if self.butacas[num+1]==colum:
                self.butacas.pop(num+2)
                self.butacas.pop(num+1)
                self.butacas.pop(num)
                self.butacas.pop(num-1)
                num=0
            else:
                num1=num+2
                if num3==num2:
                    print("\nEl asiento ya esta reservado")
                    self.cont=1
                    num=0
                    
                    
                
                

        
    def cancelar(self,pelicula1):
        if pelicula1==1:
            matriz=self.matriz_panda.copy()
            
        if pelicula1==2:
            matriz=self.matriz_bufon.copy()
        if pelicula1==3:
            matriz=self.matriz_amigo.copy()
        salir=1
        while salir==1:
            os.system("cls")
            if pelicula1==1:
                matriz=self.matriz_panda.copy()
                print("\n**SALA 1  PELICULA: KUNG FU PANDA 4**\n")
            if pelicula1==2:  
                matriz=self.matriz_bufon.copy()
                print("\n**SALA 2  PELICULA: BUFON**\n")
            if pelicula1==3:
                matriz=self.matriz_amigo.copy()
                print("\n**SALA 3  PELICULA: AMIGOS IMAGINARIOS**\n")
            
            print("       1  2  3  4  5  6  7")
            for i in range (1,len(matriz)):
                print(color_def+"\n ",i, "  ", end=" ")
                for j in range (1,len(matriz[i])):
                    print(matriz[i][j], end="  ")
            self.vali=0
            while self.vali==0:
                self.vali=0
                fila=input(color_def+"\n\n Introduzca el numero de la fila: ")
                con=6
                self.validacion(fila,con)
                if(self.vali!=0):
                    fila=int(fila)
            self.vali=0
            while self.vali==0:
                self.vali=0
                colum=input("\n Introduzca el numero de la columna: ")
                con=6
                self.validacion(colum,con)
                if(self.vali!=0):
                    colum=int(colum)
        
            if(matriz[fila][colum]==rojo+cuadro1):
                num=self.butaca1.count(fila)
                num1=self.butaca1.count(colum)
                if pelicula1==1 and num!=0 and num1!=0:
                    
                    self.butaca(fila,colum,self.butaca1)
                    if self.cont==0:
                        self.asientos_p=self.asientos_p-1
                        matriz[fila][colum]=verde+cuadro
                        print("\nCancelacion de asiento exitoso.\n")
                
                num=self.butaca2.count(fila)
                num1=self.butaca2.count(colum)

                if pelicula1==2 and num!=0 and num1!=0:
                    self.butaca(fila,colum,self.butaca2)
                    if self.cont==0:
                        self.asientos_f=self.asientos_f-1
                        matriz[fila][colum]=verde+cuadro
                        print("\nCancelacion de asiento exitoso.\n")

                num=self.butaca3.count(fila)
                num1=self.butaca3.count(colum)

                if pelicula1==3 and num!=0 and num1!=0:
                    self.butaca(fila,colum,self.butaca3)
                    if self.cont==0:
                        self.asientos_a=self.asientos_a-1
                        matriz[fila][colum]=verde+cuadro
                        print("\nCancelacion de asiento exitoso.\n")
                
                if matriz[fila][colum]!=verde+cuadro and self.cont==0:
                    print("\nEl asiento ya esta reservado")

                
            else:
                print("\nEl asiento esta disponible")
                
            self.vali=0
            while self.vali==0:
                self.vali=0
                salir=input("\nMarque (1) para eliminar otro asiento y (2) para finalizar: ")
                con=0
                self.validacion(salir,con)
                if(self.vali!=0):
                    salir=int(salir)
                
            
        if pelicula1==1:
            self.matriz_panda=matriz.copy()
            os.system("pause")
                
        if pelicula1==2:
            self.matriz_bufon=matriz.copy()
            os.system("pause")
                
        if pelicula1==3:
            self.matriz_amigo=matriz.copy()
            os.system("pause")

    def tiempo(self,texto):
        print(texto," .", end="",flush=True)
        time.sleep(1)
        print(".",end="",flush=True)
        time.sleep(1)
        print(".",end="",flush=True)
        time.sleep(1)
        os.system("cls")
        
    def validacion(self, peli1, con):
        try:
            if(peli1.isdigit()):
                peli1=int(peli1)
                if (peli1>=1 and peli1<=2+con):
                    self.vali=3
                else:
                    print("\nERROR, introduzca nuevamente los numeros aceptados\n")
                    os.system("pause")
                    self.vali=0
            else:
                print("\nERROR, introduzca solamente numeros\n")
                os.system("pause")
                self.vali=0
        except ValueError:
            print("\nERROR, introduzca solamente numeros\n")
            self.vali=0
            os.system("pause")

    def factura(self):
        print(verde+"*****************************************")
        print("*\t\tFACTURA\t\t\t*") 
        print("*****************************************"+color_def)
        
        if (self.asientos_p!=0 or self.asientos_a!=0 or self.asientos_f!=0):
            if(self.asientos_p!=0):
                print("SALA 1 (KUNG FU PANDA 4) ASIENTOS COMPRADOS: ",self.asientos_p," butaca: ",self.butaca1)

            if(self.asientos_f!=0):
                print("SALA 2 (BUFON) ASIENTOS COMPRADOS: ",self.asientos_f," butaca: ",self.butaca2)

            if(self.asientos_a!=0):
                print("SALA 3 (AMIGOS IMAGINARIOS) ASIENTOS COMPRADOS: ",self.asientos_a," butaca: ",self.butaca3)

            self.asiento=self.asientos_a+self.asientos_f+self.asientos_p
            print("\n\nEl costo total por ",self.asiento," asientos es de: ",self.asiento*74,"Bs")
            self.vali=0
            while self.vali==0:
                self.vali=0
                print(azul+"\n*****************************************")
                print("*\tMETODO DE PAGO\t\t\t*") 
                print("*****************************************"+color_def)
                print(morado+"*****************************************")
                print("*\t1- PAGO MOVIL\t\t\t*")
                print(amarillo+"*\t2- PUNTO DE VENTA\t\t*")
                print(verde+"*\t3- EFECTIVO\t\t\t*")
                print(rojo+"*\t4- REGRESAR AL MENU\t\t*")
                print(morado+"*****************************************\n\n")
                pago=input(color_def+"Seleccione la opcion que desee: ")
                con=2
                self.validacion(pago,con) 
                os.system("cls")
                if(self.vali!=0):
                    pago=int(pago)
            if pago==1:
                self.vali=0
                while self.vali==0:
                    self.vali=0
                    print(morado+"*****************************************\n*\t\tPAGO MOVIL\t\t*")
                    print("*****************************************\n\n")
                    print(color_def+"BENEFICIARIO: J-503705264\nTELEFONO: 0416-4596852\nBANCO: BANCO DE VENEZUELA\n\n")
                    try:
                        refe=int(input("Introducir los ultimos 6 digitos de la referencia: "))
                        self.tiempo("\n\nPROCESANDO")
                        if refe<999999 and refe>99999:
                            self.vali=1
                        else:
                            print("Error en la referencia...")
                            os.system("pause")
                    except ValueError:
                        print("Error en la referencia...")
                        os.system("pause")
                    os.system("cls")
                print("GRACIAS POR SU COMPRA QUE DISFRUTE DE LA FUNCION\n")

            if pago==2:
                self.vali=0
                while self.vali==0:
                    self.vali=0
                    print(amarillo+"*****************************************\n*\t\tPUNTO DE VENTA\t\t*")
                    print("*****************************************\n\n"+color_def)
                    self.tiempo("PASANDO LA TARJETA")
                    try:
                        cedula=int(input("Introduzca Su Cedula: "))
                        if cedula<45000000 and cedula>5000000:
                            self.vali=1
                        else:
                            print("Error en la cedula...")
                            os.system("pause")
                    except ValueError:
                        print("Error en la cedula...")
                        os.system("pause")
                    os.system("cls")
                    if self.vali!=0:
                        self.tiempo("\n\nPROCESANDO")
                        print("Tipo de Cuenta")
                        print("\n1- Ahorro\n\n2- Corriente\n\n")
                        opcion=input("Seleccione la opcion que desee: ")
                        con=0
                        self.validacion(opcion,con)
                        os.system("cls")
                    if self.vali!=0:
                        self.tiempo("\n\nPROCESANDO")
                        try:
                            clave=int(input("Intruduzca Su Clave: "))
                            if(clave<=9999 and clave>=0000):
                                self.vali=1
                            else:
                                print("Error De Clave...")
                                os.system("pause")
                        except ValueError:
                            print("Error De Clave...")
                            os.system("pause")
                    
                    os.system("cls")
                print("GRACIAS POR SU COMPRA QUE DISFRUTE DE LA FUNCION\n")


            elif pago==3:
                self.vali=0
                while self.vali==0:
                    self.vali=0
                    print(verde+"*****************************************\n*\t\tEFECTIVO\t\t*")
                    print("*****************************************\n\n"+color_def)
                    print("1-DOLARES ($)\n2-BOLIVARES (BS)\n")
                    opc=input("Seleccione la opcion que desee: ")
                    self.tiempo("\n\nPROCESANDO")
                    con=0
                    self.validacion(opc,con)

                print("GRACIAS POR SU COMPRA QUE DISFRUTE DE LA FUNCION\n")
            if pago!=4:
                self.vali=0
                while self.vali==0:
                    self.vali=0
                    continuar=input("\n\nPresione (1) para regresar al menu y (2) para cerrar el cine: ")
                    con=0
                    self.validacion(continuar,con)
                if(self.vali!=0):
                    continuar=int(continuar)
                if continuar==2:
                    self.salir_1=4
                self.asientos_p = 0
                self.asientos_f = 0
                self.asientos_a = 0
                self.butaca1 = []
                self.butaca2 = []
                self.butaca3 = []
        else:
            print("No existe ninguna compra realizada\n")
        os.system("pause")


    def menu(self):       
        self.salir_1=0
        while self.salir_1!=4:
            self.vali=0
            while self.vali==0:
                self.vali=0
                print(rojo+"*****************************************\n*\t\tCINE \t\t*")
                print("*****************************************")
                print(azul+"*****************************************")
                print("*\t\t\t\t\t*\n*\t1.- CARTELERA Y RESERVA\t\t*")
                print("*\t\t\t\t\t*\n*\t2.- CANCELAR EL ASIENTO\t\t*")
                print("*\t\t\t\t\t*\n*\t3.- FACTURA DEL CLIENTE\t\t*")
                print("*\t\t\t\t\t*\n*\t4.- SALIR DEL CINE\t\t*")
                print("*\t\t\t\t\t*\n*****************************************\n")
                self.salir_1=input(color_def+"Seleccione la opcion que desee: ")
                con=2
                self.validacion(self.salir_1,con)
                os.system("cls")
                if(self.vali!=0):
                    self.salir_1=int(self.salir_1)

            if (self.salir_1==1):
                self.vali=0
                while self.vali==0:
                    self.vali=0
                    print(azul+"*****************************************")
                    print("*\t\tPELICULAS\t\t*")
                    print("*****************************************")
                    print(verde+"*\t1.- KUNG FU PANDA 4 (ESP)\t*")
                    print(morado+"*\t2.- BUFON (ESP)\t\t\t*")
                    print(amarillo+"*\t3.- AMIGOS IMAGINARIOS (ESP)\t*")
                    print(azul+"*****************************************"+color_def)
                    pelicula=input("\nMarque el numero de la pelicula que desee: ")
                    con=1
                    self.validacion(pelicula,con)
                    os.system("cls") 
                      
                    if(self.vali!=0):
                        pelicula=int(pelicula)
                
                self.reservar(pelicula)
                
            elif (self.salir_1==2):
                self.vali=0
                while self.vali==0:
                    self.vali=0
                    print(azul+"*****************************************")
                    print("*\tPELICULA QUE DESEA CANCELAR\t*")
                    print("*****************************************")
                    print(verde+"*\t1.- KUNG FU PANDA 4 (ESP)\t*")
                    print(morado+"*\t2.- BUFON (ESP)\t\t\t*")
                    print(rojo+"*\t3.- AMIGOS IMAGINARIOS (ESP)\t*")
                    print(amarillo+"*\t4.- REGRESAR AL MENU\t\t*")
                    print(color_def+"*****************************************")
                    pelicula1=input("\nMarque el numero que la pelicula que desee cancelar: ")
                    con=2
                    self.validacion(pelicula1,con)
                    os.system("cls")
                    
                    if(self.vali!=0):
                        pelicula1=int(pelicula1)
                    
                if pelicula1!=4:
                    self.cancelar(pelicula1)
                
                
            elif (self.salir_1==3):
                self.factura()

            elif (self.salir_1==4):
                print("*****GRACIAS POR UTILIZAR NUESTRO CINE*****")
                os.system("pause")

            os.system("cls")

cine = Cine()
cine.menu()