# Exercice 3 : Manipulation de base des conteneurs

## 1. Vérifier la version de Docker

**Commande :**
```bash
docker --version
```

**Résultat :**
```
Docker version 28.4.0, build d8eb465
```

**Explication :** Cette commande vérifie que Docker est bien installé sur la machine.

---

## 2. Lister les images disponibles

**Commande :**
```bash
docker images
```

**Résultat :**
```
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
```

**Explication :** Cette commande affiche toutes les images Docker stockées localement. Au début, la liste est vide.

---

## 3. Télécharger l'image hello-world

**Commande :**
```bash
docker pull hello-world
```

**Résultat :**
```
Using default tag: latest
latest: Pulling from library/hello-world
198f93fd5094: Pull complete 
Digest: sha256:d4aaab6242e0cace87e2ec17a2ed3d779d18fbfd03042ea58f2995626396a274
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest
```

**Explication :** Cette commande télécharge l'image "hello-world" depuis Docker Hub (le registre officiel des images Docker).

---

## 4. Exécuter le conteneur hello-world

**Commande :**
```bash
docker run hello-world
```

**Résultat :**
```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

**Explication :** Cette commande crée et lance un conteneur à partir de l'image hello-world. Le conteneur affiche un message puis s'arrête automatiquement.

---

## 5. Lister les conteneurs actifs

**Commande :**
```bash
docker ps
```

**Résultat :**
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

**Explication :** Cette commande affiche uniquement les conteneurs en cours d'exécution. Le conteneur hello-world s'est déjà arrêté, donc la liste est vide.

---

## 6. Lister tous les conteneurs

**Commande :**
```bash
docker ps -a
```

**Résultat :**
```
CONTAINER ID   IMAGE         COMMAND    CREATED              STATUS                          PORTS     NAMES
f08db233f0a2   hello-world   "/hello"   About a minute ago   Exited (0) About a minute ago             tender_bassi

```

**Explication :** L'option `-a` affiche tous les conteneurs, y compris ceux qui sont arrêtés. On voit le conteneur hello-world avec le statut "Exited".

---

## 7. Supprimer un conteneur

**Commande :**
```bash
docker rm f08db233f0a2
```

**Résultat :**
```
f08db233f0a2
```

**Explication :** Cette commande supprime le conteneur arrêté. Docker affiche l'ID du conteneur supprimé pour confirmer.

---

## 8. Supprimer l'image hello-world

**Commande :**
```bash
docker rmi hello-world
```

**Résultat :**
```
Untagged: hello-world:latest
Deleted: sha256:d4aaab6242e0cace87e2ec17a2ed3d779d18fbfd03042ea58f2995626396a274
```

**Explication :** Cette commande supprime l'image hello-world du système. Il faut d'abord supprimer tous les conteneurs utilisant cette image.

---

## Conclusion

Toutes les commandes de base Docker ont été exécutées avec succès. L'exercice permet de comprendre le cycle de vie complet : téléchargement d'image → création de conteneur → nettoyage.