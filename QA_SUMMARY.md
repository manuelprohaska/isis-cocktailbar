# Finale Rezeptprüfung

Quelle: `isi_rezeptpruefung_v3.json`, Format `isi-recipe-review-v3`

- 70 geprüft
- 41 Korrekt
- 15 Korrigiert
- 14 Entfernt
- 56 aktiv

Es werden ausschließlich die 56 aktiven Rezepte ausgeliefert. Die geprüften Texte wurden nicht automatisch korrigiert oder ersetzt. Keine offenen Prüfstatus.

## App-Korrekturen

- Das ausgewählte Rezept steht nun direkt unter dem Surprise-Button und ist sofort sichtbar.
- Nach „Rezept ansehen“ springt die Ansicht automatisch zum geöffneten Rezept.
- Die Zufallsauswahl vermeidet bei mehreren Treffern eine unmittelbare Wiederholung.
- Der Portionswert ist pro Cocktail getrennt. Bei mehreren Cocktails weist die App darauf hin, dass die freigegebenen Zubereitungsschritte ein Glas beschreiben.
- Der Gin-Filter erkennt `Gin` als eigenes Wort und verwechselt es nicht mehr mit `Ginger Beer`.
- Die Rezepte stammen aus dem geprüften Version-3-Paket. Die Infotexte stammen aus den Original-Screenshots.
- Alle 56 Cocktailfotos sind als bereinigte SVG-Dateien enthalten. Bei 16 Bildern werden Textreste oben und bei 31 Bildern Textreste unten auf weißem Grund abgedeckt. Die Cocktailmotive bleiben erhalten.
- 20 zuvor am oberen Rand abgeschnittene Erklärungsausschnitte zeigen jetzt den vollständigen Absatz aus dem jeweiligen Original-Screenshot. Fünf leere Erklärungsausschnitte werden nicht mehr angezeigt. Die übrigen 31 Erklärungen sind an beiden Rändern vollständig.

## Drei getrennte Prüfdurchgänge

1. **Fotos:** Alle 56 aktiven Fotodateien und ihre SVG-Masken gegen die Originalbilder geprüft. Die auffälligen Ränder wurden weiß abgedeckt; Gin and Sin und Mimosa bleiben ohne Maske.
2. **„Über diesen Cocktail“:** Alle 56 Erklärungsausschnitte an Ober- und Unterkante geprüft. 20 angeschnittene Anfänge wiederhergestellt, fünf vollständig leere Ausschnitte ausgeblendet, 31 vollständige Ausschnitte beibehalten.
3. **Funktion:** Anzahl 56, Rezeptaufruf und Sprung zum Rezept, Filter, Überraschung und Portionsmengen getrennt geprüft.
