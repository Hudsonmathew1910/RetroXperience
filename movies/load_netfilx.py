import csv
from movies.models import Movies

def load_netflix_movies(path="data/netflix_titles.csv", batch_size=500):
    movies = []
    count = 0

    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Handle missing values
            title = row.get("title", "").strip()
            description = row.get("description", "")
            genre = row.get("listed_in", "").split(",")[0].strip() if row.get("listed_in") else ""
            year = int(row["release_year"]) if row.get("release_year") and row["release_year"].isdigit() else None

            movies.append(Movies(
                title=title,
                description=description,
                genre=genre,
                year=year,
                platform="Netflix",
            ))
            count += 1

            # Insert in batches
            if len(movies) >= batch_size:
                Movies.objects.bulk_create(movies, ignore_conflicts=True)
                print(f"Inserted {count} movies...")
                movies = []

        if movies:
            Movies.objects.bulk_create(movies, ignore_conflicts=True)
            print(f"Inserted {count} movies (final batch).")

    print(f"✅ Finished loading {count} Netflix movies.")
