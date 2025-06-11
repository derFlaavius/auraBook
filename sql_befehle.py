import klassen
import sql_connector

# === Personenliste laden ===
def personen_laden():
    conn = sql_connector.verbinde_db()
    if conn is None:
        return [], 1
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM person ORDER BY name ASC")
        pliste = cursor.fetchall()
        conn.close()
        print(pliste)
        return pliste, 0
    except Exception as e:
        print(f"Fehler beim Laden der Personen: {e}")
        conn.close()
        return [], 1

# === Einzelne Person + Verlauf laden ===
def person_laden(pid):
    conn = sql_connector.verbinde_db()
    if conn is None:
        return None, 2
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT name, aurapunkte FROM person WHERE id = ?", (pid,))
        row = cursor.fetchone()
        if row is None:
            return None, 1

        person = klassen.Person()
        person.id = pid
        person.name = row[0]
        person.aura = row[1]
        person.rang_festlegen()

        cursor.execute("SELECT datum, kontobewegung, kommentar FROM eintraege WHERE name_id = ?", (pid,))
        daten = cursor.fetchall()

        # 🔽 Jetzt sortieren wir die Liste — neuester Eintrag zuerst
        daten.sort(key=lambda x: x[0], reverse=True)

        person.ereignisse = daten
        conn.close()
        return person, 0
    except Exception as e:
        print(f"Fehler beim Laden der Person: {e}")
        conn.close()
        return None, 2


# === Neue Person hinzufügen ===
def person_anlegen(name):
    conn = sql_connector.verbinde_db()
    if conn is None:
        return 2
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM person WHERE name = ?", (name,))
        if cursor.fetchone() is not None:
            conn.close()
            return 1  # Name existiert bereits
        cursor.execute("INSERT INTO person (name, aurapunkte) VALUES (?, 0)", (name,))
        conn.commit()
        conn.close()
        return 0
    except Exception as e:
        print(f"Fehler beim Anlegen der Person: {e}")
        conn.close()
        return 2

# === Eintrag hinzufügen + Aura aktualisieren ===
def person_bearbeiten(eintrag, person):
    conn = sql_connector.verbinde_db()
    if conn is None:
        return 1
    try:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO eintraege (name_id, datum, kontobewegung, kommentar) VALUES (?, ?, ?, ?)",
            (person.id, eintrag.datum, eintrag.pkt, eintrag.kommentar)
        )
        cursor.execute(
            "UPDATE person SET aurapunkte = aurapunkte + ? WHERE id = ?",
            (eintrag.pkt, person.id)
        )
        conn.commit()
        conn.close()
        return 0
    except Exception as e:
        print(f"Fehler bei der Bearbeitung: {e}")
        conn.close()
        return 1