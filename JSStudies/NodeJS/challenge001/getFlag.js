// Exportando função

function getFlagValue(flag){
    const flagIndex = process.argv.indexOf(flag);
    return process.argv[flagIndex+1];
}

module.exports = getFlagValue;