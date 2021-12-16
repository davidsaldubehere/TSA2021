var input = document.querySelector("#input");
var output = document.querySelector("#output");

async function convert(){
    output.value += `English to Pig Latin => Translated Word: ${await eel.convertWord(input.value)()}\n`;
    output.value += "Enter another word to continue, or click the stop button\n\n";
}
async function stop(){
    output.value = `Total number of words converted ${await eel.returnWords()()}\n`;
}
async function reverse(){
    output.value += `Pig Latin to English => Translated Word: ${await eel.convertBack(input.value)()}\n`;
    output.value += "Enter another word to continue, or click the stop button\n\n";
}
function initialize(){
    input.value = "Enter a word here: ";
}
initialize()