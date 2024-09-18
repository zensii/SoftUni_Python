from collections import deque

substrings = deque(input().split())

main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']

found_colors = []

def search_color(first_sub, last_sub=''):

    color = first_sub + last_sub
    color_reverse = last_sub + first_sub
    if color in main_colors or color in secondary_colors:
        return color
    if color_reverse in main_colors or color_reverse in secondary_colors:
        return color_reverse


def process_substring(first_sub, last_sub=''):

    first_sub = first_sub[:-1]
    last_sub = last_sub[:-1]

    middle = len(substrings) // 2

    substrings.rotate(-middle)
    if last_sub != '':
        substrings.appendleft(last_sub)
    if first_sub != '':
        substrings.appendleft(first_sub)
    substrings.rotate(middle)


def check_primary(color):

    if color in main_colors:
        return True
    else:
        if color == 'orange':
            if 'red' in found_colors and 'yellow' in found_colors:
                return True
        elif color == 'purple':
            if 'red' in found_colors and 'blue' in found_colors:
                return True
        elif color == 'green':
            if 'yellow' in found_colors and 'blue' in found_colors:
                return True
    return False


while substrings:

    if len(substrings) > 1:
        first, last = substrings.popleft(), substrings.pop()
        found_color = search_color(first, last)
        if found_color:
            found_colors.append(found_color)
        else:
            process_substring(first, last)

    else:
        first = substrings.pop()
        found_color = search_color(first)
        if found_color:
            found_colors.append(found_color)
            process_substring(first)


filtered_colors = list(filter(check_primary, found_colors))
print(filtered_colors)