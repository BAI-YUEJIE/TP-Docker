# Exercice 5 : Déploiement d'une application Python Flask

## Fichiers créés

### 1. app.py
Application Flask simple qui affiche "Hello World".
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World from Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**Explication :** Cette application Flask crée un serveur web simple avec une seule route qui renvoie "Hello World from Flask!".

---

### 2. Dockerfile
Configuration Docker pour construire l'image Flask.
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY app.py .

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
```

**Explication :** 
- `FROM python:3.9-slim` : utilise une image Python légère
- `WORKDIR /app` : définit le répertoire de travail
- `COPY app.py .` : copie le fichier dans le conteneur
- `RUN pip install flask` : installe Flask
- `EXPOSE 5000` : expose le port 5000
- `CMD ["python", "app.py"]` : commande de démarrage

---

## Étapes d'exécution

### 1. Construction de l'image

**Commande :**
```bash
docker build -t flask-app .
```

**Résultat :**
```
[+] Building 12.6s (10/10) FINISHED                                                                                                                         docker:desktop-linux
 => [internal] load build definition from Dockerfile                                                                                                                        0.0s
 => => transferring dockerfile: 148B                                                                                                                                        0.0s
 => [internal] load metadata for docker.io/library/python:3.9-slim                                                                                                          1.9s
 => [auth] library/python:pull token for registry-1.docker.io                                                                                                               0.0s
 => [internal] load .dockerignore                                                                                                                                           0.0s
 => => transferring context: 2B                                                                                                                                             0.0s
 => [1/4] FROM docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13cf1731b1b                                                    5.8s
 => => resolve docker.io/library/python:3.9-slim@sha256:2d97f6910b16bd338d3060f261f53f144965f755599aab1acda1e13cf1731b1b                                                    0.0s
 => => sha256:ebfe7d4fa0c501a81a5ba6d1e1e2958e4b005d3ce3827b0adb869d47b8c51229 13.83MB / 13.83MB                                                                            3.2s
 => => sha256:c23f4b50347300e01a1a1da6dd0266adcf8e44671002ad28c2386cb6557943d6 251B / 251B                                                                                  0.3s
 => => sha256:479b8ad8bcc3edbeba82d4959dfbdc65226d5b55df3f36914c68455762bf924c 1.27MB / 1.27MB                                                                              0.8s
 => => sha256:a16e551192670581ec8359c70ab9eebf8f2af5468ffc79b3d4f9ce21b0366f47 30.14MB / 30.14MB                                                                            4.8s
 => => extracting sha256:a16e551192670581ec8359c70ab9eebf8f2af5468ffc79b3d4f9ce21b0366f47                                                                                   0.6s
 => => extracting sha256:479b8ad8bcc3edbeba82d4959dfbdc65226d5b55df3f36914c68455762bf924c                                                                                   0.0s
 => => extracting sha256:ebfe7d4fa0c501a81a5ba6d1e1e2958e4b005d3ce3827b0adb869d47b8c51229                                                                                   0.3s
 => => extracting sha256:c23f4b50347300e01a1a1da6dd0266adcf8e44671002ad28c2386cb6557943d6                                                                                   0.0s
 => [internal] load build context                                                                                                                                           0.0s
 => => transferring context: 215B                                                                                                                                           0.0s
 => [2/4] WORKDIR /app                                                                                                                                                      0.4s
 => [3/4] COPY app.py .                                                                                                                                                     0.0s
 => [4/4] RUN pip install flask                                                                                                                                             3.6s
 => exporting to image                                                                                                                                                      0.8s 
 => => exporting layers                                                                                                                                                     0.6s
 => => exporting manifest sha256:fc10e09910197cca8d337eb1240781edcb41921d878ed9b9244e513e81ad9921                                                                           0.0s
 => => exporting config sha256:477bb2e6cc9de5f2b052fdf2695864dd400a0480a7374089bab5509bfc3d19bb                                                                             0.0s
 => => exporting attestation manifest sha256:fc1846cee94a3b84a1481d78364b98a8102326e89198bd86dac8fd196a077d41                                                               0.0s
 => => exporting manifest list sha256:06ad4d68603418855f22a4383f43620bc0334470d27f44deaaed2cf36302401a                                                                      0.0s
 => => naming to docker.io/library/flask-app:latest                                                                                                                         0.0s
 => => unpacking to docker.io/library/flask-app:latest                                                                                                                      0.1s

View build details: docker-desktop://dashboard/build/desktop-linux/desktop-linux/2x5puf91nhn3ewxrqu3yzeiu3
```

**Explication :** Cette commande construit une image Docker nommée "flask-app" à partir du Dockerfile. Le processus prend environ 12 secondes.

---

### 2. Lancement du conteneur

**Commande :**
```bash
docker run -d -p 5001:5000 --name my-flask-app flask-app
```

**Résultat :**
```
c7903483080a53b08536ef1641f4f8d018b41af758af0ee9e3553099cb9b2190
```

**Explication :**
- `-d` : mode détaché (arrière-plan)
- `-p 5001:5000` : mappe le port 5001 local vers le port 5000 du conteneur (5000 était déjà occupé)
- `--name my-flask-app` : nom du conteneur
- Le conteneur renvoie son ID complet

---

### 3. Vérification du conteneur

**Commande :**
```bash
docker ps
```

**Résultat :**
```
CONTAINER ID   IMAGE       COMMAND           CREATED         STATUS         PORTS                                         NAMES
c7903483080a   flask-app   "python app.py"   9 seconds ago   Up 9 seconds   0.0.0.0:5001->5000/tcp, [::]:5001->5000/tcp   my-flask-app
```

**Explication :** Le conteneur est bien en cours d'exécution avec le mapping de ports 5001→5000.

---

### 4. Vérification des logs

**Commande :**
```bash
docker logs my-flask-app
```

**Résultat :**
```
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
```

**Explication :** Flask démarre correctement et écoute sur toutes les adresses (0.0.0.0).

---

### 5. Test dans le navigateur

**URL :** http://localhost:5001

**Résultat :** "Hello World from Flask!" affiché dans le navigateur.
![Page Hello World from Flask](hw-flask.png)

---

### 6. Arrêt et suppression du conteneur

**Commandes :**
```bash
docker stop my-flask-app
docker rm my-flask-app
```

**Résultat :**
```
my-flask-app
my-flask-app
```

**Explication :** Le conteneur est arrêté puis supprimé avec succès.

---

### 7. Vérification des images

**Commande :**
```bash
docker images
```

**Résultat :**
```
REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
flask-app    latest    06ad4d686034   15 minutes ago   228MB
nginx        latest    ca871a86d45a   9 days ago       244MB
```

**Explication :** L'image flask-app fait 228MB et est disponible pour être réutilisée.

---

## Notes importantes

- Le port 5000 était déjà utilisé par le processus ControlCenter (macOS), donc le port 5001 a été utilisé.
- L'image Python 3.9-slim fait environ 228MB, ce qui est léger pour une image Python complète.
- Flask affiche un avertissement car c'est un serveur de développement, pas de production.

---

## Conclusion

L'application Flask a été conteneurisée avec succès. Le Dockerfile permet de créer une image portable qui peut être déployée facilement. L'exercice démontre le cycle complet : build → run → test → stop → clean.