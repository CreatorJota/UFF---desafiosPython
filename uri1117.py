def recebe_notas():
    nota = float(input())
    if nota < 0 or nota > 10:
        print('nota invalida')
        recebe_notas()
    elif len(media) < 1:
        media.append(nota)
        recebe_notas()
    else:
        media.append(nota)
        calculo_media(media)


def calculo_media(arr):
    med = 0
    for i in arr:
        med += i
    return print('media = %.2f' % (med / 2))


if __name__ == '__main__':
    media = []
    recebe_notas()
