$(document).ready(function() {
    $('#operationType').change(function() {
        const operation = $(this).val();
        if (operation === 'compress') {
            $('#compressionOptions').show();
            $('#cropOptions').hide();
        } else if (operation === 'crop') {
            $('#compressionOptions').hide();
            $('#cropOptions').show();
        } else {
            $('#compressionOptions').hide();
            $('#cropOptions').hide();
        }
    });

    $('#fileInput').change(function() {
        let files = $(this).prop('files');
        if (files.length > 0) {
            $('#uploadForm button').html('<i class="fas fa-spinner fa-spin"></i> Processing...');
        }
    });

    $('#uploadForm').submit(async function(e) {
        e.preventDefault();
        const files = $('#fileInput')[0].files;
        const formData = new FormData();
        for (const file of files) {
            formData.append('files', file);
        }
        formData.append('operation', $('#operationType').val());
        formData.append('compressionFormat', $('#compressionFormat').val());
        formData.append('compressionQuality', $('#compressionQuality').val());
        formData.append('cropRatio', $('#cropRatio').val());

        const response = await fetch('/process', {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const blob = await response.blob();
            const url = URL.createObjectURL(blob);
            const fileName = prompt("Enter the name for the output file:", "output");
            if (fileName) {
                const link = document.createElement('a');
                link.href = url;
                link.download = `${fileName}.${$('#operationType').val() === 'jpgToPdf' ? 'pdf' : $('#compressionFormat').val().toLowerCase()}`;
                $('#output').html(link);
                link.click();
            }
            $('#uploadForm button').html('<i class="fas fa-file-upload"></i> Process');
        } else {
            const errorText = await response.text();
            $('#output').html(`<p style="color: red;">${errorText}</p>`);
            $('#uploadForm button').html('<i class="fas fa-file-upload"></i> Process');
        }
    });
});

