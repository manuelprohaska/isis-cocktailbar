# Isi’s Cocktailbar – 40 Cocktails zum 40er (Version 7)

Die App enthält genau 40 für die Feier ausgewählte Rezepte, 40 bereinigte Cocktailfotos und 38 Infotexte aus den Original-Screenshots. Die Cocktailkarte wird nach Namen sortiert, auch wenn weitere Rezepte später zur Datendatei hinzukommen. Die acht zuletzt gestrichenen Cocktails sind Jack and Coke, Between The Sheets, Buck’s Fizz, Gin Rickey, Highball, Mimosa, Screwdriver und Southside (Variante). Die zuvor auf Wunsch entfernten acht Rezepte bleiben ebenfalls ausgeschlossen.

## Bedienung

„Rezept ansehen“ öffnet den Cocktail und springt automatisch nach oben zum Rezept. „← Cocktailauswahl“ schließt das Rezept und springt zurück zum selben Cocktail in der Liste. Filter nach Spirituose, Zutat und Name sowie „Surprise me, Isi!“ bleiben verfügbar. Die frühere Zeile mit der Anzahl passender und geprüfter Cocktails ist entfernt.

## Start und Deployment

```bash
pip install -r requirements.txt
streamlit run app.py
```

Die Live-App ist mit dem GitHub-Repository `manuelprohaska/isis-cocktailbar` verbunden. Für einen manuellen Upload das ZIP entpacken und die enthaltenen Dateien und den Ordner `assets/` auf `main` hochladen; `app.py` bleibt die Hauptdatei. Der bestehende QR-Code führt weiterhin zur gleichen App-Adresse.

## Hinweise

Für Saftmengen werden abgefüllter Zitronen- und Limettensaft verwendet. Frische Früchte bleiben für Garnituren und die Caipirinha nötig. Beim Mai Tai verwenden wir 15 ml Cointreau statt orangenen Curaçao. Bei B-52 und Tequila Slammer weist die App auf sichere Handhabung hin. Die Einkaufsliste liegt separat vor und wird Gästen nicht angezeigt.

