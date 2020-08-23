##################ENJOY#####################                                                             
print(" oo_________________________________________________ooo_____oooo_ \n oo_______ooooo__oo_ooo___ooooo__oo_______o__ooooo___oo____oo____  \n oo______oo___oo_ooo___o_oo____o_oo__oo___o_oo___oo__oo___ooooo__   \n oo______oo___oo_oo____o_ooooooo_oo__oo___o_oo___oo__oo___oo_____  \n oo______oo___oo_oo____o_oo_______oo_oo__o__oo___oo__oo___oo_____  \n ooooooo__ooooo__oo____o__ooooo____oo__oo____ooooo__ooooo_oo_____ \n  ________________________________________________________________")
import random
count=0
while True:  
                    print("Enter a number between 1 to 6")
                    num=int(input())
                    x = str(random.randint(1, 6))
                    print("Rolling the dice...........")
                    if num == x:
                            print("Number =  ", x)
                            print("You Won!!!!!!")
                            count = count + 1
                            print("Your Score is : ", count)
                            
                    elif(num<=0 or num>6):
                        print("wrong input")
                            
                    else:
                        print("Your choice is wrong")
                        print("Computer choice is: ", x)
                        print("Youre Score is : ", count)
                    
                    z = input(("Play Again? y/n: ").lower())
                    if(z=="n"):
                        break
