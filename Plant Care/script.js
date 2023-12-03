const uploadInput = document.getElementById("image-upload");

uploadInput.addEventListener("change", function () {
    if (uploadInput.files.length > 0) {
        window.location.href = "loading.html";
    }
});

const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';

      // Select the login button container
      const loginButtonContainer = document.getElementById('loginButtonContainer');

      if (isLoggedIn) {
        const username = localStorage.getItem('username');
        // If the user is logged in, change the button to "Logout"
        loginButtonContainer.innerHTML = `
        <div style="float: right; margin-right: 20px;">
          <span>Welcome, ${username}</span>
          <button id="logout-button" onclick="logout()">Logout</button>
        </div>
        `;
      } else {
        // If the user is not logged in, keep the "Login" button
        loginButtonContainer.innerHTML = `
          <button id="login-button" onclick="redirectToLogin()">Login</button>
        `;
      }

      // Function to handle logout
      function logout() {
        // Clear login state from local storage
        localStorage.removeItem('isLoggedIn');
        localStorage.removeItem('username');
        // Redirect to the login page
        window.location.href = 'login.html';
      }

      // Function to redirect to the login page
      function redirectToLogin() {
        window.location.href = 'login.html';
      }


