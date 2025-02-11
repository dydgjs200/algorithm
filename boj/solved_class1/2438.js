const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.question("", (N) => {
  N = Number(N);

  for (let i = 1; i <= N; i++) {
    console.log("*".repeat(i));
  }
});
