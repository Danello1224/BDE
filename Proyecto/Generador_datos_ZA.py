from faker import Faker
import random
import datetime
import string
import sys
import os
from faker.providers import BaseProvider

class DatabaseAZProvider(BaseProvider):
    
    #define marca
    def marca(self):
        marca_c =[
            "Audi",
            "Chevrolet",
            "Ferrari",
            "Aston Martin",
            "Honda",
            "Jaguar",
            "Jeep",
            "Kia",
            "Lamborghini",
            "Mercedes-Benz",
            "Nissan",
            "Porsche",
            "Tesla",
            "Toyota",
            "Volkswagen",
            "Mazda",
            "Chrysler",
            "Renault",
            "Alfa Romeo",
            "Bentley",
            "BMW",
            "Cadillac",
            "Dodge",
            "Ford",
            "Hyundai",
            "Koenigsegg",
            "Land Rover",
            "Maserati",
            "Peugeot",
            "Rimac",
            "SSC",
            "Subaru"
        ]
        return self.random_element(marca_c)
    
    #define modelo con base a marca
    def modelo(self,marca):
        marca_modelos = {
            "Audi": ["A3", "A4", "A6", "Q5", "Q7"],
            "Chevrolet": ["Malibu", "Camaro", "Silverado", "Equinox", "Tahoe"],
            "Ferrari": ["488 GTB", "Roma", "Portofino", "F8 Tributo", "SF90 Stradale"],
            "Aston Martin": ["DB11", "Vantage", "DBS Superleggera", "Rapide", "Valkyrie"],
            "Honda": ["Civic", "Accord", "CR-V", "Pilot", "Fit"],
            "Jaguar": ["XF", "XE", "F-Pace", "E-Pace", "I-Pace"],
            "Jeep": ["Wrangler", "Cherokee", "Grand Cherokee", "Renegade", "Compass"],
            "Kia": ["Sorento", "Sportage", "Optima", "Soul", "Telluride"],
            "Lamborghini": ["Huracán", "Aventador", "Urus", "Gallardo", "Murciélago"],
            "Mercedes-Benz": ["C-Class", "E-Class", "S-Class", "GLA", "GLE"],
            "Nissan": ["Altima", "Maxima", "Rogue", "Murano", "370Z"],
            "Porsche": ["911", "Cayenne", "Panamera", "Macan", "Taycan"],
            "Tesla": ["Model S", "Model 3", "Model X", "Model Y", "Cybertruck"],
            "Toyota": ["Corolla", "Camry", "RAV4", "Highlander", "Prius"],
            "Volkswagen": ["Golf", "Passat", "Tiguan", "Jetta", "Atlas"],
            "Mazda": ["Mazda3", "Mazda6", "CX-5", "CX-9", "MX-5 Miata"],
            "Chrysler": ["300", "Pacifica", "Voyager"],
            "Renault": ["Clio", "Megane", "Captur", "Kadjar", "Talisman"],
            "Alfa Romeo": ["Giulia", "Stelvio", "Giulietta", "4C", "8C Competizione"],
            "Bentley": ["Continental GT", "Bentayga", "Flying Spur", "Mulsanne"],
            "BMW": ["3 Series", "5 Series", "7 Series", "X3", "X5"],
            "Cadillac": ["CTS", "XT5", "Escalade", "CT6", "ATS"],
            "Dodge": ["Charger", "Challenger", "Durango", "Journey", "Grand Caravan"],
            "Ford": ["F-150", "Mustang", "Explorer", "Fusion", "Escape"],
            "Hyundai": ["Elantra", "Sonata", "Tucson", "Santa Fe", "Palisade"],
            "Koenigsegg": ["Agera", "Regera", "Jesko", "Gemera"],
            "Land Rover": ["Range Rover", "Discovery", "Defender", "Evoque", "Velar"],
            "Maserati": ["Ghibli", "Quattroporte", "Levante", "GranTurismo"],
            "Peugeot": ["208", "308", "3008", "508", "2008"],
            "Rimac": ["C_Two", "Concept_One"],
            "SSC": ["Tuatara"],
            "Subaru": ["Impreza", "Outback", "Forester", "Crosstrek", "WRX"]
            }
        return self.random_element(marca_modelos[marca])
        
    #define matricula
    def matricula(self,unique_matricula):
        comprueba = True
        while comprueba:
            letters = ''.join(random.choices(string.ascii_uppercase, k=3))
            numbers = ''.join(random.choices(string.digits, k=3))
            mat=f'{letters}-{numbers}'
            if (mat) not in unique_matricula:
                comprueba= False
                break
        return mat

    #define color_carro
    def color_carro(self):
        color_c=[
            "Violeta",
            "Dorado",
            "Plateado",
            "Crema",
            "Borgoña",
            "Cian"
        ]
        return self.random_element(color_c)
    

