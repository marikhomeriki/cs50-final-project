document.addEventListener('DOMContentLoaded', () => {
    const fileInput = document.querySelector('#file');
    const image = document.querySelector('#image');

    if (fileInput === null || image === null) {
        return;
    }

    fileInput.addEventListener('change', () => {
        if (fileInput.files.length === 0) {
            return;
        }

        const file = fileInput.files[0];

        const url = URL.createObjectURL(file);

        image.src = url;
    })

    console.log(fileInput)
})
