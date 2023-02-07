# program to convert grade percent to gpa scale
# author: Courtney Hoppus

def main():
    valid = False
    gpa = None
    percent = None

    # validate input
    while valid == False:
        number = input('Enter the percentage earned: ')
        try:
            percent = float(number)
            valid = percent >= 0.0 and percent <= 100.0
            if valid == False:
                print('Must enter a valid number between 0 and 100. ')
        except:
            print('Must enter a number. ')

    # upper and lower limit cases
    if percent < 65.0:
        gpa = 0.0
    elif percent >= 95.0:
        gpa = 4.0

    # check value of percent to gpa
    # start at lowest base score 65.0 which is a gpa of 1.0
    # as the score increases by 1, the gpa increases by 0.1
    else:
        base_percent = 65.0
        gpa = 1.0
        multiplier = 0.1
        
        gpa += ((percent - base_percent) * multiplier)


    # print result
    print('Percent is:', percent, 'and the GPA is:', round(gpa, 1))
    
if __name__ == '__main__':
    main()
