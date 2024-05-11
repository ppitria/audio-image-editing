import soundfile as sf
import io

def audio_compress(audio_data):
    if not audio_data:
        raise ValueError("Data audio tidak valid")

    audio, sample_rate = sf.read(io.BytesIO(audio_data))

    new_sample_rate = sample_rate//2

    compressed_io = io.BytesIO()
    sf.write(compressed_io, audio, new_sample_rate, format='mp3')
    compressed_io.seek(0)

    return compressed_io