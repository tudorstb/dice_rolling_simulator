#V1_one dice

import random
nr_1='''
 ___________
|           |
|     *     |
|           |
 ___________
'''
nr_2='''
 ___________
|           |
|   *    *  |
|           |
 ___________
'''

nr_3='''
 ___________
|     *     |
|     *     |
|     *     |
 ___________
'''

nr_4='''
 ___________
|  *     *  |
|           |
|  *     *  |
 ___________

'''
nr_5='''
 ___________
|  *     *  |
|     *     |
|  *     *  |
 ___________
'''

nr_6='''
 ___________
|  *     *  |
|  *     *  |
|  *     *  |
 ___________
'''

numere=[nr_1,nr_2,nr_3,nr_4,nr_5,nr_6]


while True:
    text = input("Press enter to roll the dice:")
    print('To exit the game press anyting else')
    if text == "":
        numar_secret_1=random.randrange(1,6)
        numar_secret_2=random.randrange(1,6)

        print(numere[numar_secret_1-1]+numere[numar_secret_2-1])
    else:
        break



