def logHandler(path):
    line = open(path).read().split('\n')
    err_ids = []
    for i in line:
        if 'ERROR:' in i:
            err_id = i.split()[2]
            err_ids.append(err_id)
    file = open('output.log', 'w+')
    for i in err_ids:
        group_list = []
        for j in line:
            if i in j:
                group_list.append(j)
        if len(group_list) >= 4:
            group_list = group_list[-4:]
            group_list[-1] = group_list[-1] + '  -------  '
        else:
            group_list[-1] = group_list[-1] + ' // There are only {} messages before the error -------  '.format(
                len(group_list) - 1)
        for k in group_list:
            file.write(k + '\n')
    file.close()
    file = open('output.log', 'r')
    output_string = file.read()
    return output_string
