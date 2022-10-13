let clickbutton = document.getElementById("btn");
let counter = 0;

clickbutton.addEventListener("click", function() {
    counter++;
    console.log(counter);
    document.getElementById('clickedNum').innerHTML = "You clicked the button " + counter + " times";});