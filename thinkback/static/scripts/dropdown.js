/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show_t");
  }
  
  // Close the dropdown if the user clicks outside of it
  window.onclick = function(e) {
    if (!e.target.matches('.dropbtn_t')) {
    var myDropdown = document.getElementById("myDropdown");
      if (myDropdown.classList.contains('show_t')) {
        myDropdown.classList.remove('show_t');
      }
    }
  }