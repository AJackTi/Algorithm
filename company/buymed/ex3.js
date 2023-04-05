let input = [4, 5, 1, 2, 3]

const getSortedLength = (arr) => {
    let count = 1
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] > arr[i - 1]) {
            count++
        } else {
            count = 1
        }
        if (i === arr.length - 1) {
            return count
        }
    }
}

let max = 0
for (let i = 0; i < input.length - 1; i++) {
    let newArr = input.slice(i + 1, input.length).concat(input.slice(0, i + 1));
    let maxOfArr = getSortedLength(newArr)
    max = maxOfArr > max ? maxOfArr : max;
}

console.log(`The max continuous ascending is:`, max);