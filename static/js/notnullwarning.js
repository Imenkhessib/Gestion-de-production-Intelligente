$(function validateForm() {
  var reference = document.forms["itemform"]["ref"].value;
  var designation = document.forms["itemform"]["desig"].value;
  var qty = document.forms["itemform"]["quantity"].value;
  if (reference == "") {
    alert("Reference must be filled out");
    return false;
  }
}