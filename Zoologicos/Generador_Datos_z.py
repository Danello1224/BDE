from faker import Faker
import random
import datetime
import sys
import os
from faker.providers import BaseProvider

class DataBaseZProvider(BaseProvider):
    
    def sexo_especie(self):
        sexo=[
            "Macho",
            "Hembra"
        ]
        return self.random_element(sexo)
    
    def estado_tratamiento(self):
        estado_tr=[
            "Activo",
            "Finalizado"
        ]
        return self.random_element(estado_tr)
    
    def dia_semana_v(self,fecha_r):
        dia=fecha_r.strftime("%A")
        dias_es={
            "Monday": "Lunes",
            "Tuesday": "Martes",
            "Wednesday": "Miercoles",
            "Thursday": "Jueves",
            "Friday": "Viernes",
            "Saturday": "Sabado",
            "Sunday": "Domingo"
        }

        dia_es=dias_es[dia]
        return dia_es

def combinacion_tratamiento_e(unique_id_especie,unique_id_tratamiento_combinacion_e):
    
    asigna = True
    while asigna:
        dato=random.choice(unique_id_especie)
        if dato not in unique_id_tratamiento_combinacion_e:
            unique_id_tratamiento_combinacion_e.add(dato)
            break
            asigna= False
    return dato

def combinacion_tratamiento_m(unique_id_medicamento,unique_id_tratamiento_combinacion_m):
    
    asigna = True
    while asigna:
        dato=random.choice(unique_id_medicamento)
        if dato not in unique_id_tratamiento_combinacion_m:
            unique_id_tratamiento_combinacion_m.add(dato)
            break
            asigna= False
        else:
            break
            asigna= False
    return dato

def combinacion_venta_z(unique_id_zoo,unique_id_venta_combinacion_z):
    
    asigna = True
    while asigna:
        dato=random.choice(unique_id_zoo)
        if dato not in unique_id_venta_combinacion_z:
            unique_id_venta_combinacion_z.add(dato)
            break
            asigna= False
        else:
            break
            asigna= False
    return dato

def combinacion_zoo_esta(unique_id_zoo,fk_id_zoo_dicc):

    asigna=True
    while asigna:
        dato_e=random.choice(unique_id_zoo)
        suma_dic=sum(fk_id_zoo_dicc.values())
        
        if suma_dic >= (len(unique_id_zoo)*3):
            fk_id_zoo_dicc[dato_e] += 1
            break
        else:
            if fk_id_zoo_dicc[dato_e] < 3:
                fk_id_zoo_dicc[dato_e] += 1
                break
    return dato_e

## Codigo Principal 
fake = Faker('es_MX')
fake.add_provider(DataBaseZProvider)

#num_venta = 15871
#num_comidas = 462
#num_medicamentos = 6666

num_venta = 15
num_comidas = 4
num_medicamentos = 66
num_estacionamiento=240

fecha_inicio=datetime.date(2021,1,1)
fecha_final=datetime.date(2024,6,9)

unique_id_animales=list()
unique_id_medicamento=list()
unique_id_boleto=list()
unique_id_zoo=list()
unique_id_especie=list()
unique_id_tratamiento=list()

unique_id_tratamiento_combinacion_e=set()
unique_id_tratamiento_combinacion_m=set()
unique_id_venta_combinacion_z=set()


#________________________________________________________________________________________________________________
## RUTA 1 ANIMALES
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\animales.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
    
with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO animales (id_animal,nombre_animal,nombre_cientifico,familia,genero,especie,orden,clase,peligro_extincion)\nVALUES\n')
    
    lista_animales = {
        1: ["Jaguar", "Panthera onca", "Felidae", "Panthera", "onca", "Carnivora", "Mammalia", "True","Carnivoro","America",["Mexico","Belice","Honduras","Nicaragua","Costa Rica","Panama"]],
        2: ["Gorila de montaña", "Gorilla beringei", "Hominidae", "Gorilla", "beringei", "Primates", "Mammalia", "True","Heribivoro","Africa",["Uganda","Ruanda","Republica Democratica del congo"]]
    }

    
    for i in range(1,len(lista_animales)+1):
        id_animal = str(i)
        letra_animal= lista_animales[i][0][0]
        id_animal= id_animal + str (letra_animal)
        unique_id_animales.append(id_animal)
        nombre_animal=lista_animales[i][0]
        nombre_cientifico=lista_animales[i][1]
        familia=lista_animales[i][2]
        genero=lista_animales[i][3]
        especie=lista_animales[i][4]
        orden=lista_animales[i][5]
        clase=lista_animales[i][6]
        peligro_extincion=lista_animales[i][7]
        
        nombre_animal=nombre_animal.replace("'", "''")
        nombre_cientifico=nombre_cientifico.replace("'", "''")
        familia=familia.replace("'", "''")
        genero=genero.replace("'", "''")
        especie=especie.replace("'", "''")
        orden=orden.replace("'", "''")
        clase=clase.replace("'", "''")
        peligro_extincion=peligro_extincion.replace("'", "''")
        
        file.write(f"('{id_animal}','{nombre_animal}','{nombre_cientifico}','{familia}','{genero}','{especie}','{orden}','{clase}','{peligro_extincion}')")

        if i< len(lista_animales) :
            file.write(",\n")
        else:
            file.write(";\n")
