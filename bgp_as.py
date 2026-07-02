as_number = int(input("Ingrese el número de AS de BGP: "))

# Rangos privados según IANA:
# 16-bit: 64512 - 65534
# 32-bit: 4200000000 - 4294967294
if (64512 <= as_number <= 65534) or (4200000000 <= as_number <= 4294967294):
    print(f"El AS {as_number} es un AS PRIVADO.")
elif (1 <= as_number <= 64511) or (65536 <= as_number <= 4199999999):
    print(f"El AS {as_number} es un AS PÚBLICO.")
else:
    print(f"El AS {as_number} no es un número de AS válido.")