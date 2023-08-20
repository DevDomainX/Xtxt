#!/usr/bin/env python3
import os
import shutil
from banner import banner
from  colorama import init, Fore, Style, Back
init()


def cabecera():
    banner()
    print(Fore.CYAN+"""\n\n
created by: 1lugarparaprogramar

Date : sabado 19 de agosto

created : H.saldias

Script para crear diccionarios de contraseñas 
para ataques de fuerza bruta 
    \n\n""")


def  created_dir():
    if not  os.path.exists("diccionarios"):
        os.mkdir("diccionarios")
    print("directory create")
    return menu()
  
def created():
    archive = input("Insert name archive =>  ")
    archive = archive + ".txt"
    with open(archive, "a") as con:
            pw = input("Insert password =>  ")
            con.write(pw.replace(' ', "\n"))
            shutil.move(archive, "diccionarios")
            op =  input("return Created [y/n]: ")
            if op  == "y":
                created()
            else:
                print("@1LugarParaProgramar")
        
def Intructions():
       print("1. crear nombre del archivo sin .txt ya que se agrega solo\n2. Ingrear contraseñas dependiendo para quien o que sea una al lado de otra solo  con un 1 espacio todas las posibles\ n ya que a estemismo archivo no  se le podra agregar mas\nEn  caso  de ingresar mas se  tiene  que poner el mismo nombre  en el archivo        ")
       op = input("Volver a menu (y/n): ")
       if  op == "y":
           menu()
       else:
           print("@1LugarParaProgramar")
       
def spain():
        print("""
        
        < 1 >  Crear diccionario contraseñas
        
        < 2 >  Ver intrucciones  
        
        < 3 > Crear carpeta para guardar archivos
        
        < 4 > Ver en  español
        
        < 0 > Salir
        """)
        option = int(input("Insert option =>  "))
        if option == 1:
            created()
        elif option == 2:
            Intructions()
        elif option == 3:
            created_dir()
        elif option  == 4:
            spain()
        elif option == 0:
            banner()
            os.system("exit")
        else:
            print("Fatal Error, input invalide")
            menu()
        
       
def menu():
        os.system("apt update -y && apt upgrade -y")
        pass
        cabecera()
        print("""
        
        < 1 >  Created Archive password
        
        < 2 >  Look Intructions
        
        < 3 > Created directory
        
        < 4 > Look spanish
        
        < 0 > Exit()
        """)
        option = int(input("Insert option =>  "))
        if option == 1:
            created()
        elif option == 2:
            Intructions()
        elif option == 3:
            created_dir()
        elif option  == 4:
            spain()
        elif option == 0:
            banner()
            print("======>  1LugarParaProgramar <=======\n======> Created by: H.saldias <=======")
            os.system("exit")
        else:
            print("Fatal Error, input invalide")
            menu()
            

            
            
            
menu()            


            
            
        