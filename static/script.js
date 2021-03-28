function github(){
  var ch = document.getElementById('chGitHub');
  if (ch.checked) {
    document.getElementById('selGitHub').disabled = false
  }
  else {
    document.getElementById('selGitHub').disabled = true
  }
}

function habr(){
  var ch = document.getElementById('chHabr');
  if (ch.checked) {
    document.getElementById('selHabr').disabled = false
  }
  else {
    document.getElementById('selHabr').disabled = true
  }
}

function hqna(){
  var ch = document.getElementById('chHQNA');
  if (ch.checked) {
    document.getElementById('selHQNA1').disabled = false
    document.getElementById('selHQNA2').disabled = false
  }
  else {
    document.getElementById('selHQNA1').disabled = true
    document.getElementById('selHQNA2').disabled = true
  }
}

function find(){
  var inp = document.getElementById('text-search').value.replace(' ', '+');

  if (inp == ''){
    alert('Hmm ... Correct the mistake without its description, stupid act.');
    return;
  }

  var ch1 = document.getElementById('chGitHub').checked,
      ch2 = document.getElementById('chRTD').checked,
      ch3 = document.getElementById('chHabr').checked,
      ch4 = document.getElementById('chHQNA').checked,
      vari = ['null', '1', '2', '3', '4', '5'],
      log = ['true', 'false'];

  if (ch1 || ch2 || ch3 || ch4){
    window.location.href = `/find/${inp}?github=${ch1}&number_of_comments=${vari[document.getElementById('selGitHub').selectedIndex]}&rtd=${ch2}&habr=${ch3}&total=${vari[document.getElementById('selHabr').selectedIndex]}&hqna=${ch4.checked}&answer=${log[document.getElementById('selHQNA1').selectedIndex]}&quantity_answer=${vari[document.getElementById('selHQNA2').selectedIndex]}`;
  }
  else {
    alert('Oops, no services included for troubleshooting (');
  }
}
