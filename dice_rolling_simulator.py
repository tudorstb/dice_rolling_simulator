import random

r1_1=' ___________ '
r2_1='|           |'
r3_1='|     *     |'
r4_1='|           |'
r5_1=' ___________ '

face_1=[r1_1,r2_1,r3_1,r4_1,r5_1]


r1_2=' ___________ '
r2_2='|           |'
r3_2='|  *    *   |'
r4_2='|           |'
r5_2=' ___________ '

face_2=[r1_2,r2_2,r3_2,r4_2,r5_2]

r1_3=' ___________ '
r2_3='|     *     |'
r3_3='|     *     |'
r4_3='|     *     |'
r5_3=' ___________ '

face_3=[r1_3,r2_3,r3_3,r4_3,r5_3]

r1_4=' ___________ '
r2_4='|  *     *  |'
r3_4='|           |'
r4_4='|  *     *  |'
r5_4=' ___________ '

face_4=[r1_4,r2_4,r3_4,r4_4,r5_4]

r1_5=' ___________ '
r2_5='|  *     *  |'
r3_5='|     *     |'
r4_5='|  *     *  |'
r5_5=' ___________ '

face_5=[r1_5,r2_5,r3_5,r4_5,r5_5]

numbers=[face_1,face_2,face_3,face_4,face_5]
def alling(dice_2):
    for i in range(5):
        randuri[i]=randuri[i]+" "+ dice_2[i]

redo="Y"
#select dice number:
while redo=='Y' or redo=='y':
    dice_number=input("Hom many dices do you need:")
    try:
        dice_number=int(dice_number)
        dice_number_backup=dice_number
    except:
        print("Please enter a valid number")
        redo=input(f'Want to go again (Y/N):')
    else:
        while True:
            if redo=='Y' or redo=='y':
                dice_number=dice_number_backup
                randuri = ['', '', '', '', '']
                text = input("Press enter to roll the dice:")
                try:
                    assert text==""
                except:
                    print("Wrong key pressed")
                    redo = input(f'Want to go again (Y/N):')
                else:
                    while dice_number>0:
                        numar_secret=random.randrange(1,6)
                        alling(numbers[numar_secret-1])
                        dice_number-=1
                    for i in range(5):
                        print(randuri[i])
                    redo = input(f'Want to go again (Y/N):')
                    if redo == 'Y' or redo == 'y':
                        change=input("Want to change dice number (Y/N):")

                        redo_change_dice = "Y"
                        while True and redo_change_dice=="Y" or redo_change_dice=='y':
                            if change=='Y' or change == 'y':
                                dice_number_backup = input("Hom many dices do you need:")
                            try:
                                dice_number_backup=int(dice_number_backup)
                            except:
                                print("Please enter a valid number")
                                redo_change_dice = input(f'Want to go again (Y/N):')
                            else:
                                break




            else:
                break