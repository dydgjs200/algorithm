const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on("line", (line) => {
  let input = line.split(" ").map(Number);
  console.log(input[0] + input[1]);
  rl.close();
});
