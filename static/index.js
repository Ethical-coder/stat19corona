function classTogglerMap(){
  id = this.id;
  console.log(id);
  id = id.slice(0,2);
  console.log(id)
  document.getElementById(id).classList.toggle('state-maps');
}

allDropdownItems = document.querySelectorAll('dropdown-item');
console.log(allDropdownItems);
alert("Created dropdown items.");
for(var i=0; i<allDropdownItems.length; i++){
  allDropdownItems[i].addEventListener("click",classTogglerMap);
}
alert("Added addEventListener");
