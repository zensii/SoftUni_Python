chicken_pcs = int(input())
fish_pcs = int(input())
veggie_pcs = int(input())

# prices

chicken_menu = 10.35
fish_menu = 12.4
veggie_menu = 8.15
delivery = 2.5
dessert = 0.2

total_cost_menu = (chicken_pcs*chicken_menu) + (fish_pcs*fish_menu) + (veggie_pcs*veggie_menu)
total_cost = total_cost_menu + (total_cost_menu*dessert) + delivery

print(total_cost)


