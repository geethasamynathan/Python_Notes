document
  .getElementById("loginForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent form from submitting

    let username = document.getElementById("username").value.trim();
    let password = document.getElementById("password").value.trim();
    let usernameError = document.getElementById("usernameError");
    let passwordError = document.getElementById("passwordError");
    let loginMessage = document.getElementById("loginMessage");

    usernameError.textContent = "";
    passwordError.textContent = "";
    loginMessage.textContent = "";

    let isValid = true;

    if (username === "") {
      usernameError.textContent = "Username is required";
      isValid = false;
    }

    if (password === "") {
      passwordError.textContent = "Password is required";
      isValid = false;
    }

    if (isValid) {
      if (username === "admin" && password === "1234") {
        loginMessage.style.color = "green";
        loginMessage.textContent = "Login successful!";
      } else {
        loginMessage.style.color = "red";
        loginMessage.textContent = "Invalid username or password";
      }
    }
  });
