#Bibliotecas 
from faker import Faker
from faker.providers import BaseProvider
import random
import string
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
    
    #Definicion de mascota_emp
    def mascot_emp(self):
        masc=[
            "Perro",
            "Gato",
            "Canario"
        ]
        return self.random_element(masc)
    
    #Definicion de alimento
    def alimentos_emp(self):
        alim=[
            "Tacos al Pastor",
            "Enchiladas",
            "Sopes",
            "Ceviche",
            "Pozole",
            "Chiles en Nogada",
            "Quesadillas"
        ]
        return self.random_element(alim)
    
    #definicion de fachada
    def fachada_taller(self):
        color = [
            "Violeta",
            "Dorado",
            "Plateado",
            "Crema",
            "Borgoña",
            "Cian"
        ]
        return self.random_element(color)
    
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

num_clients = 5170
num_empleados = 110
num_carros = 15 

unique_phone_numbers = set()
unique_emails = set()
unique_id_cliente=set()
unique_id_cargo_empleado=set()
unique_id_taller=set()
unique_id_empleado=set()


#___________________________________________________________________________________________________________________________________
##RUTA 1 Cliente
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Talleres\Clientes.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
#Cliente 
with open(ruta_completa, 'w', encoding='utf-8') as file:
    file.write('INSERT INTO cliente (id_cliente, nombre_cte, ap_pat_cte, ap_mat_cte, correo_cte, telefono_cte, estado_cte, municipio_cte, colonia_cte, calle_cte, cod_postal_cte,mascota_cte,bebida)\nVALUES\n')

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

#_______________________________________________________________________________________________________________________________________________
##RUTA 2 Cargo_Empleado
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Talleres\Cargo_Empleado.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
#Cliente 
with open(ruta_completa, 'w', encoding='utf-8') as file:
    file.write('INSERT INTO cargo_empleado (Id_cargo,nombre_cargo)\nVALUES\n')
    
    Cargos_exist = [
        "Mecanico Automotriz",
        "Jefe de Taller",
        "Recepcionista de Taller",
        "Asesor Tecnico",
        "Especialista en Frenos y Suspension",
        "Especialista en  Sistemas Electricos",
        "Especialista en Transmisiones",
        "Mecanico de Carroceria y Pintura",
        "Auxiliar de Mecanico",
        "Especialista en Aire Acondicionado Automotriz",
        "Especialista en Neumaticos y Alineacion",
        "Gerente de Servicio",
        "Especialista en motores"
        ]

    for i in range(len(Cargos_exist)):
        id_cargo_empleado = str(i+1)
        id_cargo_empleado = id_cargo_empleado + str(random.randint(0,100))
        unique_id_cargo_empleado.add(id_cargo_empleado)
        nombre_cargo = Cargos_exist[i]
        
        # Escapando comillas simples en los valores para evitar errores en SQL
        nombre_cargo = nombre_cargo.replace("'", "''")
        file.write(f"('{id_cargo_empleado}', '{nombre_cargo}')")

        if i < len(Cargos_exist)-1:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo Cargo_Empleado ha sido creado exitosamente.")


