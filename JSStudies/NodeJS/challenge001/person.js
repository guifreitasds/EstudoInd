const getFlagValue = require("./getFlag");

const name = getFlagValue("--name");

const greeting = getFlagValue("--greeting");

console.log(`Olá meu nome é ${name}. ${greeting}`)
