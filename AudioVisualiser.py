import pygame
import sounddevice as sd
import numpy as np
import math

# --- CONFIGURATION ---
WIDTH, HEIGHT = 1000, 600
FPS = 60
CHUNK_SIZE = 1024  
RATE = 44100  

# --- PYGAME INITIALIZATION ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EDM Fluid Gradient Audio Visualizer (SoundDevice)")
clock = pygame.time.Clock()

# --- AUDIO SHARING STATE ---
fft_data = np.zeros(CHUNK_SIZE // 2 + 1)

# This callback routine runs automatically in the background whenever audio arrives
def audio_callback(indata, frames, time, status):
    global fft_data
    if any(indata):
        # Flatten the input to mono channels
        audio_signal = indata[:, 0]
        window = np.hanning(len(audio_signal))
        fft_data = np.abs(np.fft.rfft(audio_signal * window))
    else:
        fft_data = np.zeros(CHUNK_SIZE // 2 + 1)

# Start the streamlined non-blocking audio recording stream
stream = sd.InputStream(samplerate=RATE, channels=1, blocksize=CHUNK_SIZE, callback=audio_callback)
stream.start()

# --- COLORS & MOTION ---
COLOR_LOW = (15, 23, 150, 140)    
COLOR_MID = (0, 180, 216, 100)    
COLOR_HIGH = (144, 224, 239, 90)  
BG_COLOR = (5, 5, 15)             

low_smooth = 0
mid_smooth = 0
high_smooth = 0
DECAY = 0.12  
time_step = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Process localized frequency buckets from shared global spectrum
    # Tweaked scalars to align cleanly with sounddevice's internal float mapping
    low_freq = np.mean(fft_data[1:10]) * 1.8
    mid_freq = np.mean(fft_data[10:60]) * 2.5
    high_freq = np.mean(fft_data[60:250]) * 4.5

    # Exponential moving average wrapper ("The Pump Control")
    low_smooth += (low_freq - low_smooth) * DECAY
    mid_smooth += (mid_freq - mid_smooth) * DECAY
    high_smooth += (high_freq - high_smooth) * DECAY

    low_amp = max(low_smooth, 5)
    mid_amp = max(mid_smooth, 3)
    high_amp = max(high_smooth, 2)

    screen.fill(BG_COLOR)
    overlay_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    time_step += 0.04  

    points_low, points_mid, points_high = [], [], []

    for x in range(0, WIDTH, 5):
        # Low frequencies
        y_low = (HEIGHT / 2) + math.sin(x * 0.005 + time_step * 0.8) * low_amp * 1.5
        y_low += math.sin(x * 0.01 + time_step) * (low_amp * 0.5)
        points_low.append((x, y_low))

        # Mid frequencies
        y_mid = (HEIGHT / 2) + math.sin(x * 0.012 + time_step * 1.5) * mid_amp * 2.0
        y_mid += math.cos(x * 0.02 + time_step * 0.7) * (mid_amp * 0.4)
        points_mid.append((x, y_mid))

        # High frequencies
        y_high = (HEIGHT / 2) + math.sin(x * 0.025 + time_step * 2.2) * high_amp * 2.5
        y_high += math.sin(x * 0.05 + time_step * 3.0) * (high_amp * 0.6)
        points_high.append((x, y_high))

    points_low.extend([(WIDTH, HEIGHT), (0, HEIGHT)])
    points_mid.extend([(WIDTH, HEIGHT), (0, HEIGHT)])
    points_high.extend([(WIDTH, HEIGHT), (0, HEIGHT)])

    pygame.draw.polygon(overlay_surface, COLOR_LOW, points_low)
    pygame.draw.polygon(overlay_surface, COLOR_MID, points_mid)
    pygame.draw.polygon(overlay_surface, COLOR_HIGH, points_high)

    screen.blit(overlay_surface, (0, 0))
    pygame.display.flip()
    clock.tick(FPS)

stream.stop()
stream.close()
pygame.quit()