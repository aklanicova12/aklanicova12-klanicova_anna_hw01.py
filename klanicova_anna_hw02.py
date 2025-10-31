import csv
import json

# Název vstupního a výstupního souboru
input_file = "netflix_titles.tsv"
output_file = "hw02_output.json"

# Seznam, do kterého budeme ukládat vyčištěná data
movies_list = []

# Otevření TSV souboru a jeho zpracování
with open(input_file, encoding="utf-8") as tsvfile:
    reader = csv.DictReader(tsvfile, delimiter="\t")
    
    for row in reader:
        # Získání základních údajů
        title = row.get("PRIMARYTITLE", "").strip()
        directors = row.get("DIRECTOR", "").strip()
        cast = row.get("CAST", "").strip()
        genres = row.get("GENRES", "").strip()
        start_year = row.get("STARTYEAR", "").strip()
        
        # Převod řetězců oddělených čárkami na seznamy
        directors_list = [d.strip() for d in directors.split(",")] if directors else []
        cast_list = [c.strip() for c in cast.split(",")] if cast else []
        genres_list = [g.strip() for g in genres.split(",")] if genres else []
        
        # Výpočet dekády
        try:
            year = int(start_year)
            decade = (year // 10) * 10
        except ValueError:
            decade = None  # Pokud není rok uveden
        
        # Vytvoření slovníku pro jeden film
        movie_dict = {
            "title": title,
            "directors": directors_list,
            "cast": cast_list,
            "genres": genres_list,
            "decade": decade
        }
        
        movies_list.append(movie_dict)

# Uložení výsledku do JSON souboru
with open(output_file, "w", encoding="utf-8") as jsonfile:
    json.dump(movies_list, jsonfile, indent=4, ensure_ascii=False)

print(f"Data byla uložena do {output_file}.")
