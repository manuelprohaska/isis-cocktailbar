# Isi’s Cocktailbar – korrigierte Gäste-Version (Version 3)

## Inhalt
- `app.py`: Streamlit-Gäste-App, elegante Dunkel/Gold-Optik
- `recipes.json`: 56 als **Korrekt** oder **Korrigiert** markierte Rezepte
- `assets/`: bereinigte Cocktailfotos mit reinweißem Rand sowie Infotexte der Original-Screenshots
- `requirements.txt`, `.streamlit/config.toml`: Hosting-Konfiguration

14 in der Prüfung als **Entfernt** markierte Rezepte werden nicht angezeigt. Rezeptschritte und Zutaten stammen aus `isi_rezeptpruefung_v3.json`. Die Motive der originalen Rezeptfotos bleiben erhalten; störende Textreste am oberen oder unteren Bildrand sind weiß abgedeckt. Daten sind nach Prüfung unverändert übernommen; erklärende Automatik-Hinweise sind nicht Teil der Gästeanzeige.

## Start
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Bestehende Live-App aktualisieren
Die Live-App ist mit dem GitHub-Repository `manuelprohaska/isis-cocktailbar` verbunden. Die bereinigten Foto-Dateien sind SVG-Dateien im Ordner `assets/`.

1. ZIP entpacken. **Nicht das ZIP selbst** bei GitHub hochladen.
2. Im Repository auf dem Branch `main` über **Add file → Upload files** die entpackten Dateien `app.py` und `requirements.txt` hochladen. Falls die bereinigten Fotos noch fehlen, im Ordner `assets/` zusätzlich alle `photo_*.svg` hochladen.
3. Die Änderung mit **Commit changes** speichern. `app.py` bleibt die Hauptdatei.
4. Die Live-App erneut öffnen oder aktualisieren. Oben müssen **56 geprüfte Rezepte insgesamt** stehen.

Für ein neues, leeres Repository müssen zusätzlich `recipes.json`, `requirements.txt`, `assets/` und `.streamlit/config.toml` in derselben Ordnerstruktur hochgeladen werden. Die Datei `QA_SUMMARY.md` dient nur der Dokumentation.

## Bedienung
Auf Mobilgeräten Filter nach Spirituosen, Zutaten oder Cocktailname auswählen. „Rezept ansehen“ öffnet den Cocktail und scrollt automatisch zu dessen Rezept oberhalb der Cocktailkarte. Dort Menge skalieren und Zubereitung lesen. Der Surprise-Button zeigt sofort ein zufälliges Rezept aus den gefilterten Ergebnissen. Die Mengenliste skaliert; die freigegebenen Zubereitungsschritte beschreiben weiterhin einen Cocktail.

## Qualitäts- und Sicherheitshinweise
- Mengen aus der finalen Prüfdatei wurden **nicht eigenständig abgeändert**.
- Einige von der Nutzerprüfung freigegebene Listen nennen nicht alle Garnituren oder Alternativen separat; die Zubereitung enthält weitere Hinweise.
- Der B-52-Schritt aus den freigegebenen Daten enthält eine Anweisung zum Trinken brennender Flüssigkeit; die App ergänzt deswegen ausdrücklich einen Sicherheitshinweis, keine brennenden Getränke zu trinken.
- Keine Einkaufsliste und keine Bearbeitungsmöglichkeit für Gäste.
