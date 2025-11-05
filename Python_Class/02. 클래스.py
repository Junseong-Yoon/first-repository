class Shoes_shop:

    def __init__(self, model, size, color):
        self.model = model
        self.size = size
        self.color = color

    def __str__(self):
        return f"[{self.model}], [{self.size}], [{self.color}]"
    
    def color_change(self, new_color):
        self.color = new_color

customer1 = Shoes_shop('Nike', '270', 'red')
customer1.color_change('black')

print(customer1)




class Shoes_shop:

    def __init__(self, model, size, color):
        self.model = model
        self.size = size
        self.color = color

    def color_change(self, new_color):
        self.old = self.color
        self.color = new_color
        print(f'나는 {self.model}제품 {self.size}신고 {self.old}인데{new_color}로 바꿀래')

customer2 = Shoes_shop('Nike', '270', 'red')
customer2.color_change('black')

print(customer2)