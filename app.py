from flask import Flask, request, send_file, render_template, flash, redirect, url_for
from PIL import Image
import img2pdf
import io

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessary for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        files = request.files.getlist('files')
        if not files:
            flash('No files provided', 'danger')
            return redirect(url_for('index'))

        operation = request.form.get('operation')
        compression_format = request.form.get('compressionFormat')
        compression_quality = request.form.get('compressionQuality')
        crop_ratio = request.form.get('cropRatio')

        if operation == 'jpgToPdf':
            images = [file.read() for file in files]
            pdf_bytes = img2pdf.convert(images)
            pdf_io = io.BytesIO(pdf_bytes)
            return send_file(pdf_io, mimetype='application/pdf', as_attachment=True, download_name='output.pdf')

        elif operation == 'compress':
            quality = int(compression_quality)
            images = []
            for file in files:
                img = Image.open(file)
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                img_byte_arr = io.BytesIO()
                img.save(img_byte_arr, format=compression_format, quality=quality)
                img_byte_arr = img_byte_arr.getvalue()
                images.append(img_byte_arr)
            if len(images) == 1:
                img_io = io.BytesIO(images[0])
                img_io.seek(0)
                return send_file(img_io, mimetype=f'image/{compression_format.lower()}', as_attachment=True, download_name=f'output.{compression_format.lower()}')
            else:
                pdf_bytes = img2pdf.convert(images)
                pdf_io = io.BytesIO(pdf_bytes)
                return send_file(pdf_io, mimetype='application/pdf', as_attachment=True, download_name='output.pdf')

        elif operation == 'crop':
            ratio_map = {
                '1:1': (1, 1),
                '3:2': (3, 2),
                '4:3': (4, 3),
                '16:9': (16, 9)
            }
            width_ratio, height_ratio = ratio_map[crop_ratio]
            images = []
            for file in files:
                img = Image.open(file)
                img_width, img_height = img.size
                crop_width = min(img_width, img_height * width_ratio / height_ratio)
                crop_height = min(img_height, img_width * height_ratio / width_ratio)
                left = (img_width - crop_width) / 2
                top = (img_height - crop_height) / 2
                right = (img_width + crop_width) / 2
                bottom = (img_height + crop_height) / 2
                img = img.crop((left, top, right, bottom))
                if img.mode == 'RGBA':
                    img = img.convert('RGB')
                img_byte_arr = io.BytesIO()
                img.save(img_byte_arr, format=compression_format)
                img_byte_arr = img_byte_arr.getvalue()
                images.append(img_byte_arr)
            if len(images) == 1:
                img_io = io.BytesIO(images[0])
                img_io.seek(0)
                return send_file(img_io, mimetype=f'image/{compression_format.lower()}', as_attachment=True, download_name=f'output.{compression_format.lower()}')
            else:
                pdf_bytes = img2pdf.convert(images)
                pdf_io = io.BytesIO(pdf_bytes)
                return send_file(pdf_io, mimetype='application/pdf', as_attachment=True, download_name='output.pdf')

        return 'Invalid operation', 400
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
