from flask import Flask
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

app = Flask(__name__)

# Connexion à MongoDB
try:
    client = MongoClient('mongodb://mongo:27017/', serverSelectionTimeoutMS=5000)
    # Test de connexion
    client.admin.command('ping')
    db = client['test_database']
    print("Connexion à MongoDB réussie!")
except ConnectionFailure:
    print("Échec de connexion à MongoDB")
    db = None

@app.route('/')
def hello():
    return "Flask + MongoDB - Application connectée!"

@app.route('/test')
def test_db():
    if db is None:
        return "Erreur: MongoDB non connecté", 500
    
    try:
        collection = db['test_collection']
        # Insérer un document
        result = collection.insert_one({'message': 'Test réussi', 'nombre': 42})
        # Compter les documents
        count = collection.count_documents({})
        return f"Document inséré! ID: {result.inserted_id}<br>Total documents: {count}"
    except Exception as e:
        return f"Erreur: {str(e)}", 500

@app.route('/data')
def show_data():
    if db is None:
        return "Erreur: MongoDB non connecté", 500
    
    try:
        collection = db['test_collection']
        documents = list(collection.find({}, {'_id': 0}).limit(10))
        return {'documents': documents, 'total': len(documents)}
    except Exception as e:
        return f"Erreur: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)