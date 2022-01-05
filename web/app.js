//initializes variables for key elements
var input = document.querySelector("#input");
var output = document.querySelector("#output");
//converts the inputed word to Pig Latin by communicating with the backend
async function convert(){
    output.value += `English to Pig Latin => Translated Word: ${await eel.convertWord(input.value)()}\n`;
    output.value += "Enter another word to continue, or click the stop button\n\n";
    initialize()
}
//stops the loop and returns the amount of words translated
async function stop(){
    output.value += `Total number of words converted ${await eel.returnWords()()}\n`;
}
//converts the inputed word back to English by communicating with the backend
async function reverse(){
    output.value += `Pig Latin to English => Translated Word: ${await eel.convertBack(input.value)()}\n`;
    output.value += "Enter another word to continue, or click the stop button\n\n";
    initialize()
}
//Resets the input field
function initialize(){
    input.value = "Enter a word here: ";
}
initialize()