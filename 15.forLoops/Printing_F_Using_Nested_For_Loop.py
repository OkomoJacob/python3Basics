nums = [5, 2, 5, 2, 2]
for x_count in nums:
    output = ''
    for count in range(x_count):
        output += 'X'  # We are appending 'x' after every index
    print(output)

