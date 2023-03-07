def count_letters():
    str = input()
    lwr_pt = re.compile("[a-z]")
    upp_pt = re.compile("[A-Z]")
    lwr = lwr_pt.findall(str)
    upp = upp_pt.findall(str)
    print(f'Num of lower chars = {len(lwr)}, Num of upper chars = {len(upp)}')