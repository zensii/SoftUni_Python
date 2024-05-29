def loading_bar(percent_complete):
    still_loading = ''
    full = f'{percent_complete}% '
    full_bars = percent_complete // 10 * '%'
    if complete == 100:
        print('100% Complete!')
        full = ''
    else:
        still_loading = '\nStill loading...'
    final_bar = full + '[' + full_bars + (10-(percent_complete//10)) * '.' + ']' + still_loading
    return final_bar


complete = int(input())
print(loading_bar(complete))


