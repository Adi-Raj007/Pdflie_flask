from flask import Flask, request, send_file, render_template
from PIL import Image
import img2pdf
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        files = request.files.getlist('files')
        if not files:
            return 'No files provided', 400

        compression_format = request.form.get('compressionFormat', 'JPEG')
        crop_width = request.form.get('cropWidth')
        crop_height = request.form.get('cropHeight')

        images = []
        for file in files:
            img = Image.open(file)
            if crop_width and crop_height:
                crop_width = int(crop_width)
                crop_height = int(crop_height)
                img = img.crop((0, 0, crop_width, crop_height))
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format=compression_format)
            img_byte_arr = img_byte_arr.getvalue()
            images.append(img_byte_arr)

        pdf_bytes = img2pdf.convert(images)
        pdf_io = io.BytesIO(pdf_bytes)

        return send_file(pdf_io, mimetype='application/pdf', as_attachment=True, download_name='output.pdf')
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)

