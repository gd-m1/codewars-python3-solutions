# https://www.codewars.com/kata/551dc350bf4e526099000ae5

def song_decoder(song):
    song = song.split('WUB')
    while '' in song:
        song.remove('')
    return ' '.join(song)