def zona_visitante_c(unique_id_persona,unique_id_zona,unique_id_combinacion_visita,comprueba_lista):
    asigna= True
    while asigna:
        persona_v=random.choice(unique_id_persona)
        zona_v=random.choice(unique_id_zona)
        if set(unique_id_persona) == comprueba_lista:
            if persona_v in unique_id_combinacion_visita:
                if len(unique_id_combinacion_visita[persona_v]) < 3:
                    if unique_id_combinacion_visita[persona_v].count(zona_v) < 3:
                        unique_id_combinacion_visita[persona_v].append(zona_v)
                        asigna= False
                        break
        else:
            if persona_v not in comprueba_lista:
                comprueba_lista.add(persona_v)
                unique_id_combinacion_visita[persona_v].append(zona_v)
                asigna= False
                break
    return persona_v,zona_v

def zona_vehiculo_c(unique_id_vehiculo,lista_visitas_vehiculo,lista_comprueba_v):
    asigna= True
    while asigna:
        if unique_id_vehiculo == list(lista_comprueba_v):
            vehiculo=random.choice(unique_id_vehiculo)
            zona_z=random.randint(1,13)
            if lista_visitas_vehiculo[zona_z][0]>0:
                asigna= False
                break
        else:
            vehiculo=random.choice(unique_id_vehiculo)
            zona_z=random.randint(1,13)
            if vehiculo not in lista_comprueba_v:
                lista_comprueba_v.add(vehiculo)
                
    return vehiculo,zona_z

def monto_boleto_e(unique_dicc_edad,fk_id_persona_v):
    precio=0
    edad=unique_dicc_edad[fk_id_persona_v][0]
    if edad > 3.00 and edad < 14.01:
        precio=20
        return precio
    elif edad > 14.00 and edad < 18.01:
        precio=25
        return precio
    elif edad > 18.00 and edad < 25.01:
        precio=30
        return precio
    elif edad > 25.00 and edad < 35.01:
        precio=40
        return precio
    elif edad > 35.00 and edad < 75.01:
        precio=60
        return precio
    elif edad > 75.00 and edad < 99.01:
        precio=20
        return precio
    
        



### CODIGO PRINCIPAL
fake = Faker('es_MX')
fake.add_provider(DatabaseAZProvider)

num_vehiculos=450
num_personas=3000
num_visitantes=7000
num_ingresos=777

fecha_inicio=datetime.date(2010,1,31)
fecha_final=datetime.date(2024,5,31)

unique_id_vehiculo=list()
unique_id_persona=list()
unique_id_zona=list()

unique_id_combinacion_ingreso=set()
unique_matricula=set()

unique_dicc_edad=dict()

fecha_visitante=list()




#________________________________________________________________________________________________________________
## RUTA 1 VEHICULO
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\ProyectoBDE\vehiculos.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
    
with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO vehiculo (id_vehiculo,marca,modelo,no_placa,color)\nVALUES\n')
    

    
    for i in range(1,num_vehiculos+1):
        id_vehiculo = str(i)
        unique_id_vehiculo.append(int(id_vehiculo))
        marca=fake.marca()
        modelo=fake.modelo(marca)
        no_placa=fake.matricula(unique_matricula)
        color=fake.color_carro()
        
        marca=marca.replace("'", "''")
        modelo=modelo.replace("'", "''")
        color=color.replace("'", "''")
        
        file.write(f"('{id_vehiculo}','{marca}','{modelo}','{no_placa}','{color}')")

        if i< num_vehiculos:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo de vehiculos ha sido creado exitosamente")

#________________________________________________________________________________________________________________
## RUTA 2 ZONA ARQUEOLOGICA
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\ProyectoBDE\zona_arqueologica.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
    
with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO zona_arqueologica (id_zona,nombre,estado,municipio)\nVALUES\n')
    
    lista_zona={
        1: ["Cañada de la virgen","Guanajuato","San Miguel de Abasolo"],
        2: ["Peralta","Guanajuato","Abasolo"],
        3: ["Plazuelas","Guanajuato","Penjamo"],
        4: ["Tula","Hidalgo","Tula de Allende"],
        5: ["Xihuingo","Hidalgo","Tepeapulco"],
        6: ["Huapalcalco","Hidalgo","Tulancingo de Bravo"],
        7: ["Guachimontones","Jalisco","Teuchitlan"],
        8: ["Ixtepete","Jalisco","Zapopan"],
        9: ["El Grillo","Jalisco","Zapopan"],
        10: ["El Cerrito","Queretaro","Corregidora"],
        11: ["Ranas","Queretaro","San Joaquin"],
        12: ["Toluquilla","Queretaro","Cadereyta de Montes"],
        13: ["Tancama","Queretaro","Jalpan de Serra"]
    }
    
    for i in range(1,len(lista_zona)+1):
        id_zona = str(i)
        unique_id_zona.append(int(id_zona))
        nombre_z=lista_zona[int(id_zona)][0]
        estado_z=lista_zona[int(id_zona)][1]
        municipio_z=lista_zona[int(id_zona)][2]
        
        nombre_z=nombre_z.replace("'", "''")
        estado_z=estado_z.replace("'", "''")
        municipio_z_z=municipio_z.replace("'", "''")
        
        file.write(f"('{id_zona}','{nombre_z}','{estado_z}','{municipio_z}')")

        if i< len(lista_zona):
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo de zona ha sido creado exitosamente")


