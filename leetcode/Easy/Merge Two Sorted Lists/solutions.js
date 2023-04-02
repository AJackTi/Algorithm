var mergeTwoLists = function(list1, list2) {
    let combined = []
    let i = 0
    let j = 0
    while(i < list1.length && j < list2.length) {
        if(list1[i] < list2[j]) {
            combined.push(list1[i])
            i++
        } else {
            combined.push(list2[j])
            j++
        }
    }

    while(i < list1.length) {
        combined.push(list1[i])
        i++
    }

    while(j < list2.length) {
        combined.push(list2[j])
        j++
    }
    
    return combined
};

console.log(mergeTwoLists([1,2,4], [1,3,4]));