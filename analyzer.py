 # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID: w2051853(UoW)         20231131(IIT)
# Date: 14/12/2023

# Global variables to keep track of counts and lists
global progress_count, trailer_count, retriever_count, exclude_count, progress_list, trailer_list, retriever_list, exclude_list

progress_data = (120, 0, 0)
trailer_data = ((100, 20, 0), (100, 0, 20))
retriever_data = ((80, 40, 0), (80, 20, 20), (80, 0, 40), (60, 60, 0), (60, 40, 20), (60, 20, 40),
                  (60, 0, 60), (40, 80, 0), (40, 60, 20), (40, 40, 40), (40, 20, 60), (20, 100, 0),
                  (20, 80, 20), (20, 60, 40), (20, 40, 60), (0, 120, 0), (0, 100, 20), (0, 80, 40), (0, 60, 60))
exclude_data = ((40, 0, 80), (20, 20, 80), (20, 0, 100), (0, 40, 80), (0, 20, 100), (0, 0, 120))

total_inputs = 0
progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0

progress_list = []
trailer_list = []
retriever_list = []
exclude_list = []

#function to get inputs from the user for pass, defer, and fail credits
def get_input():
    while True:
        try:
            pass_credits = int(input('\nPlease enter your credits at pass: '))
            if pass_credits not in range(0, 121, 20):
                print('Out of range!')
                continue
            while True:
                try:
                    defer_credits = int(input('Please enter your credits at defer: '))
                    if defer_credits not in range(0, 121, 20):
                        print('Out of range!')
                        continue
                    break
                except ValueError:
                    print('Integer required.')
            while True:
                try:
                    fail_credits = int(input('Please enter your credits at fail: '))
                    if fail_credits not in range(0, 121, 20):
                        print('Out of range!')
                        continue
                    break
                except ValueError:
                    print('Integer required.')
        except ValueError:
            print('Integer Required! Try again.')    #print approppriate error message
            continue

        if (pass_credits + defer_credits + fail_credits) == 120:
            return pass_credits, defer_credits, fail_credits
        else:
            print('Total incorrect! Check again.')

#display the appropriate progression outcome for an individual student
def student_version():
    global progress_count, trailer_count, retriever_count, exclude_count, progress_list, trailer_list, retriever_list, exclude_list
    pass_credits, defer_credits, fail_credits = get_input()
    
    valid_credits = (pass_credits, defer_credits, fail_credits)
    if valid_credits == progress_data:
        print('Progress')
        progress_count += 1
        progress_list.append(valid_credits)
    elif valid_credits in trailer_data:
        print('Progress (module trailer)')
        trailer_count += 1
        trailer_list.append(valid_credits)
    elif valid_credits in retriever_data:
        print('Module retriever')
        retriever_count += 1
        retriever_list.append(valid_credits)
    elif valid_credits in exclude_data:
        print('Exclude')
        exclude_count += 1
        exclude_list.append(valid_credits)
        
