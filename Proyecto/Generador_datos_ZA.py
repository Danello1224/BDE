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


### CODIGO PRINCIPAL
fake = Faker('es_MX')
fake.add_provider(DatabaseAZProvider)

num_vehiculos=450
num_personas=3000
num_visitantes=7000
num_ingresos=777

fecha_inicio=datetime.date(2010,1,31)
fecha_final=datetime.date(2024,5,31)

unique_id_vehiculo=set()
unique_id_persona=list()
unique_id_zona=list()

unique_id_combinacion_ingreso=set()
unique_id_combinacion_visita=set()
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
    file.write('INSERT INTO zona_arqueologica (id_zona)\nVALUES\n')
    
    lista_zona={
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0
    }
    
    for i in range(1,len(lista_zona)+1):
        id_zona = str(i)
        unique_id_zona.append(id_zona)
        
        file.write(f"('{id_zona}')")

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
        unique_id_persona.append(id_persona)
        nombre=fake.first_name()
        ap_pat=fake.last_name()
        ap_mat=fake.last_name()
        edad=random.randint(3,99)
        unique_dicc_edad[id_persona]=[edad]
        
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
    
    
    for i in range(1,num_visitantes+1):
        id_visitante = str(i)
        fk_id_zona_v=1
        fk_id_persona_v=1
        fecha_visita=fake.date_between(start_date=fecha_inicio,end_date=fecha_final)
        fecha_visitante.append(fecha_visita)
        monto_boleto="xd"
        
        file.write(f"('{id_visitante}','{fk_id_zona_v}','{fk_id_persona_v}','{fecha_visita}',{monto_boleto})")

        if i< num_visitantes:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo de visitante ha sido creado exitosamente")


#________________________________________________________________________________________________________________
## RUTA 4 VISITANTE
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\ProyectoBDE\ingreso.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
    
with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO ingeso (id_ingreso,id_zona,id_vehiculo,fecha_ingreso,precio_estacionamiento)\nVALUES\n')
    
    fecha_visitante_vehiculo=fecha_visitante.copy()
    
    for i in range(1,num_ingresos+1):
        id_ingreso = str(i)
        fk_id_zona_i=1
        fk_id_vehiculo_i=1
        fecha_ingreso=random.choice(fecha_visitante_vehiculo)
        fecha_visitante_vehiculo.remove(fecha_ingreso)
        precio_estacionamiento=70
        
        file.write(f"('{id_ingreso}','{fk_id_zona_i}','{fk_id_vehiculo_i}','{fecha_ingreso}',{precio_estacionamiento})")

        if i< num_visitantes:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo de ingreso ha sido creado exitosamente")

