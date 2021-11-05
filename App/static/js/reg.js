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

function showPop() {
  window.alert("Transaction started. Please send money to the bitcoin address provided, or scan the QR code with your bitcoin mobile wallet, to complete the payment.")
}

function convertCurrency() {
  let ksh = document.getElementById('fill-ksh');
  let bit_val = document.getElementById('bit-val').value;

  let bitcoin_val = 7024549.50;

  ksh.value = bit_val * bitcoin_val;
}