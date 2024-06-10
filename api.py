import tkinter as tk;#Crear una interfaz gráfica mediante python
import requests;
from io import BytesIO;#Para poder trabajar con datos binarios
from PIL import Image, ImageTk;
import json;

def buscar_pokemon():
    nombre_pokemon = entry_pokemon.get().lower();
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}";
    response = requests.get(url);#Solicitud get a la API mediante request

    if response.status_code == 200: #La solicitud fue exitosa
        data = response.json();
        #datos del pokémon
        nombre = data["name"];
        numero = data["id"];
        tipos = [tipo["type"]["name"]for tipo in data["types"]];
        resultado = f"Nombre: {nombre}\n Número: {numero}\n Tipo(s): {', '.join(tipos)}";
        
        imagen_url = data["sprites"]["front_default"];
        response_imagen = requests.get(imagen_url);
        imagen = Image.open(BytesIO(response_imagen.content));
        imagen = imagen.resize((200,200), Image.Resampling.LANCZOS);#redimensionar imágen a una medida de 200x200 píxeles
        foto = ImageTk.PhotoImage(imagen);#Convirtiendo la imágen en un objeto PhotoImage
        label_imagen.config(image=foto);
        label_imagen.image = foto;

        #Generar un archivo con los datos del pokémon
        with open(f"{nombre}.txt", "w") as archivo:
            archivo.write(resultado);
        #Crear un diccionario con los datos del pokémon

        datos_pokemon = {
            "nombre": nombre,
            "numero": numero,
            "tipos": tipos,
            "imagen_url": imagen_url
        }

        with open(f"{nombre}.json", "w") as archivo_json:
            json.dump(datos_pokemon, archivo_json);#escribimos los datos del pokémon en el archivo json

        label_resultado.config(text="Archivo Ok");
    else:
        resultado = "No se encontró el pokémon";
        label_imagen.config(image=None);
        label_resultado.config(text=resultado);

#Ventana tk
window = tk.Tk();
window.title("Buscador de pokémon");

label_pokemon = tk.Label(window, text="Ingresa el nombre del Pokémon");
label_pokemon.pack();

entry_pokemon = tk.Entry(window);
entry_pokemon.pack();

button_buscar = tk.Button(window, text="Buscar", command=buscar_pokemon);
button_buscar.pack();

label_resultado = tk.Label(window, text="");
label_resultado.pack();

label_imagen = tk.Label(window);
label_imagen.pack();

window.mainloop();















