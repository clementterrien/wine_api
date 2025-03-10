from database import SessionLocal

# Test de connexion
try:
    db = SessionLocal()
    print("Connexion à MySQL réussie !")
    db.close()
except Exception as e:
    print("Erreur de connexion :", e)