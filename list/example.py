def outList(list):
    print("\n------------------\n", list, "\n-----------------------\n")

if __name__ == '__main__':
    list = ['Zorro', 'Fabio', 'Mikele', 'Giovannino', 'Pasquale', 'Zio']
    outList(list)

    list.append('Pasqualino')
    outList(list)
    
    list.remove('Fabio')
    outList(list)

    list.insert(0, "Fortezza")
    outList(list)

    list.sort()
    outList(list)

    list.reverse()
    outList(list)