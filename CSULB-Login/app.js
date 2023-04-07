var nextBtn = document.querySelector(".sign-in-next-btn-submit");
var passwordDiv = document.querySelector(".password-sign-in-form");
var emailDiv = document.querySelector(".email-sign-in-form");
var loadingDiv = document.querySelector(".loading-screen");
const email = localStorage.getItem('.username')




nextBtn.addEventListener("click", function(event) {
    event.preventDefault(); 
    passwordDiv.style.display = "block";
    emailDiv.style.display = "none";
});

document.getElementById("username").addEventListener('keyup',returnUsername);
function returnUsername(){
    document.getElementById("display-name").innerHTML = document.getElementById("username").value;
}






