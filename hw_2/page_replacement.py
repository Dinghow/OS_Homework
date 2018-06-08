import random

# Block class
class Block:
    def __init__(self,time):
        # page of this block
        self.page  = -1
        # Accessed or not
        self.accessed = False
        # Record the access order
        self.time = time

# Create a stimulator class
class Simulator:
    def __init__(self):
        # Create the blocks sequence
        self.blocks = [Block(4),Block(3),Block(2),Block(1)]
        # Record whether the blocks are all accessed or not
        self.accessed_all = False
        # page faults counter
        self.missing_page_counter = 0

    # Check if all the blocks are accessed
    def accessed_all_check(self):
        flag = True
        for i in self.blocks:
            if not i.accessed:
                flag = False
        self.accessed_all = flag

    # Access a new page
    def access_new_page(self,new_page,algorithm):
        replacement = True
        self.accessed_all_check()
        for i in self.blocks:
            # Check whether the blocks are not accessed
            if not self.accessed_all:
                # If already exist
                if i.page == new_page:
                    replacement = False
                    break
                elif not i.accessed:
                    i.page = new_page
                    i.accessed = True
                    replacement = False
                    break
            # Check if the new page is already in the blocks
            elif i.page == new_page:
                replacement = False
                if algorithm == 1:
                    i.time = 1
                    for j in self.blocks:
                        if not j == i:
                            j.time += 1

        if replacement:
            self.missing_page_counter += 1
            # Use FIFO replacement algorithm
            if algorithm == 0:
                for i in self.blocks:
                    if i.time == 4:
                        i.page = new_page
                        i.time = 1
                        for j in self.blocks:
                            if not j == i:
                                j.time += 1
                        break

            # Use LRU replacement algorithm
            elif algorithm == 1:
                max_value = max(self.blocks[i].time for i in range(4))
                for i in self.blocks:
                    if i.time == max_value:
                        i.page = new_page
                        i.time = 1
                        for j in self.blocks:
                            if not j == i:
                                j.time += 1
                        break
            else:
                raise print("Algorithm type error!")

# Generate the instructions access sequence and relevant pages sequence
def generate_list():
    m = random.randint(1, 318)
    instructions = list()
    pages = list()
    instructions.append(m)
    pages.append(int(m / 10))
    instructions.append(m + 1)
    pages.append(int((m + 1) / 10))
    while len(instructions) <= 316:
        m1 = random.randint(0, m - 1)
        instructions.append(m1)
        instructions.append(m1 + 1)
        pages.append(int(m1/10))
        pages.append(int((m1 + 1) / 10))
        m2 = random.randint(m1 + 2, 318)
        instructions.append(m2)
        instructions.append(m2 + 1)
        pages.append(int(m2 / 10))
        pages.append(int((m2 + 1) / 10))
        m = m2
    return instructions,pages
    