print("El archivo de animales ha sido creado exitosamente")

#________________________________________________________________________________________________________________
## RUTA 1.1 ANIMALES UPDATE
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\animalesUpdate.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)

with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO animales (id_animal,nombre_animal,nombre_cientifico,familia,genero,especie,orden,clase,peligro_extincion)\nVALUES\n')
    
    esquilax_agrega = ["Esquilax", "Equus fictus", "Equidae", "Equus", "fictus", "Perissodactyla", "Mammalia", "False", "Herbívoro", "America", ["Canada", "Mexico", "Estados Unidos"]]

    
    id_animal = str(len(lista_animales)+1)
    letra_animal= esquilax_agrega[0][0]
    id_animal= id_animal + str (letra_animal)
    unique_id_animales_update=unique_id_animales.copy()
    unique_id_animales_update.append(id_animal)
    
    nombre_animal=esquilax_agrega[0]
    nombre_cientifico=esquilax_agrega[1]
    familia=esquilax_agrega[2]
    genero=esquilax_agrega[3]
    especie=esquilax_agrega[4]
    orden=esquilax_agrega[5]
    clase=esquilax_agrega[6]
    peligro_extincion=esquilax_agrega[7]
    
    nombre_animal=nombre_animal.replace("'", "''")
    nombre_cientifico=nombre_cientifico.replace("'", "''")
    familia=familia.replace("'", "''")
    genero=genero.replace("'", "''")
    especie=especie.replace("'", "''")
    orden=orden.replace("'", "''")
    clase=clase.replace("'", "''")
    peligro_extincion=peligro_extincion.replace("'", "''")
    
    file.write(f"('{id_animal}','{nombre_animal}','{nombre_cientifico}','{familia}','{genero}','{especie}','{orden}','{clase}','{peligro_extincion}')")

    if i< len(lista_animales) :
        file.write(",\n")
    else:
        file.write(";\n")
print("El archivo de animales ha sido actualizado exitosamente")

#________________________________________________________________________________________________________________
## RUTA 2 MEDICACION
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\medicacion.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)

with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO medicacion (id_medicamento,nombre_med)\nVALUES\n')
    
    lista_medicamentos= {
        1: ["Amoxicilina"],
        2: ["Ciprofloxacino"],
        3: ["Doxiciclina"]
    }
    
    for i in range(1,len(lista_medicamentos)+1):
        id_medicamento = str(i)
        letra_medicamento=lista_medicamentos[i][0][0]
        id_medicamento= id_medicamento + str(letra_medicamento)
        unique_id_medicamento.append(id_medicamento)
        nombre_med=lista_medicamentos[i][0]
        
        nombre_med=nombre_med.replace("'", "''")
        
        file.write(f"('{id_medicamento}','{nombre_med}')")

        if i < len(lista_medicamentos):
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo de medicamentos ha sido creado exitosamente")

#________________________________________________________________________________________________________________
## RUTA 3 BOLETO
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\boleto.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)

with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO boleto (id_boleto,precio,descripcion)\nVALUES\n')
    
    lista_boletos={
        1: ["N",10,"Personas Menores de 12 años"],
        2: ["J",50,"Personas Mayores de 12 años y menos de 60 años"],
        3: ["A",20,"Personas Mayores de 60 años"]
    }
    
    for i in range(1,len(lista_boletos)+1):
        id_boleto = str(i)
        id_boleto = id_boleto + str(lista_boletos[i][0])
        unique_id_boleto.append(id_boleto)
        precio =(lista_boletos[i][1])
        descripcion=lista_boletos[i][2]
        
        descripcion=descripcion.replace("'", "''")
        
        file.write(f"('{id_boleto}',{precio},'{descripcion}')")

        if i < len(lista_boletos):
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo de boletos ha sido creado exitosamente")

#________________________________________________________________________________________________________________
## RUTA 4 ZOOLOGICO
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\zoologico.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)

