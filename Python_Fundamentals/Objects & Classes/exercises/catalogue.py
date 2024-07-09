class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        searched_list = []
        for item in self.products:
            if item.lower().startswith(first_letter.lower()):
                searched_list.append(item)
        return searched_list

    def __repr__(self):
        sorted_list = sorted(self.products)
        return f"Items in the {self.name} catalogue:" + "\n" + "\n".join(sorted_list)


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
print(catalogue.get_by_letter("M"))
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
