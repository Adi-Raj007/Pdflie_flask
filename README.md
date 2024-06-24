# Image Tools Web Application

This web application provides a set of tools for processing images, including converting JPG to PDF, compressing images, and cropping images. It is built with Flask and uses the Pillow and img2pdf libraries for image processing.

## Features

- **JPG to PDF Conversion**: Convert multiple JPG images into a single PDF file.
- **Image Compression**: Compress images to a specified format (JPEG, PNG, WEBP) and quality.
- **Image Cropping**: Crop images to predefined ratios (1:1, 3:2, 4:3, 16:9).

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Adi-Raj007/flask-image-tools.git
    cd flask-image-tools
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Run the Flask App**:
    ```bash
    flask run
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000/`.

## Deployment

### Deploy to Render

1. **Create a New Web Service**:
    - Connect your GitHub repository.
    - Set the Build Command to:
      ```bash
      pip install -r requirements.txt
      ```
    - Set the Start Command to:
      ```bash
      gunicorn app:app
      ```
Open this website at https://pdflie-flask.onrender.com
2. **Deploy the Service**.

## Usage

1. **Choose Files**: Click on "Choose Files" to select the images you want to process.
2. **Select Operation**: Choose an operation (JPG to PDF, Compress Image, Crop Image).
3. **Configure Options**:
    - For compression, select the format and quality.
    - For cropping, select the desired ratio.
4. **Process**: Click "Process" to start the operation.
5. **Download**: Enter a name for the output file and download it.

## Technologies Used

- **Frontend**: HTML, CSS (Bootstrap), JavaScript (jQuery)
- **Backend**: Flask, Pillow, img2pdf
- **Deployment**: Render

## License

This project is licensed under the MIT License.

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## Contact

For questions or suggestions, please open an issue or contact the repository owner.

