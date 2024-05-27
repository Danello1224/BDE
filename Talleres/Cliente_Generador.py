from faker import Faker
from faker.providers import BaseProvider
import random
import os

class MexicoProvider(BaseProvider):
    def state(self):
        states = [
            "Ciudad de México",
            "Jalisco",
            "Nuevo León",
            "Puebla",
            "Hidalgo"
        ]
        return self.random_element(states)
    
    def municipality(self, state):
        municipalities = {
            "Ciudad de México": ["Coyoacán", "Iztapalapa", "Tlalpan", "Álvaro Obregón", "Benito Juárez"],
            "Jalisco": ["Guadalajara", "Zapopan", "Tlaquepaque", "Ameca", "Juchitlán"],
            "Nuevo León": ["Monterrey", "Guadalupe", "San Nicolás de los Garza", "Apodaca", "Santa Catarina"],
            "Puebla": ["Puebla", "Tehuacán", "Atlixco", "San Martín Texmelucan", "Cholula"],
            "Hidalgo": ["Actopan", "Cardonal", "Huichapan", "Pachuca de Soto", "Tula de Allende"]
        }
        return self.random_element(municipalities[state])
    
    def postal_code(self, municipality):
        postal_codes = {
            "Coyoacán": [4000, 4989],
            "Iztapalapa": [9000, 9989],
            "Tlalpan": [14000, 14989],
            "Álvaro Obregón": [1000,1900 ],
            "Benito Juárez": [3100, 3999],
            "Guadalajara": [44000, 44999],
            "Zapopan": [45000, 45499],
            "Tlaquepaque": [45500,45999 ],
            "Ameca": [46600, 46999],
            "Juchitlán": [46900,46999 ],
            "Monterrey": [64000,64999 ],
            "Guadalupe": [67100, 67199],
            "San Nicolás de los Garza": [66400,66499 ],
            "Apodaca": [66600,66699 ],
            "Santa Catarina": [66100,66199 ],
            "Puebla": [72000,72999 ],
            "Tehuacán": [75700,75799 ],
            "Atlixco": [74200, 74299],
            "San Martín Texmelucan": [74000,74999 ],
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

fake = Faker('es_MX')
fake.add_provider(MexicoProvider)

num_clients = 5170

ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Cliente.txt"

directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)

def genera_telefono():
    prefijo = fake.random_element(elements=('55', '56'))
    while True:
        sufijo = ''.join([str(fake.random_digit()) for _ in range(8)])
        if sufijo[0] != '0':
            break
    numero_telefono = prefijo + sufijo
    return numero_telefono

with open(ruta_completa, 'w', encoding='utf-8') as file:
    file.write('INSERT INTO cliente ("Id_Cliente", nombre_cte, ap_pat_cte, ap_mat_cte, corre_cte, telefono_cte, estado_cte, municipio_cte, colonia_cte, calle_cte, cod_postal_cte)\nVALUES\n')

    for i in range(1, num_clients + 1):
        id_cliente = str(i).zfill(5)  # Formato de ID con ceros a la izquierda
        nombre = fake.first_name()
        ap_pat = fake.last_name()
        ap_mat = fake.last_name()
        correo = fake.email()
        telefono = genera_telefono()
        estado = fake.state()
        municipio = fake.municipality(estado)
        colonia = fake.street_name()
        calle = fake.street_address()
        cod_postal = fake.postal_code(municipio)

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

        file.write(f"('{id_cliente}', '{nombre}', '{ap_pat}', '{ap_mat}', '{correo}', '{telefono}', '{estado}', '{municipio}', '{colonia}', '{calle}', '{cod_postal}')")

        if i < num_clients:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo ha sido creado exitosamente.")