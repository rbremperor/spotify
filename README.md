# Music API

This is a Django REST Framework (DRF) API for managing music-related data, including artists, albums, and songs. The API supports listing, searching, and ordering songs, as well as tracking the number of times a song has been listened to.

## Features
- **CRUD operations** for Artists, Albums, and Songs
- **Pagination** for song listings
- **Filtering and searching** by song title and artist name
- **Track song listens** with an atomic transaction
- **Retrieve top 10 most listened songs**
- **List all albums of a specific artist**

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_directory>
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Run the development server:
   ```sh
   python manage.py runserver
   ```

## API Endpoints

### Song API
- `GET /songs/` - List all songs (supports pagination, ordering, and search)
- `POST /songs/` - Create a new song
- `GET /songs/{id}/` - Retrieve a specific song
- `PUT /songs/{id}/` - Update a song
- `DELETE /songs/{id}/` - Delete a song
- `POST /songs/{id}/listen/` - Increment the song's listen count
- `GET /songs/top/` - Retrieve the top 10 most listened songs

### Artist API
- `GET /artists/` - List all artists
- `POST /artists/` - Create a new artist
- `GET /artists/{id}/` - Retrieve a specific artist
- `PUT /artists/{id}/` - Update an artist
- `DELETE /artists/{id}/` - Delete an artist
- `GET /artists/{id}/albums/` - List all albums of a specific artist

### Album API
- `GET /albums/` - List all albums
- `POST /albums/` - Create a new album
- `GET /albums/{id}/` - Retrieve a specific album
- `PUT /albums/{id}/` - Update an album
- `DELETE /albums/{id}/` - Delete an album

## Filtering and Searching
- Songs can be searched by `title` or `album__artist__name`.
- Songs can be ordered by `listened` in ascending or descending order (`-listened`).

## Pagination
The API uses `LimitOffsetPagination` for paginating song results.

## Running Tests
To run tests, use:
```sh
python manage.py test
```

## License
This project is licensed under the MIT License.

