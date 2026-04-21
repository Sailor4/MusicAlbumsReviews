# Music Albums Reviews Project
This is my Django project for SoftUni Advanced Retake exam

## 🚀 Features
* **Full CRUD for Albums & Artists:** Users can suggest new artists, register albums, view the full catalog, and manage entries.
* **Full CRUD for Reviews:** Community members can post ratings and feedback for albums, update their reviews, and delete them.
* **Dynamic Music Dashboard:** A curated homepage showing the latest added albums and the most popular ones based on community ratings.
* **Thematic Search:** A functional search and filter system in the navigation menu to find albums by title or artist.
* **Custom Error Handling:** Personalized, music-themed 404 (Vinyl Scratched) and 500 (Amp Blew Up) pages for a better user experience.
* **Template Inheritance:** Efficient frontend architecture using a master layout to ensure UI consistency across the site.

## 📂 Project Structure
I organized the project into logical apps to ensure the code is modular and clean:
* `MusicAlbumsReviews/` - Project configuration, settings, and main URL routing.
* `common/` - Contains logic for shared pages (Home, Search, Contact), custom error handlers, and authentication.
* `albums/` - Handles the core data models: Album, Artist, and Review, along with their management views.
* `templates/` - Organized with a root `base.html` and subfolders for app-specific templates.
* `static/` - Contains the global `style.css` file with my custom dark-mode theme.

## 🛠️ Technical Choices
* **Template Inheritance (DRY):** I implemented a master `base.html` file using Django's `{% extends %}` and `{% block %}` tags. This keeps the UI consistent and the code easier to maintain.
* **PostgreSQL:** Used as the primary relational database to handle data integrity and complex relationships between artists and albums.
* **Custom Dark Theme:** I designed a custom CSS inspired by modern music platforms (like Spotify) to provide a professional look and feel.
* **Class-Based Views (CBVs):** Most of the logic is handled by CBVs for better readability and reusability of the code.

## 💻 How to Run
Follow these steps to get the project running locally:

1. **Clone the project** and navigate into the directory.
2. **Install requirements:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Ensure PostgreSQL is running and a database named music_albums_db exists.
4. **Update the DATABASES setting in settings.py if your local credentials differ.
5. **Run the migrations to create the schema:
    ```bash
   python manage.py migrate
   ```
6. **Create Superuser:
    ```bash
    python manage.py createsuperuser
    ```
7. **Seed the Database provided:
    ```bash
    python seed_data.py
    ```
8. **Start the server:
    ```bash
    python manage.py runserver
    ```
9. ** Access the site: Open http://127.0.0.1:8000/ in your browser.