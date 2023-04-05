const input = [5, 2, 7, -4, 2, 7, 0, 6, 1, 3, 7, 6]

// Find the max of array
max = -Math.pow(10, 6)
for (let i = 0; i < input.length; i++) {
    if (input[i] > max) {
        max = i
    }
}

// Find the the second-largest number
let min = -Math.pow(10, 6)
let indices = {}
for (let i = 0; i < input.length; i++) {
    if (input[i] < max && input[i] > min) {
        min = input[i]
    }

    if (!indices[input[i]]) {
        indices[input[i]] = [i]
    } else {
        indices[input[i]].push(i)
    }
}

console.log(max);
console.log(min);

// Result: The index of the second-largest number
console.log(indices[min]);