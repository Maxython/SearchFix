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
  var ch1 = document.getElementById('chGitHub'),
      ch2 = document.getElementById('chRTD'),
      ch3 = document.getElementById('chHabr'),
      ch4 = document.getElementById('chHQNA'),
      inp = document.getElementById('text-search').value.replace(' ', '+');

  if (inp == ''){
    alert('Hmm ... Correct the mistake without its description, stupid act.');
    return;
  }

  if (ch1.checked || ch2.checked || ch3.checked || ch4.checked){
    var url = `/find/${inp}?github=${ch1.checked}`;
    if (ch1.checked){
      var sel = document.getElementById('selGitHub');
      url = url + `&comen=${sel.options[sel.selectedIndex].text}`;
    }

    url = url + `&rtd=${ch2.checked}&habr=${ch3.checked}`;
    if (ch3.checked){
      var sel = document.getElementById('selHabr');
      url = url + `&total=${sel.options[sel.selectedIndex].text}`;
    }

    url = url + `&hqna=${ch4.checked}`;
    if (ch4.checked) {
      var sel = document.getElementById('selHQNA1');
      url = url + `&answer=${sel.options[sel.selectedIndex].text}`;
      var sel = document.getElementById('selHQNA2');
      url = url + `&quan=${sel.options[sel.selectedIndex].text}`;
    }

    window.location.href = url;
  }
  else {
    alert('Oops, no services included for troubleshooting (');
  }
}
