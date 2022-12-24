const fs = require("fs");
const readline = require("readline");


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


function move_crates(line) {
    const instructs = line.split(" ");
    const num_to_move = Number(instructs[1]);
    const origin_stack = Number(instructs[3]);
    const destination_stack = Number(instructs[5]);
    for (let i = 0; i < num_to_move; i++) {
        const moving_crate = stacks[origin_stack].pop();
        stacks[destination_stack].push(moving_crate);
    }
}


function get_top_crates() {
    let ret = "";
    for (const stack_num in stacks) {
        const last_i = stacks[stack_num].length - 1;
        ret += stacks[stack_num][last_i];
    }
    return ret;
}


const day5_input = fs.createReadStream("./day5/day5_input.txt");
const reader = readline.createInterface({
    input: day5_input,
    terminal: false
});

let ln_num = 0;
reader.on("line", (line) => {
    const instruction = line.trim();
    move_crates(instruction);
    ln_num++;
    if (ln_num == 501) {
        console.log("The top crates are: " + get_top_crates());
    }
});
