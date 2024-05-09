from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import numpy as np
from utils.resize import image_resize
from utils.compress import audio_compress

app = Flask(__name__)

# INDEX=======
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# IMAGE========
@app.route('/resize', methods=['GET', 'POST'])
def imageResize():
    if request.method == 'POST':
        image_file = request.files['image']
        if image_file:
            
            resized_image = image_resize(image_file)

            return send_file(
                resized_image, 
                as_attachment=True, 
                download_name='resized_image.png'
            )

    return render_template('image-resize.html')


# AUDIO========
@app.route('/audio-compress', methods=['GET', 'POST'])
def audioCompress():
    if request.method == 'POST':
        audio_file = request.files.get("audio", None)
        if not audio_file:
            return render_template("audio-compress.html", error="Tidak ada file yang diunggah.")

        audio_data = audio_file.read()

        if not audio_data:
            return render_template("audio-compress.html", error="Data audio tidak valid.")

        compressed_audio = audio_compress(audio_data)

        if compressed_audio:
            return send_file(
                compressed_audio,
                as_attachment=True,
                download_name='compressed_audio.mp3'
            )
        return render_template("audio-compress.html", error="Terjadi kesalahan saat kompresi.")
    return render_template('audio-compress.html')

if __name__ == "__main__":
    app.run(debug=True)