# Isi’s Cocktailbar – Einkaufsauswahl für 10 Gäste (Version 5)

## Inhalt
- `app.py`: Streamlit-Gäste-App, elegante Dunkel/Gold-Optik
- `recipes.json`: 49 für die Feier ausgewählte Rezepte
- `assets/`: bereinigte Cocktailfotos mit reinweißem Rand sowie vollständige Infotexte der Original-Screenshots
- `requirements.txt`, `.streamlit/config.toml`: Hosting-Konfiguration

14 in der Rezeptprüfung als **Entfernt** markierte Rezepte werden nicht angezeigt. Zusätzlich wurden auf Wunsch sechs Cocktails wegen Apfelschnaps, Crème de Cassis, Scotch Whisky, Roggenwhisky und Rotwein gestrichen. Bee’s Knees entfällt wegen Honig. Für die übrigen 49 Cocktails wird abgefüllter Zitronen- und Limettensaft zum Mixen eingeplant; frische Zitrusfrüchte bleiben für Stücke, Scheiben, Zesten, Twists und die Caipirinha nötig. Beim Between The Sheets entspricht die frühere halbe Zitrone nun ungefähr 20 ml Zitronensaft. Die Motive der originalen Rezeptfotos bleiben erhalten; störende Textreste am oberen oder unteren Bildrand sind weiß abgedeckt.

## Start
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Bestehende Live-App aktualisieren
Die Live-App ist mit dem GitHub-Repository `manuelprohaska/isis-cocktailbar` verbunden. Die 49 bereinigten Foto-Dateien und 47 vollständigen Infotexte sind SVG-Dateien im Ordner `assets/`.

1. ZIP entpacken. **Nicht das ZIP selbst** bei GitHub hochladen.
2. Im Repository auf dem Branch `main` über **Add file → Upload files** die entpackten Dateien `app.py`, `recipes.json`, `requirements.txt`, `.streamlit/config.toml` und den gesamten Ordner `assets/` in derselben Ordnerstruktur hochladen. Bestehende gleichnamige Dateien überschreiben.
3. Die Änderung mit **Commit changes** speichern. `app.py` bleibt die Hauptdatei.
4. Die Live-App erneut öffnen oder aktualisieren. Oben müssen **49 geprüfte Rezepte insgesamt** stehen. Margarita und Tequila Sunrise zeigen unter „Über diesen Cocktail“ den vollständigen Absatz.

Die Datei `QA_SUMMARY.md` dient nur der Dokumentation.

## Bedienung
Auf Mobilgeräten Filter nach Spirituosen, Zutaten oder Cocktailname auswählen. „Rezept ansehen“ öffnet den Cocktail und scrollt automatisch zu dessen Rezept oberhalb der Cocktailkarte. Dort Menge skalieren und Zubereitung lesen. Der Surprise-Button zeigt sofort ein zufälliges Rezept aus den gefilterten Ergebnissen. Die Mengenliste skaliert; die freigegebenen Zubereitungsschritte beschreiben weiterhin einen Cocktail.

## Qualitäts- und Sicherheitshinweise
- Die freigegebenen Mengen bleiben erhalten, außer der ausdrücklich gewünschten Umstellung beim Between The Sheets auf ungefähr 20 ml Zitronensaft statt einer halben Zitrone.
- Einige von der Nutzerprüfung freigegebene Listen nennen nicht alle Garnituren oder Alternativen separat; die Zubereitung enthält weitere Hinweise.
- Der B-52-Schritt aus den freigegebenen Daten enthält eine Anweisung zum Trinken brennender Flüssigkeit; die App ergänzt deswegen ausdrücklich einen Sicherheitshinweis, keine brennenden Getränke zu trinken.
- Keine Einkaufsliste und keine Bearbeitungsmöglichkeit für Gäste.

