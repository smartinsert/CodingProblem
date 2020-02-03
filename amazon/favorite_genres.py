"""
Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user has
listened to as values.

Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within that
genre as values. The song can only belong to only one genre.

The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the
user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre
if he/she has listened to the same number of songs per each of the genres.

Example 1:

Input:
userSongs = {
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
},
songGenres = {
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

Output: {
   "David": ["Rock", "Techno"],
   "Emma":  ["Pop"]
}
"""

from typing import List, Dict
import math


def get_favourite_genres(user_songs: Dict[str, List[str]], genre_to_songs: Dict[str, List[str]]) -> Dict[str, List[str]]:
    user_to_genres = dict()
    song_to_genre = dict()
    for genre in genre_to_songs.keys():
        songs = genre_to_songs.get(genre)
        for song in songs:
            song_to_genre[song] = genre
    for user in user_songs:
        max_count = -math.inf
        genre_to_count = {genre: 0 for genre in genre_to_songs}
        songs = user_songs[user]
        favourite_genres = []
        for song in songs:
            genre = song_to_genre[song]
            genre_to_count[genre] += 1
            if genre_to_count[genre] > max_count:
                max_count = genre_to_count[genre]
                # refresh genres
                favourite_genres = []
                favourite_genres.append(genre)
            elif genre_to_count[genre] == max_count:
                # Add the genres whose count is equal 
                favourite_genres.append(genre)
        user_to_genres[user] = favourite_genres
    return user_to_genres


if __name__ == '__main__':
    userSongs = {
                    "David": ["song1", "song2", "song3", "song4", "song8"],
                    "Emma": ["song5", "song7", "song6"]
                }

    songGenres = {
        "Rock": ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno": ["song2", "song4"],
        "Pop": ["song5", "song6"],
        "Jazz": ["song8", "song9"]
    }

    print(get_favourite_genres(userSongs, songGenres))