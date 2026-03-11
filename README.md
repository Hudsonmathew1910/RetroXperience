# RetroXperience — Movie Discovery Web Application

RetroXperience is a Django-based movie discovery app for exploring **retro and classic movies**. It uses a real **Netflix titles CSV dataset**, supports browsing and filtering, and includes an anonymous **1–5 star rating** system with average ratings shown across the site. The project also exposes a REST API and is set up for production deployment with Gunicorn + WhiteNoise.

## Features
- Browse a large movie catalog in a paginated table
- Filter movies by **genre** and **release year**
- Search movies by **title**
- Movie detail page with full info (title, description, genre, year, platform)
- Anonymous **star ratings (1–5)** with real-time **average rating** display
- Django admin panel for managing data
- REST API for external access to movie data
- Ready for cloud deployment (Gunicorn + WhiteNoise)

## Tech Stack
- **Language:** Python 3.13
- **Framework:** Django 5.2
- **REST API:** django-tastypie (0.15)
- **Data/ML (future-ready):** pandas (2.3), scikit-learn (1.7), NumPy (2.3)
- **Frontend:** Bootstrap 5
- **Database (dev):** SQLite (db.sqlite3)
- **Static files:** WhiteNoise
- **Web server:** Gunicorn
- **Deployment target:** Render
- **Code quality:** pylint + pylint-django
- **Version control:** Git / GitHub

## Data Loading
Movie data is imported from `netflix_titles.csv` using a loader script (`load_netfilx.py`) that processes rows and bulk-inserts them into the database in batches (500 rows per batch) for fast setup.

## Ratings System
Visitors can rate any movie from **1 to 5 stars** without creating an account. Ratings are stored in the `MovieRating` model, and the **average rating** is calculated using Django’s `Avg` aggregation and displayed on both the list and detail pages.

## REST API
Movie data is available via a JSON API powered by Tastypie:
- `/api/`
- `/api/movies/`

## Future Improvements
- Add a movie recommendation engine using **pandas + scikit-learn** (similar movies by genre/year and rating patterns)
- User accounts + personalized watchlist and rating history
- Advanced search and sorting (platform, popularity, rating, decade filters)

## Author
Built by **Hudson Mathew** — September 2025
