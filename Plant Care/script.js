const uploadInput = document.getElementById("image-upload");

uploadInput.addEventListener("change", function () {
  if (uploadInput.files.length > 0) {
    window.location.href = "loading.html";
  }
});

const isLoggedIn = sessionStorage.getItem('isLoggedIn') === 'true';

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

function openTimePopup() {
  const selectedTime = window.prompt("Enter the notification time (HH:mm) military time");

  if (selectedTime !== null && selectedTime !== "") {
    const timeRegex = /^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$/;
    if (timeRegex.test(selectedTime)) {
      const notificationTime = new Date();
      const [hours, minutes] = selectedTime.split(":");
      notificationTime.setHours(parseInt(hours, 10), parseInt(minutes, 10), 0, 0);

      // Calculate the timeout value, considering if the selected time is earlier than the current time
      let timeout = notificationTime.getTime() - Date.now();
      if (timeout < 0) {
        const nextDay = new Date();
        nextDay.setDate(nextDay.getDate() + 1);
        nextDay.setHours(parseInt(hours, 10), parseInt(minutes, 10), 0, 0);
        timeout = nextDay.getTime() - Date.now();
      }
      console.log(timeout)

      setTimeout(() => {
        // Check if the browser supports notifications
        if (Push.Permission.has()) {
            // Request permission if not granted
            Push.Permission.request();
        }

        // Trigger a scheduled push notification
        Push.create("Plant Care Assistant", {
            body: "This is a scheduled notification.",
            icon: "images/watering.jpg",
            onClick: function () {
                window.focus();
                this.close();
            }
        });
      }, timeout);
    } else {
      alert("Invalid time format. Please use HH:mm format.");
    }
  }
}


