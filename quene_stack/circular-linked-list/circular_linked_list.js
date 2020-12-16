/**
 * @param {number} k
 */
var MyCircularQueue = function(k) {
    this.size = k;
    this.data = new Array(k);
    this.headIndex = 0;
    this.tailIndex = 0;
    
    return this;
};

/** 
 * @param {number} value
 * @return {boolean}
 */
MyCircularQueue.prototype.enQueue = function(value) {

    if (this.isFull()) {
        return false;
    } else if (this.isEmpty()) {
        this.data[this.tailIndex] = value;
        return true;

    } else {
        if (this.tailIndex + 1 < this.size) {
            this.tailIndex = this.tailIndex + 1;
        } else {
            this.tailIndex = this.tailIndex + 1 - this.size
        }

        this.data[this.tailIndex] = value;

        return true;
    }
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.deQueue = function() {
    const space = this.tailIndex === this.headIndex;
    // const isEmpty = space && (this.data[this.tailIndex] !== 0 && !this.data[this.tailIndex])

    if (this.isEmpty()) {
        return false
    } else {
        this.data[this.headIndex] = '';
        
        if (space) {

        } else if (this.headIndex + 1 < this.size) {
            this.headIndex++;
        } else {
            this.headIndex = this.headIndex - this.size + 1
        }

        return true;
    }
};

/**
 * @return {number}
 */
MyCircularQueue.prototype.Front = function() {
    const space = this.tailIndex === this.headIndex;
    const isEmpty = space && (space && (this.data[this.tailIndex] !== 0 && !this.data[this.tailIndex]));

    if (isEmpty) {
        return -1;
    } else {
        return this.data[this.headIndex];
    }
};

/**
 * @return {number}
 */
MyCircularQueue.prototype.Rear = function() {

    if (this.isEmpty()) {
        return -1;
    } else {
        return this.data[this.tailIndex];
    }
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.isEmpty = function() {
    const space = this.tailIndex === this.headIndex;
    const isEmpty = space  && (this.data[this.tailIndex] !== 0 && !this.data[this.tailIndex]);

    return isEmpty;
};

/**
 * @return {boolean}
 */
MyCircularQueue.prototype.isFull = function() {
    const space = this.tailIndex - this.headIndex;
    const isFull = space === -1 || space === this.size - 1;

    return isFull;
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * var obj = new MyCircularQueue(k)
 * var param_1 = obj.enQueue(value)
 * var param_2 = obj.deQueue()
 * var param_3 = obj.Front()
 * var param_4 = obj.Rear()
 * var param_5 = obj.isEmpty()
 * var param_6 = obj.isFull()
 */

var obj = new MyCircularQueue(3)

var param_1 = obj.enQueue(7)

var param_2 = obj.deQueue(2)

var param_3 = obj.Front()

var param_10 = obj.deQueue()


var param_23 = obj.Front()

var param_4 = obj.Rear()

var param_5 = obj.enQueue(0)

var param_6 = obj.isFull()

var param_6 = obj.deQueue()