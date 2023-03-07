# Librairie(s) utilisée(s)
from flask import *
import sqlite3


# Création d'un objet application web Flask
app = Flask(__name__)


def recuperer_stats(n):
    """Récupére les stats dans la table
    """
    connexion = sqlite3.connect("bdd/stats.db")
    curseur = connexion.cursor()
    requete_sql = """
    SELECT *
    FROM Stats as s
    WHERE s.Game = ?;"""
    resultat = curseur.execute(requete_sql,n)
    stats = resultat.fetchall()
    connexion.close()
    return stats


# Récupération des stats de la base de données SQLite
stats = recuperer_stats(str(1))

WIN = stats[0][1]
LANE = stats[0][2]
CHAMPION = stats[0][3]
KD = stats[0][4] / stats[0][5]

if WIN == "WIN":
    WIN = "Victoire"
else:
    WIN = "Défaite"

# Page utilisant une base de données
@app.route("/", methods=['GET', "POST"])
def accueillir():
    """Affiche un message dans le navigateur web"""
    if request.method == 'POST':
        Win = request.form['Win']
        Lane = request.form['Lane']
        Champion = request.form['Champion']
        Kills = request.form['Kills']
        Deaths = request.form['Deaths']
        
        connexion = sqlite3.connect("bdd/stats.db")
        c = connexion.cursor()
        requete_sql = """
        SELECT *
        FROM Stats as s
        WHERE s.Game = ?;"""
        c.execute(""" INSERT INTO Stats
        VALUES (15,?,?,?,?,?)""",(Win,Lane,Champion,Kills,Deaths))
        connexion.commit()
        connexion.close()
        
    # Transmission pour affichage
    return render_template("home.html",
                           WIN = WIN,
                           LANE = LANE,
                           CHAMPION = CHAMPION,
                           KD = KD)

# Page utilisant une base de données
@app.route("/ajout", methods=['GET',"POST"])
def ajout():
    """Affiche un message dans le navigateur web"""
    if request.method == 'POST':
        Win = request.form['Win']
        Lane = request.form['Lane']
        Champion = request.form['Champion']
        Kills = request.form['Kills']
        Deaths = request.form['Deaths']
        
        connexion = sqlite3.connect("bdd/stats.db")
        c = connexion.cursor()
        requete_sql = """
        SELECT *
        FROM Stats as s
        WHERE s.Game = ?;"""
        c.execute(""" INSERT INTO Stats
        VALUES (15,?,?,?,?,?)""",(Win,Lane,Champion,Kills,Deaths))
        connexion.commit()
        connexion.close()
        
    # Transmission pour affichage
    return render_template("ajout.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, debug=True)