def convert_to_xbm(data):
    if len(data) != 8:
        raise ValueError("La lista debe contener exactamente 8 enteros.")
    
    xbm_data = []
    
    for row in range(8):
        byte = 0
        for col in range(8):
            # Extrae el bit correspondiente de cada columna y colócalo en la posición correcta del byte
            bit = (data[row] >> (7 - col)) & 1
            byte |= (bit << col)
        xbm_data.append(byte)
    
    return xbm_data

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Ejemplo de uso
input_data = [3, 4, 7, 22, 0b00010000, 0b00100000, 0b01000000, 0b10000000]


xbm_output = convert_to_xbm(input_data)

print("\nSalida:")
print_matrix([[int(digit) for digit in bin(byte)[2:].zfill(8)] for byte in xbm_output])  # Salida en forma de matriz
