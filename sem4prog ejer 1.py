"""
ejer1

Elabore un programa que permita
el ingreso de matricula y kilometraje(separadospor una coma)
Hasta que el usuario ingrese "fin",luego mostrar la matricula del
carro con mayor kilometraje

"""
ingreso=""
matriculas=[]
kmL=[]
while(ingreso!="fin"):
    ingreso=input("Ingrese matricula, Kilometraje: ")#GSK-587,150000
    if ingreso!="fin":
        datos=ingreso.split(",")#[GSK-587,150000]
        matri=datos[0]#"GSK-587"
        km=datos[1]
        matriculas.append(matri)
        kmL.append(int(km))

mayorKm=max(kmL)
posKm=kmL.index(mayorKm)
mayorMatri=matriculas[posKm]
print("La matricula con mayor km es: ",mayorMatri,"con:",mayorKm,"km")