with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO zoologico (id_zoo,nombre,tamaño,presupuesto,estado,municipio,colonia,calle,cod_postal,espacios_animales,espacios_generales,espacios_administrativos,tipo_zoo)\nVALUES\n')


    lista_zoo={
        1: ["Zoologico de Chapultepec",17,31760000,"Ciudad de Mexico","Miguel Hidalgo","Bosque de Chapultepec","Chivatito","11850","Publico"],
        2: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        3: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        4: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        5: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        6: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        7: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        8: ["Zoologico de Chapultepec",17,31760000,"Ciudad de Mexico","Miguel Hidalgo","Bosque de Chapultepec","Chivatito","11850","Publico"],
        9: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        10: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        11: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        12: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        13: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        14: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        15: ["Zoologico de Chapultepec",17,31760000,"Ciudad de Mexico","Miguel Hidalgo","Bosque de Chapultepec","Chivatito","11850","Publico"],
        16: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        17: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        18: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        19: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        20: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        21: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        22: ["Zoologico de Chapultepec",17,31760000,"Ciudad de Mexico","Miguel Hidalgo","Bosque de Chapultepec","Chivatito","11850","Publico"],
        23: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        24: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        25: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        26: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        27: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        28: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        29: ["Zoologico de Chapultepec",17,31760000,"Ciudad de Mexico","Miguel Hidalgo","Bosque de Chapultepec","Chivatito","11850","Publico"],
        30: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        31: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        32: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        33: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        34: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        35: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        36: ["Zoologico de Chapultepec",17,31760000,"Ciudad de Mexico","Miguel Hidalgo","Bosque de Chapultepec","Chivatito","11850","Publico"],
        37: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        38: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        39: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        40: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        41: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        42: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        43: ["Zoologico de Chapultepec",17,31760000,"Ciudad de Mexico","Miguel Hidalgo","Bosque de Chapultepec","Chivatito","11850","Publico"],
        44: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        45: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        46: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        47: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        48: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        49: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        50: ["Zoologico de Chapultepec",17,31760000,"Ciudad de Mexico","Miguel Hidalgo","Bosque de Chapultepec","Chivatito","11850","Publico"],
        51: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        52: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        53: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        54: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        55: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        56: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        57: ["Zoologico de Chapultepec",17,31760000,"Ciudad de Mexico","Miguel Hidalgo","Bosque de Chapultepec","Chivatito","11850","Publico"],
        58: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        59: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        60: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        61: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        62: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        63: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        64: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        65: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
        66: ["Zoologico de San Juan de Aragon",15,26800000,"Ciudad de Mexico","Gustavo A. Madero","San Juan de Aragon","Jose Loreto Fabela","07920","Publico"],
    }

    for i in range(1,len(lista_zoo)+1):
        id_zoo = str(i)
        unique_id_zoo.append(id_zoo)
        nombre=lista_zoo[i][0]
        tamaño=lista_zoo[i][1]
        presupuesto=lista_zoo[i][2]
        estado=lista_zoo[i][3]
        municipio=lista_zoo[i][4]
        colonia=lista_zoo[i][5]
        calle=lista_zoo[i][6]
        cod_postal=lista_zoo[i][7]
        espacios_animales=random.randint(150,300)
        espacios_generales=random.randint(10,15)
        espacios_administrativos=random.randint(5,10)
        tipo_zoo=lista_zoo[i][8]
        
        nombre_med=nombre_med.replace("'", "''")
        estado=estado.replace("'", "''")
        municipio=municipio.replace("'", "''")
        colonia=colonia.replace("'", "''")
        calle=calle.replace("'", "''")
        tipo_zoo=tipo_zoo.replace("'", "''")
        
        file.write(f"('{id_zoo}','{nombre}',{tamaño},{presupuesto},'{estado}','{municipio}','{colonia}','{calle}','{cod_postal}',{espacios_animales},{espacios_generales},{espacios_administrativos},'{tipo_zoo}')")

        if i< len(lista_zoo) :
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo de zoo ha sido creado exitosamente")

#________________________________________________________________________________________________________________
## RUTA 5 ESPECIMEN
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\especimen.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)

