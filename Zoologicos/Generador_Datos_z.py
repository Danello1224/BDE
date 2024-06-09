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
    
    def fachada_zoo(self):
        color = [
            "Violeta",
            "Dorado",
            "Plateado",
            "Crema",
            "Borgoña",
            "Cian"
        ]
        return self.random_element(color)
    
    def bebida_c(self):
        beber = [
            "Jamaica",
            "Limon",
            "Piña"
        ]
        return self.random_element(beber)
    
def comida_tipica(estado_act):
        comida = {
            'Durango': ['Caldillo Duranguense'],
            'Ciudad de Mexico': ['Tacos al Pastor'],
            'Nayarit': ['Tostadas de Mariscos'],
            'Chiapas': ['Tamal de Chipilín'],
            'Tabasco': ['Pejelagarto en Salsa'],
            'Nuevo Leon': ['Cabrito Asado'],
            'Puebla': ['Mole Poblano'],
            'Estado de Mexico': ['Barbacoa'],
            'Yucatan': ['Cochinita Pibil'],
            'Guanajuato': ['Enchiladas Mineras'],
            'Campeche': ['Pan de Cazón'],
            'San Luis Potosi': ['Enchiladas Potosinas'],
            'Sonora': ['Carne Asada'],
            'Guerrero': ['Pozole Guerrero'],
            'Tamaulipas': ['Tamales de Elote'],
            'Tlaxcala': ['Cecina'],
            'Queretaro': ['Gorditas de Migajas'],
            'Jalisco': ['Birria'],
            'Baja California': ['Fish Tacos'],
            'Coahuila': ['Asado de Puerco'],
            'Veracruz': ['Huachinango a la Veracruzana'],
            'Michoacan': ['Carnitas'],
            'Chihuahua': ['Chile Colorado'],
            'Sinaloa': ['Aguachile'],
            'Oaxaca': ['Mole Oaxaqueño'],
            'Quintana Roo': ['Pescado Tikin Xic'],
            'Zacatecas': ['Asado de Boda'],
            'Morelos': ['Cecina con Huevo'],
            'Colima': ['Ceviche de Sierra'],
            'Baja California Sur': ['Almejas Chocolatas']
        }
        comidar=comida[estado_act][0]
        return comidar 
        


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

num_venta = 15871
num_medicamentos = 6666
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

conjunto_estado=set()


#________________________________________________________________________________________________________________
## RUTA 1 ANIMALES
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\animales.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)
    
