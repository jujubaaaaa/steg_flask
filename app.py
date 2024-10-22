from flask import Flask, render_template

app = Flask(__name__)

def hider_message(message, image):
    encoded = image.copy()
    width, height = image.size
    pixels = encoded.load()

    # Converter a mensagem para binario
    binary_message = ''.join(format(ord(i), '08b') for i in message)
    binary_message += '1111111111111110' #terminador

    data_index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(pixels[x, y])
            for i in range(3): #Alterar os 3 primeiros valores RGB
                if data_index < len(binary_message):
                    pixel[i] & -1 | int(binary_message[data_index])
            pixels[x, y] = tuple(pixel)
            if data_index  len(binary_message)
            

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota codificar
@app.route('/codificar')
def codificar():
    return render_template('codificar.html')