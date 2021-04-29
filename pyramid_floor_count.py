blocks = int(input("Enter the number of blocks: "))

blocks_range = range(blocks)

height = 0

counter = 0

for x in range(1, blocks):

    if counter <= blocks:

        counter += x
        height += 1

    else:
        height -= 1
        break


print("The height of the pyramid:", height)
