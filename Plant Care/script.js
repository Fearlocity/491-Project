const uploadInput = document.getElementById("image-upload");

uploadInput.addEventListener("change", function () {
    if (uploadInput.files.length > 0) {
        window.location.href = "loading.html";
    }
});