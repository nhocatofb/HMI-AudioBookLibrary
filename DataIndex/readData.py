# Last line of file must be a line break

filename = "DataIndex.txt"

with open(filename, 'r', encoding='UTF-8') as file:
    for line in file:
        agrs = line.split(' - ')
        # Tên sản phẩm - tác giả - thể loại - thời lượng - đường dẫn tới speech file
        name = agrs[0]
        author = agrs[1]
        bookType = agrs[2]
        length = agrs[3]
        dir = agrs[4][:-1]
        print(name, author, bookType, length, dir)