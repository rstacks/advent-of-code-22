const fs = require("fs");
const readline = require("readline");

// Each stack is organized bottom-to-top
let stacks = {
    1: ["R", "G", "H", "Q", "S", "B", "T", "N"],
    2: ["H", "S", "F", "D", "P", "Z", "J"],
    3: ["Z", "H", "V"],
    4: ["M", "Z", "J", "F", "G", "H"],
    5: ["T", "Z", "C", "D", "L", "M", "S", "R"],
    6: ["M", "T", "W", "V", "H", "Z", "J"],
    7: ["T", "F", "P", "L", "Z"],
    8: ["Q", "V", "W", "S"],
    9: ["W", "H", "L", "M", "T", "D", "N", "C"]
};








const day5_input = fs.createReadStream("./day5/day5_input.txt");
const reader = readline.createInterface({
    input: day5_input,
    terminal: false
});

reader.on("line", (line) => {
    console.log(line);
});