with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO especimen (id_especie,id_animal,id_zoo,sexo,continente,pais,alimentacion,anio_nacimiento)\nVALUES\n')

    n_especie=0
    num_animales=len(lista_animales)+1 #Cantidad de animales (dividir 13000 entre esto para saber la cantidad de especies por animal)
    animales_por_zoo=7              #Cantidad de animales por zoologico (depende de dividir la cantidad de especies por animal en enteros)
    num_zoo=len(unique_id_zoo)      #Cantidad de zoo definida (66)
    residuos=animales_por_zoo*num_zoo   #Depende ded la division de animales,especies y zoo para saber la cantidad restante entera
    
    for i in range(1,num_animales):
            c=0
            for j in range(0,animales_por_zoo):
                for k in range(0,num_zoo):
                    n_especie=n_especie+1
                    id_especie = str(n_especie)
                    unique_id_especie.append(id_especie)
                    fk_id_animal_e=unique_id_animales[i-1]
                    fk_id_zoo_e=unique_id_zoo[k]
                    sexo=fake.sexo_especie()
                    alimentacion=lista_animales[i][8]
                    continente=lista_animales[i][9]
                    pais=random.choice(lista_animales[i][10])
                    año_nacimiento=random.randint(2000,2024)
        
                    sexo=sexo.replace("'", "''")
                    continente=continente.replace("'", "''")
                    pais=pais.replace("'", "''")
                    alimentacion=alimentacion.replace("'", "''")
                    c=c+1
                    file.write(f"('{id_especie}','{fk_id_animal_e}','{fk_id_zoo_e}','{sexo}','{continente}','{pais}','{alimentacion}','{año_nacimiento}')")
                    file.write(",\n")
            
            if c == residuos:
                for l in range(0,38):
                    n_especie=n_especie+1
                    id_especie = str(n_especie)
                    unique_id_especie.append(id_especie)
                    fk_id_animal_e=unique_id_animales[i-1]
                    fk_id_zoo_e=random.choice(unique_id_zoo)
                    sexo=fake.sexo_especie()
                    alimentacion=lista_animales[i][8]
                    continente=lista_animales[i][9]
                    pais=random.choice(lista_animales[i][10])
                    año_nacimiento=random.randint(2000,2024)
        
                    sexo=sexo.replace("'", "''")
                    continente=continente.replace("'", "''")
                    pais=pais.replace("'", "''")
                    alimentacion=alimentacion.replace("'", "''")
                    c=c+1
                    
                    file.write(f"('{id_especie}','{fk_id_animal_e}','{fk_id_zoo_e}','{sexo}','{continente}','{pais}','{alimentacion}','{año_nacimiento}')")
                    

                    if i < len(lista_animales)+1:
                        if 500 == c and i==len(lista_animales):
                            file.write(";\n")
                        else:
                            file.write(",\n")


print("El archivo de especies ha sido creado exitosamente")

#________________________________________________________________________________________________________________
## RUTA 5.1 ESPECIMEN UPDATE
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\especimenUpdate.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)

with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO especimen (id_especie,id_animal,id_zoo,sexo,continente,pais,alimentacion,anio_nacimiento)\nVALUES\n')

    n_especie=13000
    animales_por_zoo=15              #Cantidad de animales por zoologico (depende de dividir la cantidad de especies por animal en enteros)
    num_zoo=len(unique_id_zoo)      #Cantidad de zoo definida (66)
    residuos=animales_por_zoo*num_zoo   #Depende ded la division de animales,especies y zoo para saber la cantidad restante entera
    
    c=0
    for j in range(0,animales_por_zoo):
        for k in range(0,num_zoo):
            n_especie=n_especie+1
            id_especie = str(n_especie)
            fk_id_animal_e=unique_id_animales_update[-1]
            fk_id_zoo_e=unique_id_zoo[k]
            sexo=fake.sexo_especie()
            alimentacion=esquilax_agrega[8]
            continente=esquilax_agrega[9]
            pais=random.choice(esquilax_agrega[10])
            año_nacimiento=random.randint(2000,2024)
        
            sexo=sexo.replace("'", "''")
            continente=continente.replace("'", "''")
            pais=pais.replace("'", "''")
            alimentacion=alimentacion.replace("'", "''")
            c=c+1
            file.write(f"('{id_especie}','{fk_id_animal_e}','{fk_id_zoo_e}','{sexo}','{continente}','{pais}','{alimentacion}','{año_nacimiento}')")
            file.write(",\n")
            
        if c == residuos:
            for l in range(0,10):
                n_especie=n_especie+1
                id_especie = str(n_especie)
                fk_id_animal_e=unique_id_animales_update[-1]
                fk_id_zoo_e=random.choice(unique_id_zoo)
                sexo=fake.sexo_especie()
                alimentacion=esquilax_agrega[8]
                continente=esquilax_agrega[9]
                pais=random.choice(esquilax_agrega[10])
                año_nacimiento=random.randint(2000,2024)
        
                sexo=sexo.replace("'", "''")
                continente=continente.replace("'", "''")
                pais=pais.replace("'", "''")
                alimentacion=alimentacion.replace("'", "''")
                c=c+1
                    
                file.write(f"('{id_especie}','{fk_id_animal_e}','{fk_id_zoo_e}','{sexo}','{continente}','{pais}','{alimentacion}','{año_nacimiento}')")
                if l < 10:
                    if c==1000:
                        file.write(";\n")
                    else:
                        file.write(",\n")