with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO animales (id_animal,nombre_animal,nombre_cientifico,familia,genero,especie,orden,clase,peligro_extincion)\nVALUES\n')
    
    lista_animales = {
        1: ["Jaguar", "Panthera onca", "Felidae", "Panthera", "onca", "Carnivora", "Mammalia", "True", "Carnívoro", "América", ["México", "Belice", "Honduras", "Nicaragua", "Costa Rica", "Panamá"]],
        2: ["Gorila de montaña", "Gorilla beringei", "Hominidae", "Gorilla", "beringei", "Primates", "Mammalia", "True", "Herbívoro", "África", ["Uganda", "Ruanda", "República Democrática del Congo"]],
        3: ["Elefante africano", "Loxodonta africana", "Elephantidae", "Loxodonta", "africana", "Proboscidea", "Mammalia", "True", "Herbívoro", "África", ["Botswana","Namibia","Sudafrica"]],
        4: ["León", "Panthera leo", "Felidae", "Panthera", "leo", "Carnivora", "Mammalia", "True", "Carnívoro", "África", ["Namibia","Tanzania","Kenia"]],
        5: ["Tigre de Bengala", "Panthera tigris tigris", "Felidae", "Panthera", "tigris", "Carnivora", "Mammalia", "True", "Carnívoro", "Asia", ["India", "Bangladesh", "Bután"]],
        6: ["Oso polar", "Ursus maritimus", "Ursidae", "Ursus", "maritimus", "Carnivora", "Mammalia", "True", "Carnívoro", "Ártico", ["Canadá", "Groenlandia", "Noruega"]],
        7: ["Panda gigante", "Ailuropoda melanoleuca", "Ursidae", "Ailuropoda", "melanoleuca", "Carnivora", "Mammalia", "True", "Herbívoro", "Asia", ["China"]],
        8: ["Cebra", "Equus quagga", "Equidae", "Equus", "quagga", "Perissodactyla", "Mammalia", "True", "Herbívoro", "África", ["Etiopia","Kenia"]],
        9: ["Rinoceronte blanco", "Ceratotherium simum", "Rhinocerotidae", "Ceratotherium", "simum", "Perissodactyla", "Mammalia", "True", "Herbívoro", "África", ["Sudafrica","Namibia","Zimbabwe","Kenia"]],
        10: ["Hipopótamo común", "Hippopotamus amphibius", "Hippopotamidae", "Hippopotamus", "amphibius", "Artiodactyla", "Mammalia", "True", "Herbívoro", "África", ["Botsuana","Zambia","Zimbabue"]],
        11: ["Girafa", "Giraffa camelopardalis", "Giraffidae", "Giraffa", "camelopardalis", "Artiodactyla", "Mammalia", "True", "Herbívoro", "África", ["Chad","Niger","Somalia"]],
        12: ["Leopardo", "Panthera pardus", "Felidae", "Panthera", "pardus", "Carnivora", "Mammalia", "True", "Carnívoro", "África", ["Sudafrica","Zambia"]],
        13: ["Lobo gris", "Canis lupus", "Canidae", "Canis", "lupus", "Carnivora", "Mammalia", "True", "Carnívoro", "América", ["Mexico","Estados Unidos"]],
        14: ["Puma", "Puma concolor", "Felidae", "Puma", "concolor", "Carnivora", "Mammalia", "True", "Carnívoro", "América", ["Belice","Costa Rica","El Salvador","Colombia","Guyana"]],
        15: ["Orangután", "Pongo", "Hominidae", "Pongo", "sp.", "Primates", "Mammalia", "True", "Frugívoro", "Asia", ["Indonesia", "Malasia"]],
        16: ["Oso pardo", "Ursus arctos", "Ursidae", "Ursus", "arctos", "Carnivora", "Mammalia", "True", "Carnívoro", "América", ["Estados Unidos","España","Francia"]],
        17: ["Koala", "Phascolarctos cinereus", "Phascolarctidae", "Phascolarctos", "cinereus", "Diprotodontia", "Mammalia", "True", "Herbívoro", "Australia", ["Australia"]],
        18: ["Panda rojo", "Ailurus fulgens", "Ailuridae", "Ailurus", "fulgens", "Carnivora", "Mammalia", "True", "Omnívoro", "Asia", ["Nepal", "Bután", "China"]],
        19: ["Canguro rojo", "Macropus rufus", "Macropodidae", "Macropus", "rufus", "Diprotodontia", "Mammalia", "True", "Herbívoro", "Australia", ["Australia"]],
        20: ["Tucán", "Ramphastos", "Ramphastidae", "Ramphastos", "sp.", "Piciformes", "Aves", "False", "Frugívoro", "América", ["Argentina","Paraguay","Surinam","Brasil","Peru"]],
        21: ["Cocodrilo del Nilo", "Crocodylus niloticus", "Crocodylidae", "Crocodylus", "niloticus", "Crocodylia", "Reptilia", "False", "Carnívoro", "África", ["Sudafrica","Tanzania","Estados Unidos"]],
        22: ["Halcón peregrino", "Falco peregrinus", "Falconidae", "Falco", "peregrinus", "Falconiformes", "Aves", "False", "Carnívoro", "Global", ["España","Australia","Gran Bretaña"]],
        23: ["Tortuga laúd", "Dermochelys coriacea", "Dermochelyidae", "Dermochelys", "coriacea", "Testudines", "Reptilia", "False", "Carnívoro", "Global", ["Guyana","Surinam","Trinidad y Tobago","Panama"]],
        24: ["Pinguino emperador", "Aptenodytes forsteri", "Aptenodytidae", "Aptenodytes", "forsteri", "Sphenisciformes", "Aves", "False", "Piscívoro", "Antártida", ["Antártida"]],
        25: ["Jirafa reticulada", "Giraffa camelopardalis reticulata", "Giraffidae", "Giraffa", "camelopardalis", "Artiodactyla", "Mammalia", "True", "Herbívoro", "África", ["Kenia", "Somalia", "Etiopía"]],
        26: ["Tortuga verde", "Chelonia mydas", "Cheloniidae", "Chelonia", "mydas", "Testudines", "Reptilia", "False", "Herbívoro", "Global", ["Canada","Mexico","Islas Galapagos"]]
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
    
    lista_medicamentos = {
        1: ["Amoxicilina"],
        2: ["Ciprofloxacino"],
        3: ["Doxiciclina"],
        4: ["Enrofloxacino"],
        5: ["Clindamicina"],
        6: ["Metronidazol"],
        7: ["Ivermectina"],
        8: ["Fenbendazol"],
        9: ["Praziquantel"],
        10: ["Albendazol"],
        11: ["Prednisona"],
        12: ["Dexametasona"],
        13: ["Ketoprofeno"],
        14: ["Meloxicam"],
        15: ["Tramadol"],
        16: ["Gabapentina"],
        17: ["Omeprazol"],
        18: ["Sucralfato"],
        19: ["Loperamida"],
        20: ["Bromhexina"],
        21: ["Difenhidramina"],
        22: ["Cefalexina"],
        23: ["Marbofloxacino"],
        24: ["Pentobarbital"],
        25: ["Fenitoína"],
        26: ["Amikacina"],
        27: ["Neomicina"],
        28: ["Sulfadiazina"],
        29: ["Trimetoprima"],
        30: ["Estradiol"]
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


    lista_zoo = {
    1: ["Zoologico de Chapultepec", 17, 31760000, "Ciudad de Mexico", "Miguel Hidalgo", "Bosque de Chapultepec", "Chivatito", "11850", "Publico"],
    2: ["Zoologico de San Juan de Aragon", 15, 26800000, "Ciudad de Mexico", "Gustavo A. Madero", "San Juan de Aragon", "Jose Loreto Fabela", "07920", "Publico"],
    3: ["Zoologico Los Coyotes", 11, 19000000, "Ciudad de Mexico", "Coyoacan", "Ex-Ejido de San Pablo Tepetlapa", "Escuela Naval Militar", "04900", "Publico"],
    4: ["Africam Safari", 200, 28000000, "Puebla", "Puebla", "Africam", "Carretera al Oasis 17302", "72960", "Privado"],
    5: ["Zoologico Guadalajara", 50, 7000000, "Jalisco", "Guadalajara", "Huetitan el Alto", "Calzada Independencia Norte", "44390", "Publico"],
    6: ["Zoologico de Morelia Benito Juarez", 35, 6000000, "Michoacan", "Tuxpan", "Felix Ireta", "Calzada Juarez S/N", "58070", "Publico"],
    7: ["Zoologico de Zacango", 32, 18000000, "Estado de Mexico", "Calimaya", "Santa Maria Nativitas", "Carretera Metepec", "52200", "Publico"],
    8: ["Zoologico del Altiplano", 13, 17000000, "Tlaxcala", "Apetitlan de Antonio Carvajal", "La Noria", "Carretera Apizaco-Tlaxcala", "90606", "Publico"],
    9: ["Bioparque Estrella", 300, 9000000, "Estado de Mexico", "Jilotepec", "Ixtlahuaca", "Carretera Jilotepec", "54340", "Privado"],
    10: ["Parque Zoologico La Pastora", 20, 10000000, "Nuevo Leon", "Guadalupe", "La Pastora", "Prolongacion Chapultepec", "67140", "Publico"],
    11: ["Parque Ecologico Ehecatl", 9, 15000000, "Estado de Mexico", "Ecatepec", "La Mora", "Av. Agricultura", "55030", "Publico"],
    12: ["Zoologico de Leon", 33, 6000000, "Guanajuato", "Leon", "El moral", "Blvd. Aeropuerto", "37670", "Publico"],
    13: ["Zoologico de Veracruz", 12, 19000000, "Veracruz", "Veracruz", "Ricardo Flores Magon", "Manuel Avila Camacho", "91900", "Privado"],
    14: ["Zoologico del Parque Morelos", 7, 8000000, "Baja California", "Tecate", "Zona Rio", "Gustavo Diaz Ordaz", "22010", "Publico"],
    15: ["Zoologico de Culiacan", 5, 3000000, "Sinaloa", "Culiacan", "Miguel Hidalgo", "Rolando Arjona Amabilis", "80127", "Publico"],
    16: ["Parque Zoologico de Saltillo", 7, 7000000, "Coahuila", "Saltillo", "La Nogalera", "Carretera Saltillo", "25050", "Publico"],
    17: ["Zoologico del Centenario", 9, 5000000, "Yucatan", "Merida", "Unidad Revolucion", "59 x Circuito Colonias", "97115", "Publico"],
    18: ["Zoologico Neptuno Zihuatanejo", 3, 7000000, "Guerrero", "Zihuatanejo", "Centro", "Vicente Guerrero", "40890", "Privado"],
    19: ["Zoologico Mundos Animales", 8, 5000000, "Jalisco", "Ocotlan", "Versalles", "Francisco Medina Ascencio", "48310", "Privado"],
    20: ["Zoologico de Aldama", 4, 4000000, "Chihuahua", "Juan Aldama", "Las Moras", "Granjas Camprestres del Bosque", "32900", "Privado"],
    21: ["Zoologico de Ciudad Obregon", 6, 7000000, "Sonora", "Ciudad Obregon", "Bellavista", "Rodolfo Elias Calles", "85070", "Privado"],
    22: ["Zoologico de Mexicali", 36, 13000000, "Baja California", "Mexicali", "Alvarado", "Nueva Esperanza", "21050", "Publico"],
    23: ["Zoologico Zoochilpan", 8, 5000000, "Guerrero", "Chilpancingo", "Jose Lopez Portillo", "Sta. Cruz", "39074", "Publico"],
    24: ["Interactive Zoo Cancun", 7, 6000000, "Quintana Roo", "Cancun", "La Isla", "Kukulcan 12.5", "77500", "Privado"],
    25: ["Zoologico de Nuevo Laredo", 5, 5000000, "Tamaulipas", "Nuevo Laredo", "Viveros", "Carretera Nacional Nuevo Laredo", "88000", "Publico"],
    26: ["Zoologico de Reinosa", 8, 4000000, "Tamaulipas", "Reynosa", "Ejido Los Cavazos", "Carretera Ribereña", "88614", "Privado"],
    27: ["Gran Zoologico Mazatlan : Mar de Cortes", 4, 2000000, "Sinaloa", "Mazatlan", "Telleria", "Av. de los Deportes", "82017", "Privado"],
    28: ["Zoologico Lira", 6, 13000000, "Coahuila", "Torreon", "La Perla", "Carretera Estatal", "27404", "Privado"],
    29: ["Recreativo Zoologico de San Jorge", 8, 17000000, "Chihuahua", "Juarez", "El Sauzal", "Mariano Abasolo", "32599", "Publico"],
    30: ["El Zoologico", 6, 9000000, "Estado de Mexico", "Ixtapaluca", "Santa Barbara", "Progreso S/N", "56538", "Privado"],
    31: ["Zoologico de Mexquitic", 6, 14000000, "San Luis Potosi", "Mexquitic", "Alvaro Obregon Supermanzana", "Lado Sur Presa", "78400", "Publico"],
    32: ["Pai Pai Ecotourism", 9, 10000000, "Baja California", "Ensenada", "Lazaro Cardenas", "La Bufadora", "22790", "Privado"],
    33: ["Santuario del Jaguar Zoologico Yaguar Xoo", 5, 12000000, "Oaxaca", "Tlacolula de Matamoros", "Crucero de Tanivet", "Carr.Internacional", "70403", "Privado"],
    34: ["Santuario De cocodrilos el cora", 4, 6000000, "Nayarit", "Nuevo Vallarta", "Bucerias", "Carretera Puerto Vallarta-Tepic", "63735", "Privado"],
    35: ["Parque Zoologico Benito Juarez", 25, 51000000, "Michoacan", "Morelia", "Feliz Ireta", "Calz. Juarez S/N", "58070", "Publico"],
    36: ["Zoologico La Encantada", 5, 20000000, "Zacatecas", "La Encantada", "Parque La Encantada", "Av. P la Encantada", "98088", "Publico"],
    37: ["Zoologico Tamatan", 56, 30000000, "Tamaulipas", "Altamira", "Sin nombre de Col 21", "Calz Gral Luis Caballero SN", "87060", "Publico"],
    38: ["Parque Zoologico de Tuxtla Gutierrez", 140, 15000000, "Chiapas", "Tuxtla Gutierres", "El Zapotal", "Calz. Cerro Hueco s/n", "29094", "Publico"],
    39: ["Zoologico de Monterrey", 70, 25000000, "Nuevo Leon", "Monterrey", "Colonia Obispado", "Ave. General Anaya", "64000", "Publico"],
    40: ["Zoologico de Tepic", 10, 8000000, "Nayarit", "Tepic", "Centro", "Calzada de la Cruz", "63000", "Publico"],
    41: ["Zoologico de Xalapa", 15, 12000000, "Veracruz", "Xalapa", "El tronconal", "Carretera antigua a Coatepec", "91193", "Publico"],
    42: ["Zoologico de Colima", 8, 10000000, "Colima", "Colima", "El Diezmo", "Carretera Colima Manzanillo", "28017", "Publico"],
    43: ["Zoologico de Campeche", 12, 7000000, "Campeche", "Campeche", "Frac. Bonanza", "Av. Patricio Trueba", "24014", "Publico"],
    44: ["Zoologico de La Paz", 10, 8000000, "Baja California Sur", "La Paz", "El Centenario", "Carretera a Los Planes", "23090", "Publico"],
    45: ["Zoologico de Tlaxcala", 7, 6000000, "Tlaxcala", "Tlaxcala", "Atlihuetzia", "Km. 1.5 Carretera Apizaco-Huamantla", "90620", "Publico"],
    46: ["Zoologico de Poza Rica", 10, 7000000, "Veracruz", "Poza Rica", "Lazaro Cardenas", "Prolongacion Puebla", "93210", "Publico"],
    47: ["Zoologico de Ciudad Victoria", 8, 5000000, "Tamaulipas", "Ciudad Victoria", "Villas de San Felipe", "Blvd. Tamaulipas", "87020", "Publico"],
    48: ["Zoologico de Chetumal", 6, 4000000, "Quintana Roo", "Chetumal", "Forjadores", "Av. Juventud", "77020", "Publico"],
    49: ["Zoologico de Cuernavaca", 12, 7000000, "Morelos", "Cuernavaca", "Buena Vista del Monte", "Carretera a Tepoztlan", "62180", "Publico"],
    50: ["Zoologico de Villahermosa", 15, 10000000, "Tabasco", "Villahermosa", "Atasta", "Periferico Carlos Pellicer", "86100", "Publico"],
    51: ["Zoologico de Oaxaca", 9, 6000000, "Oaxaca", "Oaxaca de Juarez", "Reforma", "5 de Mayo", "68000", "Publico"],
    52: ["Zoologico de Toluca", 18, 12000000, "Estado de Mexico", "Toluca", "San Pedro Totoltepec", "Camino viejo a San Mateo", "50220", "Publico"],
    53: ["Zoologico de Queretaro", 8, 5000000, "Queretaro", "Queretaro", "Cerrito Colorado", "Calle Trenes", "76090", "Publico"],
    54: ["Zoologico de Durango", 6, 6000000, "Durango", "Durango", "Fracc. Dolores", "Av. 20 de Noviembre","89000","Publico"],
    55: ["Zoologico de Tijuana", 20, 15000000, "Baja California", "Tijuana", "La Presa", "Blvd. Insurgentes", "22435", "Publico"],
    56: ["Zoologico de Acapulco", 15, 10000000, "Guerrero", "Acapulco", "Fracc. Las Playas", "Av. Costera Miguel Aleman", "39390", "Publico"],
    57: ["Zoologico de Puerto Vallarta", 10, 8000000, "Jalisco", "Puerto Vallarta", "Las Juntas", "Libramiento a Ixtapa", "48291", "Publico"],
    58: ["Zoologico de Tampico", 12, 9000000, "Tamaulipas", "Tampico", "Petrolera", "Av. Hidalgo", "89150", "Publico"],
    59: ["Zoologico de San Luis Potosi", 10, 8000000, "San Luis Potosi", "San Luis Potosi", "El Aguaje", "Carretera 57", "78216", "Publico"],
    60: ["Zoologico de Guaymas", 6, 5000000, "Sonora", "Guaymas", "El Cochorit", "Blvd. Beltrones", "85420", "Publico"],
    61: ["Zoologico de Coatzacoalcos", 8, 6000000, "Veracruz", "Coatzacoalcos", "Puente Morelos", "Av. Transistmica", "96400", "Publico"],
    62: ["Zoologico de Tapachula", 9, 7000000, "Chiapas", "Tapachula", "Fracc. Las Palmas", "Av. Insurgentes", "30700", "Publico"],
    63: ["Zoologico de Minatitlan", 7, 5000000, "Veracruz", "Minatitlan", "Santa Clara", "Av. Justo Sierra", "96750", "Publico"],
    64: ["Zoologico de Cuautla", 6, 5000000, "Morelos", "Cuautla", "Ruben Jaramillo", "Av. Emilio Vazquez Gomez", "62745", "Publico"],
    65: ["Zoologico de Tehuacan", 8, 6000000, "Puebla", "Tehuacan", "San Lorenzo Teotipilco", "Camino Real a San Diego Chalma", "75790", "Publico"],
    66: ["Zoologico de Los Mochis", 12, 9000000, "Sinaloa", "Los Mochis", "Fovisste", "Blvd. Antonio Rosales", "81258", "Publico"]
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
## RUTA 4.1 ZOOLOGICO UPDATE
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\zoologicoUpdate.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)

with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('ALTER TABLE zoologico ADD COLUMN comida_regional character varying ;\n')
    file.write('ALTER TABLE zoologico ADD COLUMN color_fachada character varying ;\n')
    
    
    for i in range(1,len(lista_zoo)+1):
        
        estado_a=lista_zoo[i][3]
        comida_tipica_estado=comida_tipica(estado_a)
        color_fachada=fake.fachada_zoo()

        comida_tipica_estado=comida_tipica_estado.replace("'", "''")
        
        file.write(f"UPDATE zoologico SET comida_regional = '{comida_tipica_estado}' WHERE id_zoo = '{i}';\n")
        file.write(f"UPDATE zoologico SET color_fachada = '{color_fachada}' WHERE id_zoo = '{i}';\n")
        

print("El archivo de medicamentos ha sido creado exitosamente")

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

#________________________________________________________________________________________________________________
## RUTA 9 Comida
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\comida.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)

with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO comida (id_tipo_puesto,comida)\nVALUES\n')
    
    lista_com={
        1: ["TP","Tacos al Pastor"],
        2: ["E","Enchiladas"],
        3: ["S","Sopes"],
        4: ["C","Ceviche"],
        5: ["P","Pozole"],
        6: ["CN","Chiles en Nogada"],
        7: ["Q","Quesadillas"]
    }
    
    for i in range(1,len(lista_com)+1):
        id_tipo_puesto = str(i)
        id_tipo_puesto = id_tipo_puesto + str(lista_com[i][0])
        comida_com=lista_com[i][1]
        
        comida_com=comida_com.replace("'", "''")
        
        file.write(f"('{id_tipo_puesto}','{comida_com}')")

        if i < len(lista_com):
            file.write(",\n")
        else:
            file.write(";\n")

print("El archivo de comida ha sido creado exitosamente")


#________________________________________________________________________________________________________________
## RUTA 10 VENTA COMIDA
ruta_completa = r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\venta_comida.txt"
directorio = os.path.dirname(ruta_completa)
if not os.path.exists(directorio):
    os.makedirs(directorio)

with open(ruta_completa,'w',encoding='utf-8') as file:
    file.write('INSERT INTO venta_comida (id_recinto,id_zoo,id_tipo_puesto,bebida)\nVALUES\n')
    
    
    for i in range(1,len(lista_zoo)+1):
        for j in range(1,len(lista_com)+1):
            id_recinto = str(i)
            id_recinto =id_recinto + "Z" + str(j)
            id_zoo_vc=str(i)
            id_tipo_puesto_vc=str(j)
            id_tipo_puesto_vc = id_tipo_puesto_vc + str(lista_com[j][0])
            bebida_venta=fake.bebida_c()
        
            bebida_venta=bebida_venta.replace("'", "''")
        
            file.write(f"('{id_recinto}','{id_zoo_vc}','{id_tipo_puesto_vc}','{bebida_venta}')")

            if i == len(lista_zoo):
                if j == len(lista_com):
                    file.write(";\n")
                else:
                    file.write(",\n") 
            else:
                file.write(",\n")

print("El archivo de venta_comida ha sido creado exitosamente")





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
              r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\estacionamientos.txt",
              r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\comida.txt",
              r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\venta_comida.txt"
              ]

file_paths_Update = [r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\animalesUpdate.txt", 
              r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\especimenUpdate.txt",
              r"C:\Users\danel_jaje6pg\Downloads\Zoologicos\zoologicoUpdate.txt"
              ]

# Nombre del archivo de salida
output_file_path = r'C:\Users\danel_jaje6pg\Downloads\Zoologicos\BASE_DATOS_ZOO.txt'
output_file_path_Update = r'C:\Users\danel_jaje6pg\Downloads\Zoologicos\BASE_DATOS_Zoologico_UPDATE.txt'

#Llamar a la función para unir los archivos
merge_text_files(file_paths, output_file_path)
merge_text_files(file_paths_Update, output_file_path_Update)

print("¡Archivos unidos exitosamente!")

