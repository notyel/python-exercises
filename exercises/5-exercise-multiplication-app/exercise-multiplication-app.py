import os

output_message = ""
base = 5
header_message = f"""
===========================================
        Tabla del {base}
===========================================\n
"""

for i in range(1, 11):
    output_message += f"{base} x {i} = {base * i}\n"

output_message = header_message + output_message
print(output_message)
output_path = "outputs"

os.makedirs(output_path, exist_ok=True)
with open(f"{output_path}/tabla-{base}.txt", "w") as file:
    file.write(output_message)

print("¡Archivo creado!")