#________________________________________________________________________________________________________________
## RUTA 3 ZONA PERSONA
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\ProyectoBDE\persona.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
    
with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO persona (id_persona,nombre,ap_pat,ap_mat,edad)\nVALUES\n')
    
    for i in range(1,num_personas+1):
        id_persona = str(i)
        unique_id_persona.append(int(id_persona))
        nombre=fake.first_name()
        ap_pat=fake.last_name()
        ap_mat=fake.last_name()
        edad_anios=random.randint(3,99)
        
        if edad_anios== 3:
            edad_meses=((random.randint(1,11))/100)
        elif edad_anios ==99:
            edad_meses=0.00
        else:
            edad_meses=((random.randint(0,11))/100)

        edad=edad_anios+edad_meses
        unique_dicc_edad[int(id_persona)]=[edad]
        
        nombre=nombre.replace("'", "''")
        ap_pat=ap_pat.replace("'", "''")
        ap_mat=ap_mat.replace("'", "''")
        
        file.write(f"('{id_persona}','{nombre}','{ap_pat}','{ap_mat}',{edad})")

        if i< num_personas:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo de persona ha sido creado exitosamente")


#________________________________________________________________________________________________________________
## RUTA 4 VISITANTE
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\ProyectoBDE\visitante.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
    
with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO visitante (id_visitante,id_zona,id_persona,fecha_visita,monto_boleto)\nVALUES\n')
    
    unique_id_combinacion_visita= {numero:[] for numero in unique_id_persona}
    comprueba_lista=set()
    
    lista_visitas={
        1: [0],
        2: [0],
        3: [0],
        4: [0],
        5: [0],
        6: [0],
        7: [0],
        8: [0],
        9: [0],
        10: [0],
        11: [0],
        12: [0],
        13: [0]
    }

    
    for i in range(1,num_visitantes+1):
        id_visitante = str(i)
        fk_id_persona_v,fk_id_zona_v=zona_visitante_c(unique_id_persona,unique_id_zona,unique_id_combinacion_visita,comprueba_lista)
        fecha_visita=fake.date_between(start_date=fecha_inicio,end_date=fecha_final)
        fecha_visitante.append(fecha_visita)
        monto_boleto=monto_boleto_e(unique_dicc_edad,fk_id_persona_v)
        
        lista_visitas[fk_id_zona_v][0]=lista_visitas[fk_id_zona_v][0]+1
        
        file.write(f"('{id_visitante}','{fk_id_zona_v}','{fk_id_persona_v}','{fecha_visita}',{monto_boleto})")

        if i< num_visitantes:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo de visitante ha sido creado exitosamente")
#________________________________________________________________________________________________________________
## RUTA 5 INGRESO
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\ProyectoBDE\ingreso.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
    
with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO ingreso (id_ingreso,id_zona,id_vehiculo,fecha_ingreso,precio_estacionamiento)\nVALUES\n')
    
    fecha_visitante_vehiculo=fecha_visitante.copy()
    
    lista_visitas_vehiculo=lista_visitas.copy()
    lista_comprueba_v=set()
    
    for i in range(1,num_ingresos+1):
        id_ingreso = str(i)
        fk_id_vehiculo_i,fk_id_zona_i=zona_vehiculo_c(unique_id_vehiculo,lista_visitas_vehiculo,lista_comprueba_v)
        fecha_ingreso=random.choice(fecha_visitante_vehiculo)
        fecha_visitante_vehiculo.remove(fecha_ingreso)
        precio_estacionamiento=70
        
        file.write(f"('{id_ingreso}','{fk_id_zona_i}','{fk_id_vehiculo_i}','{fecha_ingreso}',{precio_estacionamiento})")

        if i< num_ingresos:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo de ingreso ha sido creado exitosamente")

#------------------------------------------------------------------------------------------------------------------------------
def merge_text_files(file_paths, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as input_file:
                output_file.write(input_file.read())
                output_file.write('\n\n\n')


# Lista de los nombres de los archivos de texto que quieres unir
file_paths = [r"C:\Users\danel_jaje6pg\Downloads\ProyectoBDE\Codigo_Tablas_Zona.txt",
              r"C:\Users\danel_jaje6pg\Downloads\ProyectoBDE\vehiculos.txt", 
              r"C:\Users\danel_jaje6pg\Downloads\ProyectoBDE\zona_arqueologica.txt",
              r"C:\Users\danel_jaje6pg\Downloads\ProyectoBDE\persona.txt",
              r"C:\Users\danel_jaje6pg\Downloads\ProyectoBDE\visitante.txt",
              r"C:\Users\danel_jaje6pg\Downloads\ProyectoBDE\ingreso.txt"
              ]


# Nombre del archivo de salida
output_file_path = r"C:\Users\danel_jaje6pg\Downloads\ProyectoBDE\BASE_PROYECTO.txt"

#Llamar a la función para unir los archivos
merge_text_files(file_paths, output_file_path)

print("¡Archivos unidos exitosamente!")

