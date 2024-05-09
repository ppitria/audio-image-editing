import soundfile as sf
import numpy as np
import io
from io import BytesIO

def audio_compress(audio_data):
    if not audio_data:
        raise ValueError("Data audio tidak valid")

    audio, sample_rate = sf.read(io.BytesIO(audio_data))

    compressed_io = io.BytesIO()
    sf.write(compressed_io, audio, sample_rate, format='mp3')
    compressed_io.seek(0)

    return compressed_io