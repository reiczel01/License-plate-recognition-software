import cv2
import numpy as np
import subprocess

# Ustaw link do strumienia wideo
stream_url = 'https://62abe29de64ab.streamlock.net:4444/EPGD/pps3.stream/playlist.m3u8'

# Definiuj komendę ffmpeg do pobierania strumienia wideo
ffmpeg_cmd = [
    'ffmpeg',
    '-i', stream_url,
    '-vf', 'format=bgr24',
    '-c:v', 'rawvideo',
    '-an', '-sn',
    '-f', 'image2pipe',
    '-pix_fmt', 'bgr24',
    '-']

# Uruchamiaj proces ffmpeg i otwieraj potok
ffmpeg_process = subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, bufsize=10**8)

# Pętla odczytująca i wyświetlająca klatki strumienia
while True:
    # Odczytaj klatkę z potoku
    raw_frame = ffmpeg_process.stdout.read(3840 * 2160 * 3)  # Ustaw rozmiar klatki zgodnie z wymaganiami

    # Sprawdź, czy odczytano dane klatki
    if not raw_frame:
        break

    # Konwertuj dane klatki do tablicy numpy
    frame = np.frombuffer(raw_frame, dtype=np.uint8)
    frame = frame.reshape((2160, 3840, 3))

    # Wyświetl klatkę
    cv2.imshow('Strumień wideo', frame)

    # Przerwij pętlę po naciśnięciu klawisza 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Zatrzymaj proces ffmpeg i zwolnij zasoby
ffmpeg_process.kill()
cv2.destroyAllWindows()
