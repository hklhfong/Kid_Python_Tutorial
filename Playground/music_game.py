import random
import pygame

# Initialize Pygame
pygame.init()

# Define a list of song lyrics and their corresponding song titles
songs = {
    "I've paid my dues, time after time": "We Will Rock You",
    "I'm just a poor boy, nobody loves me": "Bohemian Rhapsody",
    "Yesterday, all my troubles seemed so far away": "Yesterday",
}



def play_music_game():
    print("Welcome to the Music Guessing Game!")
    print("I'll give you a line from a song, and you have to guess the song title.")
    print("Type 'quit' to exit the game.")
    

    while True:
        lyric, song_title = random.choice(list(songs.items()))
        # Load the background music
        pygame.mixer.music.load(song_title + '.mp3')
        pygame.mixer.music.set_volume(0.3)  # Adjust the volume
        pygame.mixer.music.play(-1)  # Start playing the background music and looping

        print("\nHere's a lyric from a song:")
        print(lyric)
        guess = input("Guess the song title: ").strip().title()

        if guess == "Quit":
            break

        if guess == song_title:
            print("Correct! You guessed the song title.")
        else:
            print(f"Sorry, that's not correct. The song title is '{song_title}'.")

if __name__ == "__main__":
    try:
        play_music_game()
    finally:
        pygame.mixer.music.stop()
