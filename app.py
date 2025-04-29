from flask import Flask, request, jsonify
from collections import Counter

app = Flask(__name__)

# Simulación de base de datos de interacciones
interacciones = {
    'user_1': ['motos', 'coches', 'coches', 'coches', 'moda', 'motos'],
    'user_2': ['moda', 'moda', 'coches']
}

@app.route('/recomendaciones', methods=['GET'])
def recomendaciones():
    user_id = request.args.get('user_id')
    gustos = interacciones.get(user_id, [])
    if not gustos:
        return jsonify({'mensaje': 'Sin interacciones, muestra contenido random'})
    
    contados = Counter(gustos)
    categorias_preferidas = [categoria for categoria, _ in contados.most_common(2)]
    return jsonify({'recomendado': categorias_preferidas})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
