#Bibliotecas 
from faker import Faker
from faker.providers import BaseProvider
import random
import os
#------------------------------------------------------------------------------
# Clase para datos
class MexicoProvider(BaseProvider):
    #definicion de estado
    def state(self):
        states = [
            "Ciudad de Mexico",
            "Jalisco",
            "Nuevo Leon",
            "Puebla",
            "Hidalgo"
        ]
        return self.random_element(states)
    
    #definicion de animal_Cte
    def animales_cte(self):
        animales = [
            "Perro",
            "Gato",
            "Canario",
            "Cuyo",
            "Perico",
            "Peces",
            "Esquilax"
        ]
        return self.random_element(animales)
    
    #definicion de bebida
    def bebida_cte(self):
        bebida =[
            "Jamaica",
            "Limon",
            "Piña"
        ]
        return self.random_element(bebida)
    
    #Definicion de municipio
    
    def municipality(self, state):
        municipalities = {
            "Ciudad de Mexico": ["Coyoacan", "Iztapalapa", "Tlalpan", "Alvaro Obregon", "Benito Juarez"],
            "Jalisco": ["Guadalajara", "Zapopan", "Tlaquepaque", "Ameca", "Juchitlan"],
            "Nuevo Leon": ["Monterrey", "Guadalupe", "San Nicolas de los Garza", "Apodaca", "Santa Catarina"],
            "Puebla": ["Puebla", "Tehuacan", "Atlixco", "San Martin Texmelucan", "Cholula"],
            "Hidalgo": ["Actopan", "Cardonal", "Huichapan", "Pachuca de Soto", "Tula de Allende"]
        }
        return self.random_element(municipalities[state])
    
    #Definicion de codigo postal
    def postal_code(self, municipality):
        postal_codes = {
            "Coyoacan": [4000, 4989],
            "Iztapalapa": [9000, 9989],
            "Tlalpan": [14000, 14989],
            "Alvaro Obregon": [1000,1900 ],
            "Benito Juarez": [3100, 3999],
            "Guadalajara": [44000, 44999],
            "Zapopan": [45000, 45499],
            "Tlaquepaque": [45500,45999 ],
            "Ameca": [46600, 46999],
            "Juchitlan": [46900,46999 ],
            "Monterrey": [64000,64999 ],
            "Guadalupe": [67100, 67199],
            "San Nicolas de los Garza": [66400,66499 ],
            "Apodaca": [66600,66699 ],
            "Santa Catarina": [66100,66199 ],
            "Puebla": [72000,72999 ],
            "Tehuacan": [75700,75799 ],
            "Atlixco": [74200, 74299],
            "San Martin Texmelucan": [74000,74999 ],
            "Cholula": [72700,72799],
            "Actopan": [42500,42599 ],
            "Cardonal": [42300,42399 ],
            "Huichapan": [42300,42399 ],
            "Pachuca de Soto": [42000,42999 ],
            "Tula de Allende": [42800,42899 ]
        }
        postal_code_range = postal_codes[municipality]
        postal_code = str(random.randint(postal_code_range[0], postal_code_range[1]))
        if len(postal_code) == 4:
            postal_code = '0' + postal_code
        return postal_code
    

#Genera telefono
def genera_telefono(estado):
    prefijos = {
        'Nuevo Leon': ['81'],
        'Ciudad de Mexico': ['55', '56'],
        'Jalisco': ['33', '341', '342', '343', '344', '345', '346', '347', '348', '349', '358'],
        'Puebla': ['222', '231', '232', '233', '248', '249', '276'],
        'Hidalgo': ['771', '772', '773', '774', '775', '778', '779']
    }
    
    if estado not in prefijos:
        raise ValueError("Estado no soportado")
    
    prefijo = fake.random_element(elements=prefijos[estado])
    
    while True:
        sufijo = ''.join([str(fake.random_digit()) for _ in range(10 - len(prefijo))])
        if sufijo[0] != '0':
            numero_telefono = prefijo + sufijo
            if numero_telefono not in unique_phone_numbers:
                unique_phone_numbers.add(numero_telefono)
                break
    return numero_telefono

#Genera correo
def genera_correo(nombre, apellido):
    correo_tipo =[
        "@gmail.com",
        "@hotmail.com",
        "@outlook.com",
        "@yahoo.com"
    ]
    dominio = random.choice(correo_tipo)
    base_correo = f"{nombre.lower()}.{apellido.lower()}"
    correo = f"{base_correo}{dominio}"
    sufijo = 1
    
    while correo in unique_emails:
        correo = f"{base_correo}{sufijo}{dominio}"
        sufijo += 1
        
    unique_emails.add(correo)
    return correo

