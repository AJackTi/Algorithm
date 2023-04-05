// let input = "((3+2)-5)+(9-3)" // => (3+2)
// let input = "((1+(10-5))-4+3)-(2+7)" // => (10-5)
let input = "(2+7)+((1+(10-5))-4+3)" // => (10-5)

input = input.trim()
let max = 0
let count = 0

let dict = {}

for (let i = 0; i < input.length; i++) {
    // check bigger index of '('
    if (input[i] == "(") {
        count += 1
    }

    // reset
    if (input[i] == ")") {
        dict[i] = count
        count = 0
    }
}

console.log(dict);

const getMax = Object.keys(dict)
    .filter(x => {
        return dict[x] == Math.max.apply(null,
            Object.values(dict));
    })

// ((3+2)-5)+(9-3)
let indexMostCharacter = getMax;
let result = '('
for (let i = 0; i <= indexMostCharacter; i++) {
    if (input[i] == '(') {
        result = "("
        continue
    }

    result += input[i]
}

console.log(result);;