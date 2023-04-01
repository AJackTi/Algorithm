class Node {
    constructor(value) {
        this.value = value
        this.next = null
    }
}

class LinkedList {
    constructor(value) {
        const newNode = new Node(value)
        this.head = newNode
        this.tail = this.head
        this.length = 1
    }

    push(value) {
        const newNode = new Node(value)
        if(!this.head) {
            this.head = newNode
            this.tail = newNode
        } else {
            this.tail.next = newNode
            this.tail = newNode
        }
        this.length++
        return this
    }

    pop() {
        if(!this.head) return undefined
        let temp = this.head
        let pre = this.head
        while(temp.next) {
            pre = temp
            temp = temp.next
        }
        this.tail = pre
        this.tail.next = null
        this.length--
        if(this.length == 0) {
            this.head = null
            this.tail = null
        }
        return temp
    }

    unshift(value) {
        let newNode = new Node(value)
        if(this.length == 0) { // !this.head
            this.head = newNode
            this.tail = newNode
        } else {
            newNode.next = this.head
            this.head = newNode
        }
        this.length++
        return this
    }

    shift() {
        if(!this.head) {
            return undefined
        }
        let temp = this.head
        this.head = this.head.next
        temp.next = null
        this.length--
        if(this.length === 0) {
            this.tail = null
        }
        return temp
    }

    get(index) {
        if(index < 0 || index > this.length) return undefined
        let i = 0
        let currentNode = this.head
        while(currentNode) {
            if(i == index) {
                return currentNode
            }
            currentNode = currentNode.next
            i++
        }
    }

    set(index, value) {
        let temp = this.get(index)
        if(temp) {
            temp.value = value
            return true
        }
        return false
    }

    insert(index, value) {
        if(index < 0 || index > this.length) return false
        if(index === 0) return this.unshift(value)
        if(index === this.length) return this.push(value)
        
        const newNode = new Node(value)
        const temp = this.get(index - 1)

        newNode.next = temp.next
        temp.next = newNode
        this.length++
        return true
    }

    remove(index) {
        if(index < 0 || index > this.length) return false
        if(index === 0) return this.shift()
        if(index === this.length) return this.pop()

        const preNode = this.get(index-1)
        const next = preNode.next

        preNode.next = next.next
        next.next = null
        this.length--
    }

    reverse() {
        let temp = this.head
        this.head = this.tail
        this.tail = temp

        let next = temp.next
        let prev = null
        for(let i = 0; i < this.length; i++) {
            next = temp.next
            temp.next = prev
            prev = temp
            temp = next
        }
        return this
    }
}

//let linkedList = new LinkedList(4)
// linkedList.push(10)
// console.log(linkedList);
// linkedList.pop()
// console.log(linkedList);
// linkedList.pop()
// console.log(linkedList);
// linkedList.unshift(10)
// console.log(linkedList);
// linkedList.unshift(11)
// console.log(linkedList);
// linkedList.shift()
// console.log(linkedList);
// linkedList.shift()
// console.log(linkedList);
// linkedList.shift()
// console.log(linkedList);

let linkedList = new LinkedList(4)
linkedList.push(5)
linkedList.push(6)
linkedList.push(7)
// console.log(linkedList.get(0));
// console.log(linkedList.get(1));
// console.log(linkedList.get(2));
// console.log(linkedList.get(3));
// console.log(linkedList.get(4));
// console.log(linkedList.get(-1));
// linkedList.insert(1, 111)
linkedList.insert(0, 111)
console.log(linkedList);
console.log(linkedList.reverse());