print("El archivo de especies ha sido actualizado exitosamente")

#________________________________________________________________________________________________________________
## RUTA 6 TRATAMIENTO
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\tratamiento.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)

with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO tratamiento (id_tratamiento,id_especie,id_medicamento,estado)\nVALUES\n')
    
    
    for i in range(1,num_medicamentos+1):
        
        id_tratamiento = str(i)
        id_especie_t=combinacion_tratamiento_e(unique_id_especie,unique_id_tratamiento_combinacion_e)
        id_medicamento_t=combinacion_tratamiento_m(unique_id_medicamento,unique_id_tratamiento_combinacion_m)
        estado_t=fake.estado_tratamiento()
        
        estado_t=estado_t.replace("'", "''")
        
        file.write(f"('{id_tratamiento}','{id_especie_t}','{id_medicamento_t}','{estado_t}')")

        if i < num_medicamentos:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo de tratamientos ha sido creado exitosamente")


#________________________________________________________________________________________________________________
## RUTA 7 VENTAS
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\ventas.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)

with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO venta (id_venta,id_boleto,id_zoo,fecha,dia_semana)\nVALUES\n')
    
    
    for i in range(1,num_venta+1):
        id_venta = str(i)
        id_boleto_v=random.choice(unique_id_boleto)
        id_venta=id_venta + str(id_boleto_v[1])
        id_zoo_v=combinacion_venta_z(unique_id_zoo,unique_id_venta_combinacion_z)
        fecha_venta=fake.date_between(start_date=fecha_inicio,end_date=fecha_final)
        dia_semana=fake.dia_semana_v(fecha_venta)
        
        dia_semana=dia_semana.replace("'", "''")
        
        file.write(f"('{id_venta}','{id_boleto_v}','{id_zoo_v}','{fecha_venta}','{dia_semana}')")

        if i < num_venta:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo de ventas ha sido creado exitosamente")


#________________________________________________________________________________________________________________
## RUTA 8 ESTACIONAMIENTOS
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\estacionamientos.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)

with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO estacionamiento (id_estacionamiento,id_zoo,tamaño,numero)\nVALUES\n')
    
    fk_id_zoo_dicc={elemento: 0 for elemento in unique_id_zoo}
    
    for i in range(1,num_estacionamiento+1):
        id_estacionamiento = str(i)
        fk_id_zoo_e=combinacion_zoo_esta(unique_id_zoo,fk_id_zoo_dicc)
        tamaño_estacionamiento=random.randint(2000,100000)
        numero_estacionamiento=fk_id_zoo_dicc[fk_id_zoo_e]
        
        file.write(f"('{id_estacionamiento}','{fk_id_zoo_e}',{tamaño_estacionamiento},{numero_estacionamiento})")

        if i < num_estacionamiento:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo de estacionamiento sido creado exitosamente")

#_________________________________________________________________________________________________________________________________

#------------------------------------------------------------------------------------------------------------------------------
def merge_text_files(file_paths, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as input_file:
                output_file.write(input_file.read())
                output_file.write('\n\n\n')


# Lista de los nombres de los archivos de texto que quieres unir
file_paths = [r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\Codigo_Tablas_Zoo.txt", 
              r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\animales.txt", 
              r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\medicacion.txt",
              r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\boleto.txt",
              r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\zoologico.txt",
              r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\especimen.txt",
              r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\tratamiento.txt",
              r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\ventas.txt",
              r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\estacionamientos.txt"
              ]

file_paths_Update = [r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\animalesUpdate.txt", 
              r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\especimenUpdate.txt"
              ]

# Nombre del archivo de salida
output_file_path = r'C:\Users\danel_jaje6pg\Downloads\Zoologicos\BASE_DATOS_ZOO.txt'
output_file_path_Update = r'C:\Users\danel_jaje6pg\Downloads\Zoologicos\BASE_DATOS_Zoologico_UPDATE.txt'

#Llamar a la función para unir los archivos
merge_text_files(file_paths, output_file_path)
merge_text_files(file_paths_Update, output_file_path_Update)

print("¡Archivos unidos exitosamente!")

