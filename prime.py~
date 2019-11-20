import time, math, bitarray
from bitarray import bitarray

class Linked_List:
    def __init__(self):
        self.first = None
        self.last = self.first
        self.curr_node = self.first
        self.size = 0
    
    def add(self, value):
        if self.first is None:
            self.first = Linked_List_Node(value)
            self.curr_node = self.first
            self.last = self.first
        else:
            self.last.next = Linked_List_Node(value)
            self.last = self.last.next
        self.size += 1
    
    def reset_pointer(self):
        self.curr_node = self.first

    def has_next(self):
        return self.curr_node is not None

    def next(self):
        ret = self.curr_node.value
        self.curr_node = self.curr_node.next
        return ret

    def get_last(self):
        return self.last.value

    def print_list(self):
        while self.has_next():
            print(self.next(), end=" ")
        print()
        self.reset_pointer()

class Linked_List_Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Primes:
    def __init__(self, num):
        self.segment_size = max(6, math.ceil(math.sqrt(num)))
        self.domain = bitarray(self.segment_size)
        for i in range(0, 4):
            self.domain[i] = 1
        for i in range(4, self.segment_size):
            self.domain[i] = 0

        self.primes = Linked_List()
        self.primes.add(2)
        self.primes.add(3)
        self.offset = 0
        self.num_required_primes = math.ceil(math.sqrt(num))
    
    def get_prime(self, amt):
        num_primes_last_segment = 0
        count = 2
        i = 0
        while count < amt:
            curr_prime = 2

            domain_start = self.segment_size * self.offset
            domain_end = self.segment_size * (self.offset + 1)

            while self.primes.has_next() and curr_prime * curr_prime < domain_end:
                curr_prime = self.primes.next()

                starting_index = 0
                if domain_start % curr_prime != 0:
                    starting_index = curr_prime - domain_start % curr_prime

                for i in range(starting_index, self.segment_size, curr_prime):
                    #print("Marking %d for # %d"%(i + domain_start, curr_prime))
                    self.domain[i] = 1 # Marking with 1 means it is composite.


            self.primes.reset_pointer()
            num_primes_last_segment = self.expand_primes()
            #print(self.domain)
            #self.primes.print_list()
            count += num_primes_last_segment
            if count >= amt:
                break

            last_prime = self.primes.get_last()
            if last_prime * last_prime > domain_end:
                self.offset += 1
                self.domain.setall(0)

        prime_index = num_primes_last_segment - (count - amt)
        find = 0
        while prime_index > 0:
            if self.domain[find] == 0:
                prime_index -= 1
            find += 1
        find -= 1
        print("The %dth Prime Number is %d" %(amt, self.segment_size * self.offset + find))
    
    def expand_primes(self):
        count = 0
        for i in range(0, self.segment_size):
            if self.domain[i] == 0:
                prime = i + self.segment_size * self.offset
                for j in range(i + prime, self.segment_size, prime):
                    self.domain[j] = 1
                
                if (self.primes.size < self.num_required_primes):
                    self.primes.add(i + self.segment_size * self.offset)
                count += 1
        
        return count

def run():
    n = int(input("What nth prime number would you like? "))
    prime_sim = Primes(n)
    
    start_time = time.time()
    prime_sim.get_prime(n)
    print("--- %s seconds ---"%(time.time() - start_time))

if __name__ == "__main__":
    run()
