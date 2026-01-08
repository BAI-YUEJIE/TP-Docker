# Exercice 4 : Création d'un serveur web avec Nginx

## 1. Télécharger l'image Nginx

**Commande :**
```bash
docker pull nginx
```

**Résultat :**
```
Using default tag: latest
latest: Pulling from library/nginx
0e794dd6ce7e: Pull complete 
eb6c73a28c57: Pull complete 
45f02391f163: Pull complete 
eac08499d0aa: Pull complete 
2ae15a201602: Pull complete 
3d3b30ae197f: Pull complete 
3276fb849f59: Pull complete 
Digest: sha256:ca871a86d45a3ec6864dc45f014b11fe626145569ef0e74deaffc95a3b15b430
Status: Downloaded newer image for nginx:latest
docker.io/library/nginx:latest
```

**Explication :** Cette commande télécharge l'image officielle Nginx depuis Docker Hub.

---

## 2. Lancer le conteneur Nginx

**Commande :**
```bash
docker run -d -p 8080:80 --name mon_nginx nginx
```

**Résultat :**
```
cd82f43092223b941c8a7bf9c676bb2bc2322d5ab27db9428f649d375ca81e22
```

**Explication :** 
- `-d` : lance le conteneur en arrière-plan (mode détaché)
- `-p 8080:80` : mappe le port 8080 de la machine locale vers le port 80 du conteneur
- `--name mon_nginx` : donne un nom au conteneur
- Le conteneur renvoie son ID complet

---

## 3. Vérifier le conteneur actif

**Commande :**
```bash
docker ps
```

**Résultat :**
```
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                     NAMES
cd82f4309222   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   mon_nginx
```

**Explication :** Le conteneur Nginx est bien en cours d'exécution. On voit le mapping de ports 8080→80.

---

## 4. Accéder à la page Nginx

**URL :** http://localhost:8080

**Résultat :** ![alt text](image.png)

**Explication :** Le serveur web Nginx est accessible via le navigateur sur le port 8080.

---

## 5. Arrêter le conteneur

**Commande :**
```bash
docker stop mon_nginx
```

**Résultat :**
```
mon_nginx
```

**Explication :** Cette commande arrête le conteneur en cours d'exécution. Docker affiche le nom du conteneur arrêté.

---

## 6. Supprimer le conteneur

**Commande :**
```bash
docker rm mon_nginx
```

**Résultat :**
```
mon_nginx
```

**Explication :** Cette commande supprime le conteneur arrêté. Il faut d'abord arrêter un conteneur avant de le supprimer.

---

## Conclusion

Le serveur web Nginx a été déployé avec succès dans un conteneur Docker. L'exercice démontre le mapping de ports et l'accès à un service web conteneurisé.