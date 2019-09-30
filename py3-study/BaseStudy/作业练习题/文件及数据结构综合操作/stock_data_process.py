

data_list = []

with open("stock_data.data", "r", encoding="utf-8") as f:
    title = f.readline().split()
    data_list_new = [[] for _ in title]

    for line in f:
        line_list = line.split()
        data_list.append(line_list)
        for index, val in enumerate(line_list):
            data_list_new[index].append(val)

data_dict = dict(zip(title, data_list_new))
# for d in data_dict.items():
#     print(d)
# print(data_list)


while True:
    result_num = 0
    text = input('输入查询内容:')
    print(title)
    params = []
    for symbol in ['<', '>']:
        if symbol in text:
            params = text.split(symbol)
            params.append(symbol)
    if params:
        if params[-1] == '<':
            for index, name in enumerate(data_dict.get(params[0].strip())):
                if float(name) < float(params[1]):
                    result_num += 1
                    print(data_list[index])
        elif params[-1] == '>':
            for index, name in enumerate(data_dict.get(params[0].strip())):
                if float(name) > float(params[1]):
                    result_num += 1
                    print(data_list[index])
    else:
        for index, name in enumerate(data_dict.get('名称')):
            if text in name:
                result_num += 1
                print(data_list[index])
    print('找到%s条'%(result_num))






# data_list = []
# with open('stock_data.data', 'r', encoding='utf8') as f:
#     for line in f:
#         data_list.append(line.split())
# print(data_list)
# data_list_new = [[] for i in range(len(data_list[0]))]
#
# for data in data_list:
#     for index, d in enumerate(data):
#         data_list_new[index].append(d)
#
# data_dict = {}
# for d_new in data_list_new:
#     data_dict[d_new[0]] = d_new[1:]
#
# for k, y in data_dict.items():
#     print(k, y)



