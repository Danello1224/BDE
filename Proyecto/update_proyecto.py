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

### CODIGO PRINCIPAL
fake = Faker('es_MX')
fake.add_provider(DatabaseAZProvider)


#________________________________________________________________________________________________________________
## RUTA 1 ZONA_ARQUEOLOGICA UPDATE
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\ProyectoBDE\zona_arqueologica_Update.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)

with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('ALTER TABLE zona_arqueologica ADD COLUMN presupuesto_anual bigint;\n')
    
    
    for i in range(1,14):
        presupuesto=random.randint(1000000,50000000)
        file.write(f"UPDATE zona_arqueologica SET presupuesto_anual = {presupuesto} WHERE id_zona = '{i}';\n")

print("El archivo de zona ha sido actualizado exitosamente")
