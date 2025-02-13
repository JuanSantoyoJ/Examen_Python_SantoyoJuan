import json

def abrirJSON():
    dicFinal={}
    with open("./usuarios.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./usuarios.json",'w') as outFile:
        json.dump(dic,outFile)
usuarios={}
usuarios=abrirJSON()
InicioDeTodo=True
while InicioDeTodo:    
    print("-----------------------------------------------")
    print("      Bienvenido a Movistar Administrador      ")
    print("-----------------------------------------------")
    print("\n ¿Que desea hacer?")
    print("1. Ver usuarios")
    print("2. Agregar usuarios")
    print("3. Eliminar usuarios")
    opc=int(input("\nIngresa la opcion: "))
    if opc ==1:
        for i in range(len(usuarios["usuarios"])):
            print("Usuario: ",i+1)
            print("ID: ", usuarios["usuarios"][i]["ID"])
            print("Nombres: ",usuarios["usuarios"][i]["Nombres"])
            print("Apellidos: ",usuarios["usuarios"][i]["Apellidos"])
            print("Direccion: ",usuarios["usuarios"][i]["Direccion"])
            print("Telefono: ",usuarios["usuarios"][i]["Telefono"])
            print("\n")
    if opc ==2:
        nuevoUsuario={
            "ID": input("Ingrese la ID: "),
            "Nombres": input("Ingresa los nombres del usuario: "),
            "Apellidos": input("Ingresa los apellidos del usuario: "),
            "Direccion": input("Ingresa la direccion del usuario: "),
            "Telefono": input("Ingresa el telefono del usuario: ")}
        usuarios["usuarios"].append(nuevoUsuario)
        guardarJSON(usuarios)
    if opc==3:
        quitarUsuarioID={"ID": input("Ingresa el ID del usuario a eliminar: ")}
        for usuario in usuarios["usuarios"]:
            if usuario["ID"] == quitarUsuarioID:
                usuarios["usuarios"].remove(usuario)
            guardarJSON(usuarios)
            print("Usuario elminado")