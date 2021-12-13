var input = document.querySelector("#input");
var output = document.querySelector("#output");

async function convert(){
    output.value = await eel.convertWord(input.value)();
}

function initialize(){
    input.value = "Enter a word: ";
    output.value = "No output yet";
}
initialize()