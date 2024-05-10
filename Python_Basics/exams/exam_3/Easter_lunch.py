cakes = int(input())
egg_boxes = int(input())
cookies = int(input())

cake_price = 3.2
eggs_price12 = 4.35
cookies_price = 5.4
egg_paint = 0.15
eggs = egg_boxes * 12
paint_price = eggs * egg_paint

total = cakes * cake_price + cookies * cookies_price + egg_boxes * eggs_price12 + paint_price

print(f'{total:.2f}')
