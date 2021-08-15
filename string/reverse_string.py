# def reverse_string(strs) -> None:
#     strs = strs[::-1]

# using two point SWAP method
def reverse_string_pointer(strs) -> None:
    left, right = 0, len(strs) - 1
    while left < right:
        strs[left], strs[right] = strs[right], strs[left]
        left += 1
        right -= 1

    print(strs)

strs = ['H', 'a', 'n', 'n', 'a', 'h']
reverse_string_pointer(strs)