from graphics import *
def staff_version():    
    global progress_count, trailer_count, retriever_count, exclude_count, progress_list, trailer_list, retriever_list, exclude_list
    progress_count = 0
    trailer_count = 0
    retriever_count = 0
    exclude_count = 0

    progress_list = []
    trailer_list = []
    retriever_list = []
    exclude_list = []

    while True:
        student_version()
        #ask user for multiple entries
        more_entries = input("\nWould you like to enter data for another student? " "\nEnter 'y' for yes or 'q' to quit and view results: ")
        if more_entries.lower() == 'y':
            continue                    

        elif more_entries.lower() == 'q':       
            def histogram(count, colours, space):         # histogram part 
                win = GraphWin('Histogram', 550, 500)
                win.setBackground(color_rgb(237, 237, 230))
                bars = len(count)
                bar_width = 85

                max_data = max(count)
                minimum_height = 25
                scale = max(minimum_height, 5 / max_data)   #set a scale to ensure the representation of bars are clearly visible

                base_start = Point(40, 400)
                base_end = Point(40 + bars * (bar_width + space), 400)

                base_line = Line(base_start, base_end)
                base_line.setOutline('black')
                base_line.draw(win)

                for i in range(bars):
                    top_x = 50 + (i * (bar_width + space))
                    top_y = 400 - count[i] * scale
                    bottom_x = bar_width + top_x
                    base = 400

                    bar = Rectangle(Point(top_x, top_y), Point(bottom_x, base))
                    bar.setFill(colours[i])
                    bar.setOutline('black')
                    bar.draw(win)

                    bar_count = Text(Point(top_x + bar_width / 2, top_y - 12), str(count[i]))
                    bar_count.setTextColor(color_rgb(49, 72, 122))
                    bar_count.setStyle('bold')
                    bar_count.draw(win)

                    bar_name = Text(Point(top_x + bar_width / 2, base + 15),('Progress', 'Trailer', 'Retriever', 'Excluded')[i])
                    bar_name.setStyle('bold')
                    bar_name.setTextColor(color_rgb(33, 64, 66))
                    bar_name.draw(win)                           #print progression outcome names under bars

                above_text = Text(Point(148, 25), 'Histogram Results')
                above_text.setSize(17)
                above_text.setStyle('bold')
                above_text.setTextColor('black')
                above_text.draw(win)

                total_outcomes = count[0] + count[1] + count[2] + count[3]
                below_text = Text(Point(149, 450), f'{total_outcomes} outcome(s) in total.')
                below_text.setSize(14)
                below_text.setStyle('bold')
                below_text.setTextColor(color_rgb(52, 66, 71))
                below_text.draw(win)                  #print total outcomes

                win.getMouse()
                win.close()
            count = [progress_count, trailer_count, retriever_count, exclude_count]
            colours = [(color_rgb(129, 252, 137)), (color_rgb(5, 120, 12)), (color_rgb(86, 120, 1)),(color_rgb(250, 117, 199))]
            space = 35
            histogram(count, colours, space)       

            print('-' * 70)
            # Part 2 : program saves the input data to a list, access stored data and print after histogram
            print('Part 2:')
            for count in range(len(progress_list)):
                print('Progress - ', str(progress_list[count]).strip('()'))
            for count in range(len(trailer_list)):
                print('Progress(Module Trailer) - ', str(trailer_list[count]).strip('()'))
            for count in range(len(retriever_list)):
                print('Progress(Module Retriever) - ', str(retriever_list[count]).strip('()'))
            for count in range(len(exclude_list)):
                print('Exclude - ', str(exclude_list[count]).strip('()'))

            print('-' * 70)
            # Part 3 : program saves the input data to a text file, access stored data and print
            def text_file():
                file = open('save_input.txt', 'w')
                file.write('Part 3 :\n')
                for count in range(len(progress_list)):
                    file.write('Progress - ' + str(progress_list[count]).strip('()') + '\n')
                for count in range(len(trailer_list)):
                    file.write('Progress (Module Trailer) - ' + str(trailer_list[count]).strip('()') + '\n')
                for count in range(len(retriever_list)):
                    file.write('Module Retriever - ' + str(retriever_list[count]).strip('()') + '\n')
                for count in range(len(exclude_list)):
                    file.write('Exclude - ' + str(exclude_list[count]).strip('()') + '\n')
                file.close()

            text_file()

            file = open('save_input.txt', 'r')
            for line in file:
                print(line.rstrip('\n'))
            print('-' * 70)

        else:
            print('Invalid input!\nEnter previous credits again.')
            staff_version()
        break
    
#function to ask whether user wants to rerun the program or terminate
def rerun():         
   while True:
        rerun = input("\nDo you want to rerun the program?\nEnter 'y' for yes or 'n' to exit the program : ")
        if rerun.lower() == 'y':
            version()
            break
        elif rerun.lower() == 'n':
            print('Program terminated successfully.')  # print the end message and quit the program
            break
        else :
            print('Invalid input! Program terminated successfully.')
            break

#function to ask user to choose student version or staff version 
def version():
    while True:
        print('\nPlease enter your preferred version:\n\t1.Student Version\n\t2.Staff Version(for multiple outcomes)\n:')
        choice = input("Enter the number of your choice (1 or 2): ")

        if choice == '1':
            print('\n\tStudent Version >>>')
            student_version()
            rerun()
            break
        elif choice == '2':
            print('\n\tStaff Version >>>')
            staff_version()
            rerun()
            break
        else:
            print("Invalid input! Please enter 1, or 2.")
            continue
version()
