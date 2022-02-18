//появление 1-го поп-апа
document.getElementById("elastic").onclick = function (){
    var theMenu = document.getElementById("myMenu");
    if(theMenu.style.display == 'none') {
        theMenu.style.display = 'block';
    }
    else {
        theMenu.style.display = 'none';
    }
}

//появление 2-го поп-апа
document.getElementById("wheretogo").onclick = function (){
    var theMenu = document.getElementById("myMenu2");
    if(theMenu.style.display == 'none') {
        theMenu.style.display = 'block';
    }
    else {
        theMenu.style.display = 'none';
    }
}

//сортировка 1-го поп-апа
document.querySelector("#elastic").oninput = function (search){
  let val = this.value.trim();
  let elasticItems = document.querySelectorAll('.elastic li');
  if (val != '') {
      elasticItems.forEach(function (elem) {
          if (elem.innerText.search(val) == -1){
              elem.classList.add('hide');
          }
          else {
               elem.classList.remove('hide');
          }
      });
  }
  else {
      elasticItems.forEach(function (elem) {
          elem.classList.remove('hide');
      });
  }
}

//сортировка 2-го поп-апа
document.querySelector("#wheretogo").oninput = function (search){
  let val = this.value.trim();
  let elasticItems = document.querySelectorAll('.elastic2 li');
  if (val != '') {
      elasticItems.forEach(function (elem) {
          if (elem.innerText.search(val) == -1){
              elem.classList.add('hide');
          }
          else {
               elem.classList.remove('hide');
          }
      });
  }
  else {
      elasticItems.forEach(function (elem) {
          elem.classList.remove('hide');
      });
  }
}

//вписывание слов в input
function insert (word) {
    let inp = document.querySelector('#elastic');
    let start = inp.selectionStart;
    inp.value = inp.value.substring(0, start) + word +
      inp.value.substring(inp.selectionEnd, inp.value.length) 
      inp.focus();
      inp.setSelectionRange(start, start + word.length)
  }

//вписывание слов в input
function insert2 (word) {
    let inp = document.querySelector('#wheretogo');
    let start = inp.selectionStart;
    inp.value = inp.value.substring(0, start) + word +
      inp.value.substring(inp.selectionEnd, inp.value.length) 
      inp.focus();
      inp.setSelectionRange(start, start + word.length)     
}

//меняет местами значения input-ов
document.getElementById("switch").onclick = function (){
    [
      document.getElementById("elastic").value,
      document.getElementById("wheretogo").value
    ] = [
      document.getElementById("wheretogo").value,
      document.getElementById("elastic").value
    ];
};


function sendToPage(){
  var input2 = document.getElementById("wheretogo").value;
  //alert(input);
  if (input2 == "Латвия(LV)"){
      location.href = "/latvia.html";
      return false;
  }

  if (input2 == "Испания(S)"){
    location.href = "/spain.html";
    return false;
  }

  if (input2 == "США(US)"){
    location.href = "usa.html";
    return false;
  }

  if (input2 == "Нидерланды(NL)"){
    location.href = "/netherlands.html";
    return false;
  }

  if (input2 == "Норвегия(NO)"){
    location.href = "/norway.html";
    return false;
  }

  if (input2 == "Румыния(RO)"){
    location.href = "/romania.html";
    return false;
  }

  if (input2 == "Россия(RU)"){
    location.href = "/russia.html";
    return false;
  }

}