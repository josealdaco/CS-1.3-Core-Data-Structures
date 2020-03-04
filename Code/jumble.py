class Jumble():

    def __init__(self, path_file, four_words):
        self.path_file = path_file
        self.four_words = four_words
        self.actual_words = []
        self.sorted_four_words = [] # ['eisst', 'horsu', 'dlo', 'aert']
        self.counter = 0
        self.groups = set()
        self.phrase = ""
        
        for word in self.four_words:
            word = "".join(sorted(word))
            self.sorted_four_words.append(word)
        with open(self.path_file) as file:
            for line in file:
                word = line.strip().split()[0] # eht
                if "".join(sorted(word)) in self.sorted_four_words:
                    self.actual_words.append(word)
    
    def arrange_words(self):
        new_actual_words = []
        
        for w in self.sorted_four_words:
            for inner_w in self.actual_words:
                if sorted(w) == sorted(inner_w):
                    self.groups.add((w, inner_w))
                    new_actual_words.append(inner_w)
        return new_actual_words

    def get_word_bank(self):
        first_bank = [2,4,0,1,3,4,3,4]
        first_bank_table = {}
        circles_list = [2,3,1,2]
        circle_counter = 0 
        for w in self.arrange_words():
            first_bank_table[w] = circles_list[circle_counter]
            circle_counter += 1

        first_bank_output = []
        # second_bank = [1,2,3,0,2,0,1,2,4,5]
        for w in self.arrange_words():
            # print("--",w)
            for _ in range(first_bank_table[w]):
                first_bank_output.append(w[first_bank[0]])
                first_bank.pop(0)
        return first_bank_output

    # stretch challenge attempted :'( 
    # def get_phrase(self):
    #     self.phrase = "".join(self.get_word_bank())
    #     self.__init__(self.path_file, [self.phrase])
    #     return self.actual_words
                

if __name__ == "__main__":
    path = "words.txt"
    puzzle_one = ["tefon", "sokik", "niumem", "siconu"]
    jumble_one = Jumble(path, puzzle_one)
    jumble_one.get_word_bank()
    print("SOLUTION WORDS")
    for group in jumble_one.groups:
        print("---",group,"---")