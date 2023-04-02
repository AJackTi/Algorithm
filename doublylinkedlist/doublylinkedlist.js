class Node {
    constructor(value) {
        this.value = value
        this.next = null
        this.prev = null
    }
}

class DoublyLinkedList {
    constructor(value) {
        const newNode = new Node(value)
        this.head = newNode
        this.tail = this.head
        this.length = 1
    }

    push(value) {
        let newNode = new Node(value)
        if (!this.head) {
            this.head = newNode
            this.tail = newNode
        } else {
            this.tail.next = newNode
            newNode.prev = this.tail
            this.tail = newNode
        }
        this.length++
            return this
    }

    pop() {
        if (!this.head || !this.tail || this.length === 0) {
            return undefined
        }
        let temp = this.tail
        if (this.length === 1) {
            this.head = null
            this.tail = null
        } else {
            this.tail = this.tail.prev
            this.tail.next = null
            temp.prev = null
        }
        this.length--
            return temp
    }

    unshift(value) {
        let newNode = new Node(value)
        if (!this.head) {
            this.head = newNode
            this.tail = newNode
        } else {
            newNode.next = this.head
            this.head.prev = newNode
            this.head = newNode
        }

        this.length++
            return this
    }

    shift() {
        if (!this.head) {
            return undefined
        }
        if (!this.head.next) {
            this.head = null
            this.tail = null
        } else {
            const temp = this.head.next
            temp.prev = null
            this.head.next = null
            this.head = temp
        }
        this.length--
            return this
    }

    get(index) {
        if (0 > index || index >= this.length) {
            return undefined
        }

        let temp = this.head
        if (index < this.length / 2) {
            for (let i = 0; i < index; i++) {
                temp = temp.next
            }
        } else {
            temp = this.tail
            for (let i = this.length - 1; i > index; i--) {
                temp = temp.prev
            }
        }

        return temp
    }

    set(index, value) {
        let temp = this.get(index)
        if (temp) {
            temp.value = value
            return true
        }
        return false
    }

    insert(index, value) {
        if (index === 0) return this.unshift(value)
        if (index === this.length) return this.push(value)
        if (index < 0 || index > this.length) return false

        const newNode = new Node(value)
        const before = this.get(index - 1)
        const after = before.next
        before.next = newNode
        newNode.next = after
        newNode.prev = before
        after.prev = newNode
        this.length++;
        return true
    }

    remove(index) {
        if (index === 0) return this.shift();
        if (index === this.length) return this.pop(index);
        if (index < 0 || index > this.length) return false;

        let before = this.get(index - 1);
        let after = this.get(index + 1);
        let temp = this.get(index)
        before.next = after
        after.prev = before
        temp.next = null
        temp.prev = null
        return true
    }
}

let doublyLinkedList = new DoublyLinkedList(1);
// console.log(doublyLinkedList);
doublyLinkedList.push(2)
doublyLinkedList.push(3)
doublyLinkedList.push(4);
// console.log(doublyLinkedList);
// doublyLinkedList.pop()
// console.log(doublyLinkedList);
// doublyLinkedList.pop()
// console.log(doublyLinkedList);
doublyLinkedList.get(1)
doublyLinkedList.set(1, 100)
doublyLinkedList.insert(1, 111)
doublyLinkedList.remove(1)