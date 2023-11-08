const uploadInput = document.getElementById("image-upload");
const loginButton = document.getElementById("login-button")

uploadInput.addEventListener("change", function () {
    if (uploadInput.files.length > 0) {
        window.location.href = "loading.html";
    }
});

loginButton.addEventListener("click", function () {
    window.location.href = "login.html";
});