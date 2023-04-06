var page = document.getElementById("current_page");
page.style.display = "none";

page_number = page.innerText;
console.log(page_number);

target_id = "page_number_" + String(page_number);
var target = document.getElementById(target_id);
target.style.color = "#f00";
