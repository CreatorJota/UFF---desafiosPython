# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

notas = input().split(" ")
notas = [float(i) for i in notas]
nUm, nDois, nTres, nQuatro = notas
media = ((nUm * 2) + (nDois * 3) + (nTres * 4) + nQuatro) / 10
print('Media: {:.1f}'.format(media))
if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
elif media >= 5 or media <= 6.9:
    print("Aluno em exame.")
    notaExame = float(input())
    print('Nota do exame:', notaExame)
    mediaFinal = (notaExame + float(media)) / 2
    if mediaFinal >= 5:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(mediaFinal))
    else:
        print("Aluno reprovado.")
        print('Media final: {:.1f}'.format(mediaFinal))

