var signup = document.getElementById('register-page');
var signin = document.getElementById('login-page');
var reset = document.getElementById('reset-page')

function showReg() {
  signin.style.display = 'none';
  reset.style.display = 'none';
  signup.style.display = 'block';
}

function showLogin() {
  signup.style.display = 'none';
  reset.style.display = 'none';
  signin.style.display = 'block';
}

function showReset() {
  signup.style.display = 'none';
  signin.style.display = 'none';
  reset.style.display = 'block';
}
