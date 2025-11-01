# 🧩 Projet Django - Stage NCA ROUIBA

Ce dépôt contient le code source du projet **Django** développé dans le cadre du stage à la société **NCA Rouiba**.  
Le projet repose sur **Django + MySQL**.

---

## 🚀 Installation du projet

### 1️⃣ Cloner le dépôt
```bash
git clone https://github.com/fritih-maya/stage_NCA-ROUIBA.git
cd stage_NCA-ROUIBA
```

### 2️⃣ Créer un environnement virtuel (fortement recommandé)
Sous Windows :
```bash
python -m venv venv
venv\Scripts\activate
```
Sous Linux / Mac :
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration de la base de données

Le projet utilise une base **MySQL** locale (`localhost`).  
Assurez-vous d’avoir MySQL (via **XAMPP**, **WAMP** ou **MySQL Server**) en cours d’exécution.

Ouvrez le fichier :
```
project_name/settings.py
```

Et configurez la section suivante :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nom_de_votre_base',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

## 🧱 Initialisation de la base
Exécutez les commandes suivantes :
```bash
python manage.py makemigrations
python manage.py migrate
```

Si vous avez des données de test :
```bash
python manage.py loaddata data.json
```

---

## 🧩 Lancement du serveur
Démarrez le serveur local Django :
```bash
python manage.py runserver
```

Le projet sera accessible à l’adresse :  
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧠 Fonctionnalités principales
- Gestion des utilisateurs et authentification  
- Connexion à la base MySQL locale  
---

## 🧰 Outils utilisés
- **Django 5**
- **MySQL / phpMyAdmin**
- **Python 3.12+**
- **Visual Studio Code** (éditeur recommandé)
- **Git & GitHub**

---

## 👩‍💻 Auteurs
**Maya Fritih** et **Souheil BENAMAR** 

---
