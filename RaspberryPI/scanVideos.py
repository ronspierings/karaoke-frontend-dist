import os
import json

def inventariseer_liedjes(directory, output_json):
    # Maak een lege lijst voor de liedjes
    liedjes = []

    # Doorloop alle bestanden in de opgegeven directory
    for filename in os.listdir(directory):
        # Controleer of het een .mp3-bestand is
        if filename.endswith(".mp3"):
            # Maak een object met de gevraagde structuur
            lied = {
                "songFilename": filename,
                "songTitle": "",
                "songArtist": ""
            }
            # Voeg het object toe aan de lijst
            liedjes.append(lied)

    # Schrijf de lijst met liedjes naar een JSON-bestand
    with open(output_json, "w", encoding='utf-8') as json_file:
        json.dump(liedjes, json_file, ensure_ascii=False, indent=4)

    print(f"Inventarisatie opgeslagen in {output_json}")

# Voorbeeld van hoe het script te gebruiken:
directory_path = "frontend/karaoke-frontend-dist/videos"  # Verander dit naar jouw map
output_json_file = "liedjes_inventaris.json"  # Dit is het uitvoerbestand

# Roep de functie aan
inventariseer_liedjes(directory_path, output_json_file)
