// Get the email and password inputs
var emailInput = document.getElementsByName("email")[0];
var passwordInput = document.getElementsByName("password")[0];

// Send a POST request to the server when the submit button is clicked
document.getElementById("submitButton").addEventListener("click", function() {
  // Enter the email and password values
  emailInput.value = "example@example.com";
  passwordInput.value = "password";

  // Submit the login form
  document.forms[0].submit();

  // Wait for the page to load and do any necessary processing
  setTimeout(function() {
    // Call the Python function to run the main script with the email and password arguments
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "#edit this to work w/ carine's working JS, );
    xhr.send();
  }, 5000);
});
