document.getElementById('uploadForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const files = document.getElementById('fileInput').files;
    const formData = new FormData();
    for (const file of files) {
        formData.append('files', file);
    }

    const response = await fetch('/convert', {
        method: 'POST',
        body: formData
    });

    const blob = await response.blob();
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = 'converted.pdf';
    document.getElementById('output').appendChild(link);
    link.click();
});

