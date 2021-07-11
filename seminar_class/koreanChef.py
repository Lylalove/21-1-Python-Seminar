from chef import Chef

class KoreanChef(Chef):
    # override 된 것.
    def make_special_dish(self):
        print("Chef is making today's special! (등갈비김치찜)")

    def make_bulgogi(self):
        print("Chef is making bulgogi")