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