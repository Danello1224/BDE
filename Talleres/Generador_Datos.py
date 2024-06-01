#Bibliotecas 
from faker import Faker
from faker.providers import BaseProvider
import random
import sys
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
    
    #define marca
    def marca_gen_c(self):
        marca_c =[
            "Audi",
            "Chevrolet",
            "Ferrari",
            "Aston Martin",
            "Honda",
            "Jaguar",
            "Jeep",
            "Kia",
            "Lamborguini",
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
    
    #define transmision
    def transmision_carro(self):
        trans=[
            "automatico",
            "estandar"
        ]
        return self.random_element(trans)
    
    #define marca_neumaticos
    def marca_neumaticos(self):
        mark_ne=[
            "Michelin",
            "Dunlop",
            "Continental",
            "Brigdestone",
            "Pirelli"
        ]
        return self.random_element(mark_ne)
    
    #define matricula
    def matricula_gen(self,unique_matricula):
        comprueba = True
        while comprueba:
            letters = ''.join(random.choices(string.ascii_uppercase, k=3))
            numbers = ''.join(random.choices(string.digits, k=3))
            mat=f'{letters}-{numbers}'
            if (mat) not in unique_matricula:
                comprueba= False
                break
        return mat
    
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

#-----------------------------------------------------------------------------------------------------------------------

def empleados_taller_cargo_union(combinacion_emp,combinacion_emp_tall,combinacion_emp_cartall):        
    asigna= True
    while asigna:
        rand = random.randint(1,15)
        rand2 = random.randint(1,13) 
        if combinacion_emp_tall[rand][1] != 0 and combinacion_emp [rand2][1] != 0:
            if combinacion_emp_cartall [(rand,rand2)][0] != 0:
                
                fk_id_taller = combinacion_emp_tall[rand][0]
                combinacion_emp_tall[rand][1] = combinacion_emp_tall[rand][1]-1
                
                fk_id_cargo = combinacion_emp[rand2][0]
                combinacion_emp[rand2][1]=combinacion_emp[rand2][1]-1
                
                combinacion_emp_cartall[(rand,rand2)][0]= combinacion_emp_cartall[(rand,rand2)][0]-1
                
                asigna = False
                break
    
    return fk_id_cargo,fk_id_taller

#____________________________________________________________________________________________________________________________________

#Define la lista de clientes por coche
def cliente_coche(unique_id_cliente,fk_cliente_lis):
    if len(fk_cliente_lis) > 0:
        datoc=random.choice(fk_cliente_lis)
        fk_cliente_lis.remove(datoc)
        return datoc
    else:
        datoc=random.choice(list(unique_id_cliente))
        return datoc
    
#define la lista de coches por reparacion
def coche_r(unique_id_coche,fk_coche_lis):
    if len(fk_coche_lis)>0:
        dator1=random.choice(fk_coche_lis)
        fk_coche_lis.remove(dator1)
        return dator1
    else:
        dator1=random.choice(list(unique_id_coche))
        return dator1

#define la lista de empleados por reparacion
def empleado_r(unique_id_empleado,fk_id_empleado):
    if len(fk_id_empleado)>0:
        dator2=random.choice(fk_id_empleado)
        fk_id_empleado.remove(dator2)
        return dator2
    else:
        dator2=random.choice(list(unique_id_empleado))
        return dator2

#-------------------------------------------------------------------------------------------------------------
##Codigo principal
fake = Faker('es_MX')
fake.add_provider(MexicoProvider)

num_clients = 5170
num_empleados = 11095
num_carros = 15505
num_arreglos = 23000

unique_phone_numbers = set()
unique_emails = set()
unique_id_cliente=set()
unique_id_cargo_empleado=[]
unique_id_taller=[]
unique_id_empleado=set()
unique_id_coche=set()
unique_matricula = set()


#___________________________________________________________________________________________________________________________________
##RUTA 1 Cliente
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Talleres\Clientes.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
#Cliente 
with open(ruta_completa, 'w', encoding='utf-8') as file:
    file.write('INSERT INTO cliente (id_cliente, nombre_cte, ap_pat_cte, ap_mat_cte, correo_cte, telefono_cte, estado_cte, municipio_cte, colonia_cte, calle_cte, cod_postal_cte)\nVALUES\n')

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

print("El archivo de clientes sido creado exitosamente.")



#___________________________________________________________________________________________________________________________________
##RUTA 1.1 Actualizado
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Talleres\ClientesUpdate.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
#Cliente ap_pat_cte
with open(ruta_completa, 'w', encoding='utf-8') as file:

    file.write(f"ALTER TABLE cliente ADD COLUMN mascota character varying (20);\n")
    file.write(f"ALTER TABLE cliente ADD COLUMN bebida character varying (20);\n")
    for i in range(1, num_clients + 1):
        mascota = fake.animales_cte()
        bebida = fake.bebida_cte()

        # Escapando comillas simples en los valores para evitar errores en SQL
        mascota = mascota.replace("'", "''")
        bebida = bebida.replace("'", "''")

        file.write(f"UPDATE cliente SET mascota = '{mascota}' WHERE id_cliente = '{i}';\n")
        file.write(f"UPDATE cliente SET bebida = '{bebida}' WHERE id_cliente = '{i}';\n")

print("El archivo de clientes ha sido actualizado exitosamente.")


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
        unique_id_cargo_empleado.append(id_cargo_empleado)
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
    file.write('INSERT INTO taller (Id_Taller,estado,municipio,colonia,calle,cod_postal,telefono)\nVALUES\n')


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
        id_taller = str(i)
        id_taller = id_taller + str("T")
        unique_id_taller.append(id_taller)
        dataT = Taller[i]
        estado,municipio,colonia,calle,cod_postal= dataT
        telefono = genera_telefono(estado)
        

        # Escapando comillas simples en los valores para evitar errores en SQL
        estado = estado.replace("'", "''")
        municipio = municipio.replace("'", "''")
        colonia = colonia.replace("'", "''")
        calle = calle.replace("'", "''")
        cod_postal = cod_postal.replace("'", "''")
        telefono = telefono.replace("'", "''")
        
        
        file.write(f"('{id_taller}', '{estado}','{municipio}','{colonia}','{calle}','{cod_postal}','{telefono}')")

        if i < 15:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo taller ha sido creado exitosamente.")



#_______________________________________________________________________________________________________________________________________________
##RUTA 3.1 Taller UPDATE
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Talleres\TalleresUpdate.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
#Taller 
with open(ruta_completa, 'w', encoding='utf-8') as file:
    
    file.write(f"ALTER TABLE taller ADD COLUMN color_fachada character varying (20);\n")
    for i in range(1,16):
        color_fachada = fake.fachada_taller()
        color_fachada = color_fachada.replace("'", "''")
    
        file.write(f"UPDATE taller SET color_fachada = '{color_fachada}' WHERE Id_Taller = '{i}T';\n")
print("El archivo taller ha sido actualizado exitosamente.")


#_______________________________________________________________________________________________________________________________________________
##RUTA 4 empleado
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Talleres\Empleado.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
#Empleado
with open(ruta_completa, 'w', encoding='utf-8') as file:
    file.write('INSERT INTO empleado (Id_Empleado,id_cargo,id_taller,nombre_emp,ap_pat_emp,ap_mat_emp,correo_emp,telefono_emp)\nVALUES\n')

#-------------- Generacion de listas para combinacion
    #Para cada cargo hay 
    Cantidad_Empleados =[4435,105,105,105,1110,1110,555,555,2220,225,225,120,225]
    
    if sum(Cantidad_Empleados) != num_empleados:
        print("Error en coincidencia de empleados 1 \n No se puede realizar archivo de empleados :(")
        sys.exit(1)
        
    valor=list(range(1,14))
    combinacion_emp = dict(zip(valor, [[u_id, cant] for u_id, cant in zip(unique_id_cargo_empleado, Cantidad_Empleados)]))
    
    #Para cada taller hay 
    empleados_taller=[740,740,740,740,740,740,740,740,740,740,739,739,739,739,739]
    if sum(empleados_taller) != num_empleados:
        print("Error en coincidencia de empleados 2 \n No se puede realizar archivo de empleados :(")
        sys.exit(1)
        
    valor_t=list(range(1,16))
    combinacion_emp_tall = dict(zip(valor_t,[[u_id2,cant2] for u_id2,cant2 in zip(unique_id_taller,empleados_taller)]))
    
    dicc_emp_tall={
        (1, 1): [296], (1, 2): [7], (1, 3): [7], (1, 4): [7], (1, 5): [74], (1, 6): [74], (1, 7): [37], (1, 8): [37], (1, 9): [148], (1, 10): [15], (1, 11): [15], (1, 12): [8], (1, 13): [15], 
        (2, 1): [296], (2, 2): [7], (2, 3): [7], (2, 4): [7], (2, 5): [74], (2, 6): [74], (2, 7): [37], (2, 8): [37], (2, 9): [148], (2, 10): [15], (2, 11): [15], (2, 12): [8], (2, 13): [15], 
        (3, 1): [296], (3, 2): [7], (3, 3): [7], (3, 4): [7], (3, 5): [74], (3, 6): [74], (3, 7): [37], (3, 8): [37], (3, 9): [148], (3, 10): [15], (3, 11): [15], (3, 12): [8], (3, 13): [15], 
        (4, 1): [296], (4, 2): [7], (4, 3): [7], (4, 4): [7], (4, 5): [74], (4, 6): [74], (4, 7): [37], (4, 8): [37], (4, 9): [148], (4, 10): [15], (4, 11): [15], (4, 12): [8], (4, 13): [15], 
        (5, 1): [296], (5, 2): [7], (5, 3): [7], (5, 4): [7], (5, 5): [74], (5, 6): [74], (5, 7): [37], (5, 8): [37], (5, 9): [148], (5, 10): [15], (5, 11): [15], (5, 12): [8], (5, 13): [15], 
        (6, 1): [296], (6, 2): [7], (6, 3): [7], (6, 4): [7], (6, 5): [74], (6, 6): [74], (6, 7): [37], (6, 8): [37], (6, 9): [148], (6, 10): [15], (6, 11): [15], (6, 12): [8], (6, 13): [15], 
        (7, 1): [296], (7, 2): [7], (7, 3): [7], (7, 4): [7], (7, 5): [74], (7, 6): [74], (7, 7): [37], (7, 8): [37], (7, 9): [148], (7, 10): [15], (7, 11): [15], (7, 12): [8], (7, 13): [15], 
        (8, 1): [296], (8, 2): [7], (8, 3): [7], (8, 4): [7], (8, 5): [74], (8, 6): [74], (8, 7): [37], (8, 8): [37], (8, 9): [148], (8, 10): [15], (8, 11): [15], (8, 12): [8], (8, 13): [15], 
        (9, 1): [296], (9, 2): [7], (9, 3): [7], (9, 4): [7], (9, 5): [74], (9, 6): [74], (9, 7): [37], (9, 8): [37], (9, 9): [148], (9, 10): [15], (9, 11): [15], (9, 12): [8], (9, 13): [15], 
        (10, 1): [296], (10, 2): [7], (10, 3): [7], (10, 4): [7], (10, 5): [74], (10, 6): [74], (10, 7): [37], (10, 8): [37], (10, 9): [148], (10, 10): [15], (10, 11): [15], (10, 12): [8], (10, 13): [15], 
        (11, 1): [295], (11, 2): [7], (11, 3): [7], (11, 4): [7], (11, 5): [74], (11, 6): [74], (11, 7): [37], (11, 8): [37], (11, 9): [148], (11, 10): [15], (11, 11): [15], (11, 12): [8], (11, 13): [15], 
        (12, 1): [295], (12, 2): [7], (12, 3): [7], (12, 4): [7], (12, 5): [74], (12, 6): [74], (12, 7): [37], (12, 8): [37], (12, 9): [148], (12, 10): [15], (12, 11): [15], (12, 12): [8], (12, 13): [15], 
        (13, 1): [295], (13, 2): [7], (13, 3): [7], (13, 4): [7], (13, 5): [74], (13, 6): [74], (13, 7): [37], (13, 8): [37], (13, 9): [148], (13, 10): [15], (13, 11): [15], (13, 12): [8], (13, 13): [15], 
        (14, 1): [295], (14, 2): [7], (14, 3): [7], (14, 4): [7], (14, 5): [74], (14, 6): [74], (14, 7): [37], (14, 8): [37], (14, 9): [148], (14, 10): [15], (14, 11): [15], (14, 12): [8], (14, 13): [15], 
        (15, 1): [295], (15, 2): [7], (15, 3): [7], (15, 4): [7], (15, 5): [74], (15, 6): [74], (15, 7): [37], (15, 8): [37], (15, 9): [148], (15, 10): [15], (15, 11): [15], (15, 12): [8], (15, 13): [15]
    }
    suma_total=0
    for key, value in dicc_emp_tall.items():
        suma_total += sum(value)
    if suma_total != num_empleados:
        print(f"La suma de los valores es {suma_total}, no de {num_empleados}.")
        sys.exit(1)
    
    

#-----------------------------------------------------
    for i in range(1,num_empleados+1):
        id_empleado = str(i)
        unique_id_empleado.add(id_empleado)
        
        fk_id_cargo,fk_id_taller=empleados_taller_cargo_union(combinacion_emp,combinacion_emp_tall,dicc_emp_tall)
            
        nombre = fake.first_name()
        ap_pat = fake.last_name()
        ap_mat = fake.last_name()
        correo = genera_correo(nombre, ap_pat)
        telefono = genera_telefono(estado)

        # Escapando comillas simples en los valores para evitar errores en SQL
        nombre = nombre.replace("'", "''")
        ap_pat = ap_pat.replace("'", "''")
        ap_mat = ap_mat.replace("'", "''")
        correo = correo.replace("'", "''")
        telefono = telefono.replace("'", "''")
        file.write(f"('{id_empleado}', '{fk_id_cargo}','{fk_id_taller}','{nombre}','{ap_pat}','{ap_mat}','{correo}','{telefono}')")

        if i < num_empleados:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo Empleados ha sido creado exitosamente.")




#_______________________________________________________________________________________________________________________________________________
##RUTA 4.1 empleado UPDATE
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Talleres\EmpleadoUpdate.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
#Empleado
with open(ruta_completa, 'w', encoding='utf-8') as file:
    
    file.write(f"ALTER TABLE empleado ADD COLUMN mascotas_emp character varying (20);\n")
    file.write(f"ALTER TABLE empleado ADD COLUMN anio_nacimiento char (4);\n")
    file.write(f"ALTER TABLE empleado ADD COLUMN alimento character varying (30);\n")

#-----------------------------------------------------
    for i in range(1,num_empleados+1):
        mascota_emp =fake.mascot_emp()
        Alimento=fake.alimentos_emp()
        Año_nacimiento= random.randint(1960,2000)

        # Escapando comillas simples en los valores para evitar errores en SQL
        mascota_emp =mascota_emp.replace("'", "''")
        Alimento=Alimento.replace("'", "''")
        
        file.write(f"UPDATE empleado SET mascotas_emp = '{mascota_emp}' WHERE Id_Empleado = '{i}';\n")
        file.write(f"UPDATE empleado SET alimento = '{Alimento}' WHERE Id_Empleado = '{i}';\n")
        file.write(f"UPDATE empleado SET anio_nacimiento = '{Año_nacimiento}' WHERE Id_Empleado = '{i}';\n")
        
print("El archivo Empleados ha sido actualizado exitosamente.")


#_______________________________________________________________________________________________________________________________________________
##RUTA 5 Coches
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Talleres\Coches.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
#Cliente 
with open(ruta_completa, 'w', encoding='utf-8') as file:
    file.write('INSERT INTO coche (Id_coche,id_cliente,matricula,marca)\nVALUES\n')
    
    fk_cliente_lis=list(unique_id_cliente)
    
    for i in range(1,num_carros+1):
        id_coche = str(i)
        unique_id_coche.add(id_coche)
        fk_id_cliente = cliente_coche(unique_id_cliente,fk_cliente_lis)
        matricula = fake.matricula_gen(unique_matricula)
        unique_matricula.add(matricula)
        marca = fake.marca_gen_c()
        
        # Escapando comillas simples en los valores para evitar errores en SQL
        matricula = matricula.replace("'", "''")
        marca = marca.replace("'", "''")
        
        file.write(f"('{id_coche}', '{fk_id_cliente}', '{matricula}', '{marca}')")

        if i < num_carros:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo Coches ha sido creado exitosamente.")





#_______________________________________________________________________________________________________________________________________________
##RUTA 5.1 Coches Update
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Talleres\CochesUpdate.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
#Cliente 
with open(ruta_completa, 'w', encoding='utf-8') as file:
        
    file.write(f"ALTER TABLE coche ADD COLUMN color character varying (20);\n")
    file.write(f"ALTER TABLE coche ADD COLUMN transmision character varying (20);\n")
    file.write(f"ALTER TABLE coche ADD COLUMN marca_neumaticos character varying (30);\n")
    
    
    for i in range(1,num_carros+1):
        color = fake.color_carro()
        transmision = fake.transmision_carro()
        marca_neumaticos = fake.marca_neumaticos()        
        
        # Escapando comillas simples en los valores para evitar errores en SQL
        color = color.replace("'", "''")
        transmision = transmision.replace("'", "''")
        marca_neumaticos = marca_neumaticos.replace("'", "''")
        
        file.write(f"UPDATE coche SET color = '{color}' WHERE Id_coche = '{i}';\n")
        file.write(f"UPDATE coche SET transmision = '{transmision}' WHERE Id_coche = '{i}';\n")
        file.write(f"UPDATE coche SET marca_neumaticos = '{marca_neumaticos}' WHERE Id_coche = '{i}';\n")

print("El archivo Coches ha sido actualizado exitosamente.")

#_______________________________________________________________________________________________________________________________________________
##RUTA 6 Reparaciones (Ultima por fin xd)
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Talleres\Reparaciones.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
#Cliente 
with open(ruta_completa, 'w', encoding='utf-8') as file:
    file.write('INSERT INTO reparacion (Id_reparacion,id_coche,id_empleado)\nVALUES\n')

    fk_id_coche=list(unique_id_coche)
    fk_id_empleado=list(unique_id_empleado)
    
    for i in range(1,num_arreglos+1):
        id_reparacion = str(i)
        id_coche_r=coche_r(unique_id_coche,fk_id_coche)
        id_empleado_r=empleado_r(unique_id_empleado,fk_id_empleado)
        
        file.write(f"('{id_reparacion}', '{id_coche_r}', '{id_empleado_r}')")


        if i < num_arreglos:
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo reparaciones ha sido creado exitosamente.")




#UNION DE ARCHIVOS


#------------------------------------------------------------------------------------------------------------------------------
def merge_text_files(file_paths, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as input_file:
                output_file.write(input_file.read())
                output_file.write('\n\n\n')


# Lista de los nombres de los archivos de texto que quieres unir
file_paths = [r"C:\Users\danel_jaje6pg\Downloads\Talleres\codigo_taller.txt", 
              r"C:\Users\danel_jaje6pg\Downloads\Talleres\Clientes.txt", 
              r"C:\Users\danel_jaje6pg\Downloads\Talleres\Cargo_Empleado.txt", 
              r"C:\Users\danel_jaje6pg\Downloads\Talleres\Talleres.txt", 
              r"C:\Users\danel_jaje6pg\Downloads\Talleres\Empleado.txt", 
              r"C:\Users\danel_jaje6pg\Downloads\Talleres\Coches.txt",
              r"C:\Users\danel_jaje6pg\Downloads\Talleres\Reparaciones.txt"
              ]

file_paths_Update = [r"C:\Users\danel_jaje6pg\Downloads\Talleres\ClientesUpdate.txt", 
              r"C:\Users\danel_jaje6pg\Downloads\Talleres\TalleresUpdate.txt", 
              r"C:\Users\danel_jaje6pg\Downloads\Talleres\EmpleadoUpdate.txt",
              r"C:\Users\danel_jaje6pg\Downloads\Talleres\CochesUpdate.txt" 
              ]

# Nombre del archivo de salida
output_file_path = r'C:\Users\danel_jaje6pg\Downloads\Talleres\BASE_DATOS_TALLER.txt'
output_file_path_Update = r'C:\Users\danel_jaje6pg\Downloads\Talleres\BASE_DATOS_TALLER_UPDATE.txt'

# Llamar a la función para unir los archivos
merge_text_files(file_paths, output_file_path)
merge_text_files(file_paths_Update, output_file_path_Update)

print("¡Archivos unidos exitosamente!")
