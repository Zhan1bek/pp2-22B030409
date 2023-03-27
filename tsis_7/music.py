import pygame

clock = pygame.time.Clock()
_songs = ['muz1.mp3', 'muz2.mp3', 'muz3.mp3', 'muz4.mp3', 'muz5.mp3']

pygame.mixer.init()
pygame.display.set_mode((200,100))
pygame.mixer.music.load(_songs[0])
pygame.mixer.music.play(0)
clock.tick(10)

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play(0)

def play_prev_song():
    global _songs
    _songs = [_songs[-1]] + _songs[:-1]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play(0)

def muspause():
    done = False
    while not done:
        pygame.mixer.music.pause()
        clock.tick(10)
        pygame.event.poll()
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            pygame.mixer.music.unpause()
            done = True


while pygame.mixer.music.get_busy():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]: play_prev_song()
    if pressed[pygame.K_RIGHT]: play_next_song()
    if pressed[pygame.K_SPACE]: muspause()
    if pressed[pygame.K_DOWN]: pygame.mixer.music.stop()
    pygame.event.poll()
    clock.tick(10)