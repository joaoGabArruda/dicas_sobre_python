max_size = 10
spacing = 3

print(
    "(a)" + " " * (max_size - 3 + spacing) +
    "(b)" + " " * (max_size - 3 + spacing) +
    "(c)" + " " * (max_size - 3 + spacing) +
    "(d)" + " " * (max_size - 3 + spacing)
    )

for i in range(1, max_size + 1):

    # Primeiro triângulo
    print("*" * i, end = " " * (max_size - i + spacing))

    # Segundo triângulo
    print("*" * (max_size - i + 1), end = " " * (i - 1 + spacing))

    # Terceiro triângulo
    print(" " * (i - 1) + "*" * (max_size - i + 1), end = " " * spacing)

    # Quarto triângulo
    print(" " * (max_size - i) + "*" * i)
    

SAIDA:
(a)          (b)          (c)          (d)
*            **********   **********            *
**           *********     *********           **
***          ********       ********          ***
****         *******         *******         ****
*****        ******           ******        *****
******       *****             *****       ******
*******      ****               ****      *******
********     ***                 ***     ********
*********    **                   **    *********
**********   *                     *   **********
