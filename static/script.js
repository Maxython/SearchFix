function github(){
  var ch = document.getElementById('chGitHub'),
      sel = document.getElementById('selGitHub');
  if (ch.checked) {
    sel.disabled = false;
  }
  else {
    sel.disabled = true;
    sel.value = sel.options[0].text;
  }
}

function rtd(){
  var ch = document.getElementById('chRTD'),
      sel = document.getElementById('selRTD');
  if (ch.checked) {
    sel.disabled = false;
  }
  else {
    sel.disabled = true;
    sel.value = sel.options[0].text;
  }
}

function habr(){
  var ch = document.getElementById('chHabr'),
      sel = document.getElementById('selHabr');
  if (ch.checked) {
    sel.disabled = false;
  }
  else {
    sel.disabled = true;
    sel.value = sel.options[0].text;
  }
}

function hqna(){
  var ch = document.getElementById('chHQNA'),
      sel1 = document.getElementById('selHQNA1'),
      sel2 = document.getElementById('selHQNA2');
  if (ch.checked) {
    sel1.disabled = false;
    sel2.disabled = false;
  }
  else {
    sel1.disabled = true;
    sel1.value = sel1.options[0].text;
    sel2.disabled = true;
    sel2.value = sel2.options[0].text;
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
      log = ['true', 'false'],
      quan = ['null', '5', '10', '20'];

  if (ch1 || ch2 || ch3 || ch4){
    window.location.href = `find/${inp}?github=${ch1}&number_of_comments=${vari[document.getElementById('selGitHub').selectedIndex]}&rtd=${ch2}&quantity=${quan[document.getElementById('selRTD').selectedIndex]}&habr=${ch3}&total=${vari[document.getElementById('selHabr').selectedIndex]}&hqna=${ch4}&answer=${log[document.getElementById('selHQNA1').selectedIndex]}&quantity_answer=${vari[document.getElementById('selHQNA2').selectedIndex]}`;
  }
  else {
    alert('Oops, no services included for troubleshooting (');
  }
}