#-------------------------------------------------------------------------------------------------------------
##Codigo principal
fake = Faker('es_MX')
fake.add_provider(MexicoProvider)

num_clients = 5

unique_phone_numbers = set()
unique_emails = set()
unique_id_cliente=set()

##RUTA 1 Cliente
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Talleres\Clientes.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
#Cliente 
with open(ruta_completa, 'w', encoding='utf-8') as file:
    file.write('INSERT INTO cliente ("Id_Cliente", nombre_cte, ap_pat_cte, ap_mat_cte, correo_cte, "telefono_cte", estado_cte, municipio_cte, colonia_cte, calle_cte, "cod_postal_cte",mascota_cte,bebida)\nVALUES\n')

    for i in range(1, num_clients + 1):
        id_cliente = str(i)
        unique_id_cliente.add(id_cliente)
        nombre = fake.first_name()
        ap_pat = fake.last_name()
        ap_mat = fake.last_name()
        correo = genera_correo(nombre, ap_pat)
        estado = fake.state()
        telefono = genera_telefono(estado)
        municipio = fake.municipality(estado)
        colonia = fake.street_name()
        calle = fake.street_address()
        cod_postal = fake.postal_code(municipio)
        mascota = fake.animales_cte()
        bebida = fake.bebida_cte()

        # Escapando comillas simples en los valores para evitar errores en SQL
        nombre = nombre.replace("'", "''")
        ap_pat = ap_pat.replace("'", "''")
        ap_mat = ap_mat.replace("'", "''")
        correo = correo.replace("'", "''")
        telefono = telefono.replace("'", "''")
        estado = estado.replace("'", "''")
        municipio = municipio.replace("'", "''")
        colonia = colonia.replace("'", "''")
        calle = calle.replace("'", "''")
        cod_postal = cod_postal.replace("'", "''")
        mascota = mascota.replace("'", "''")
        bebida = bebida.replace("'", "''")

        file.write(f"('{id_cliente}', '{nombre}', '{ap_pat}', '{ap_mat}', '{correo}', '{telefono}', '{estado}', '{municipio}', '{colonia}', '{calle}', '{cod_postal}','{mascota}','{bebida}')")

        if i < num_clients:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo de clientes sido creado exitosamente.")


##RUTA 2 Talleres
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Talleres\Taller.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
#Cliente 
with open(ruta_completa, 'w', encoding='utf-8') as file:
    file.write('INSERT INTO cliente ("Id_Cliente", nombre_cte, ap_pat_cte, ap_mat_cte, correo_cte, "telefono_cte", estado_cte, municipio_cte, colonia_cte, calle_cte, "cod_postal_cte",mascota_cte,bebida)\nVALUES\n')

    for i in range(1, num_clients + 1):
        id_cliente = str(i)
        unique_id_cliente.add(id_cliente)
        nombre = fake.first_name()
        ap_pat = fake.last_name()
        ap_mat = fake.last_name()
        correo = genera_correo(nombre, ap_pat)
        estado = fake.state()
        telefono = genera_telefono(estado)
        municipio = fake.municipality(estado)
        colonia = fake.street_name()
        calle = fake.street_address()
        cod_postal = fake.postal_code(municipio)
        mascota = fake.animales_cte()
        bebida = fake.bebida_cte()

        # Escapando comillas simples en los valores para evitar errores en SQL
        nombre = nombre.replace("'", "''")
        ap_pat = ap_pat.replace("'", "''")
        ap_mat = ap_mat.replace("'", "''")
        correo = correo.replace("'", "''")
        telefono = telefono.replace("'", "''")
        estado = estado.replace("'", "''")
        municipio = municipio.replace("'", "''")
        colonia = colonia.replace("'", "''")
        calle = calle.replace("'", "''")
        cod_postal = cod_postal.replace("'", "''")
        mascota = mascota.replace("'", "''")
        bebida = bebida.replace("'", "''")

        file.write(f"('{id_cliente}', '{nombre}', '{ap_pat}', '{ap_mat}', '{correo}', '{telefono}', '{estado}', '{municipio}', '{colonia}', '{calle}', '{cod_postal}','{mascota}','{bebida}')")

        if i < num_clients:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo ha sido creado exitosamente.")