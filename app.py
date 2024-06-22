from flask import Flask, request, send_file, render_template
import img2pdf
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    try:
        files = request.files.getlist('files')
        if not files:
            return 'No files provided', 400
        images = [file.read() for file in files]
        pdf_bytes = img2pdf.convert(images)
        with open('output.pdf', 'wb') as f:
            f.write(pdf_bytes)
        return send_file('output.pdf', as_attachment=True)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)