#_______________________________________________________________________________________________________________________________________________
##RUTA 3 Taller
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Talleres\Talleres.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
#Taller 
with open(ruta_completa, 'w', encoding='utf-8') as file:
    file.write('INSERT INTO taller (Id_Taller,estado,municipio,colonia,calle,cod_postal,telefono,color_fachada)\nVALUES\n')


    Taller = {
                1 : ["Ciudad de Mexico", "Coyoacan", "Campestre Churubusco", "Cerro de Huitzilac 118", "04200"],
                2 : ["Ciudad de Mexico", "Iztapalapa", "San Juan Cerro", "Silicio 4", "09839"],
                3 : ["Ciudad de Mexico", "Tlalpan", "San Andres Totoltepec", "Cam. Viejo a San Pedro Martir 70", "14650"],
                4 : ["Jalisco", "Guadalajara", "Alamo Industrial", "Refineria 1605", "44490"],
                5 : ["Jalisco", "Zapopan", "Los Maestros", "Paulino Navarro 2040", "45150"],
                6 : ["Jalisco", "Zapopan", "Real Vallarta", "Leonardo Da Vinci 5058", "45020"],
                7 : ["Nuevo Leon", "Monterrey", "Centro", "Serafin Peña 745 Nte", "64000"],
                8 : ["Nuevo Leon", "San Nicolas de los Garza", "Los Puentes 2do Sector", "Av. Las Puentes 106", "66460"],
                9 : ["Nuevo Leon", "Apodaca", "Moderno Apodaca", "Padre Mier 601-A", "66600"],
                10 : ["Puebla", "Tehuacan", "Aquiles Serdan", "Calle 20 Nte 204", "75750"],
                11 : ["Puebla", "Puebla", "Resurgimiento Cd. Nte", "C.26 Nte. 408", "72370"],
                12 : ["Puebla", "Atlixco", "Revolucion", "Emiliano Zapata 1009", "74270"],
                13 : ["Hidalgo", "Pachuca de Soto", "Javier Rojo Gomez", "C. Agricultura 203", "42030"],
                14 : ["Hidalgo", "Pachuca de Soto", "Doctores", "Dr. Eliseo Ramirez Ulloa 1107", "42090"],
                15 : ["Ciudad de Mexico", "Benito Juarez", "Portales", "Emiliano Zapata Num. 184", "03300"]
            }

    
    for i in range(1,16):
        id_taller = str(i+1)
        id_taller = id_taller + str(random.randint(0,10))
        unique_id_taller.add(id_taller)
        dataT = Taller[i]
        estado,municipio,colonia,calle,cod_postal= dataT
        telefono = genera_telefono(estado)
        color_fachada = fake.fachada_taller()
        

        # Escapando comillas simples en los valores para evitar errores en SQL
        estado = estado.replace("'", "''")
        municipio = municipio.replace("'", "''")
        colonia = colonia.replace("'", "''")
        calle = calle.replace("'", "''")
        cod_postal = cod_postal.replace("'", "''")
        telefono = telefono.replace("'", "''")
        color_fachada = color_fachada.replace("'", "''")
        
        
        file.write(f"('{id_taller}', '{estado}','{municipio}','{colonia}','{calle}','{cod_postal}','{telefono}','{color_fachada}')")

        if i < 15:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo taller ha sido creado exitosamente.")


#_______________________________________________________________________________________________________________________________________________
##RUTA 4 empleado
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Talleres\Empleado.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
#Empleado
with open(ruta_completa, 'w', encoding='utf-8') as file:
    file.write('INSERT INTO empleado (Id_Empleado,id_cargo,id_taller,nombre_emp,ap_pat_emp,ap_mat_emp,correo_emp,telefono_emp,mascotas_emp,anio_nacimiento,alimento)\nVALUES\n')

    Cantidad_Empleados =[10,10,10,10,10,10,10,10,10,5,5,5,5]
    valor=list(range(1,14))
    combinacion_emp = dict(zip(valor, [[u_id, cant] for u_id, cant in zip(unique_id_cargo_empleado, Cantidad_Empleados)]))
    print(combinacion_emp)
    
    empleados_taller=[7,7,7,7,7,7,7,7,7,7,7,7,7,7,12]
    valor_t=list(range(1,16))
    combinacion_emp_tall = dict(zip(valor_t,[[u_id2,cant2] for u_id2,cant2 in zip(unique_id_taller,empleados_taller)]))
    print(combinacion_emp_tall)

    for i in range(1,num_empleados+1):
        id_empleado = str(i)
        unique_id_empleado.add(id_empleado)
        asigna = True
        while asigna:
            rand = random.randint(1,13)
            if combinacion_emp[rand][1] != 0:
                fk_id_cargo= combinacion_emp[rand][0]
                combinacion_emp[rand][1]= combinacion_emp[rand][1]-1
                asigna= False
                break
        
        asigna2 = True
        while asigna2:
            rand2 = random.randint(1,15)
            if combinacion_emp_tall[rand2][1] != 0:
                fk_id_taller= combinacion_emp_tall[rand2][0]
                combinacion_emp_tall[rand2][1]= combinacion_emp_tall[rand2][1]-1
                asigna2= False
                break
        nombre = fake.first_name()
        ap_pat = fake.last_name()
        ap_mat = fake.last_name()
        correo = genera_correo(nombre, ap_pat)
        telefono = genera_telefono(estado)
        mascota_emp =fake.mascot_emp()
        Alimento=fake.alimentos_emp()
        Año_nacimiento= random.randint(1960,2000)

        # Escapando comillas simples en los valores para evitar errores en SQL
        nombre = nombre.replace("'", "''")
        ap_pat = ap_pat.replace("'", "''")
        ap_mat = ap_mat.replace("'", "''")
        correo = correo.replace("'", "''")
        telefono = telefono.replace("'", "''")
        mascota_emp =mascota_emp.replace("'", "''")
        Alimento=Alimento.replace("'", "''")
        file.write(f"('{id_empleado}', '{fk_id_cargo}','{fk_id_taller}','{nombre}','{ap_pat}','{ap_mat}','{correo}','{telefono}','{mascota_emp}','{Año_nacimiento}','{Alimento}')")

        if i < num_empleados:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo Empleados ha sido creado exitosamente.")




