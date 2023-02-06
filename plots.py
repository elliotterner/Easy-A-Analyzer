"""
Author: Bermudez, Jan
Last Modified: 02/05/2023
Description: A bar graph creation module using matplotlib and data received from database_functions.py
"""
import matplotlib.pyplot as plt
import database_functions


def graph(UI_list):

    ###############################################################################################################

    #################### Database Function Selection for Data Collection ##########################################

    faculty_choice = UI_list[0] == 'Regular Faculty'    # Does the user want all instructors OR just regular faculty
    pass_choice = UI_list[2] == 'Easy A'                # Does the user want to see just A's OR D's and F's
    count_choice = UI_list[3] == True                   # Does the user want a class count

    # if looking for a specific class, like "MATH284"
    if UI_list[1] == 'Single Class Search':            
        class_list = database_functions.search_by_instructor(UI_list[5], faculty_choice)
        graph_tile = UI_list[5]
    # if looking for the whole dept
    elif UI_list[1] == 'Department Search':             
        class_list = database_functions.search_by_instructor(UI_list[4], faculty_choice)
        graph_tile = 'All ' + UI_list[4] + ' Classes'
    # if looking for a specific dept level
    elif UI_list[1] == 'All Classes Within A Certain Level':
        search_query = UI_list[4] + UI_list[6]      
        class_list = database_functions.search_by_department_level(search_query, faculty_choice)
        class_list = list(class_list)               # dict object needs to casted to list for ease of use
        graph_tile = 'All ' + search_query + ' Level Classes'
    # Somehow a different use-case was chosen
    else:
        print("Invalid selection.")


    x_axis_list = []        # in this case, the instructors
    aperc_list = []         # list for 'Easy A' percentages
    dfperc_list = []        # list for 'Just Pass' percentages

    if count_choice:
        for i in range(len(class_list)):
            last_name = class_list[i].name.split(',')[0]
            x_axis_list.append(last_name + '(' + str(class_list[i].count) + ')')    # concatenate class count to last name
            aperc_list.append(class_list[i].aperc)
            dfperc_list.append(class_list[i].dperc + class_list[i].fperc)
    else:
        for i in range(len(class_list)):
            last_name = class_list[i].name.split(',')[0]
            x_axis_list.append(last_name)
            aperc_list.append(class_list[i].aperc)
            dfperc_list.append(class_list[i].dperc + class_list[i].fperc)

    aperc_list = [int(num * 10) / 10 for num in aperc_list]        # we truncate floats like 23.572342 to 23.5
    dfperc_list = [int(num * 10) / 10 for num in dfperc_list]      # we do this to both lists without rounding

    ##############################################################################################################

    ########################################### Graph Creation ###################################################
        
    plt.style.use('seaborn')
    fig, axs  = plt.subplots(1, 2)           # create subplot with 1 row, 2 cols
    font = {'family': 'sans-serif', 'size': 16, 'weight': 'bold'}
    bar_width = 0.4
    x_label = "Classes" if UI_list[1] == 'All Classes Within A Certain Level' else "Instructors"

    # Data for Graph 1
    bars = axs[0].bar(x_axis_list, aperc_list, bar_width)       # creates the bar graph with x, y, and specified bar width
    axs[0].bar_label(bars)
    axs[0].set_ylabel("Easy A: % As")
    axs[0].set_xlabel(x_label)
    axs[0].set_title(graph_tile, fontdict=font)
    axs[0].set_ylim(0, 100)                                     # sets the limit of the y-axis to [0, 100]
    axs[0].set_xlim(-1, 9)                                      # limit starts at -1 to allow padding to the left of the first bar
    axs[0].grid(True)                                           # allows graph to form uniformly in grid pattern
    axs[0].xaxis.grid(False)                                    # removes excessive horizontal grid lines
    axs[0].set_xticklabels(x_axis_list, rotation=90)            # adds labels underneath each bar, rotating them sideways

    #Data for Graph 2
    bars = axs[1].bar(x_axis_list, dfperc_list, bar_width)
    axs[1].bar_label(bars)
    axs[1].set_ylabel("Just Pass: % Ds and Fs")
    axs[1].set_xlabel(x_label)
    axs[1].set_title(graph_tile, fontdict=font)
    axs[1].set_ylim(0, 100)
    axs[1].set_xlim(-1, 9)
    axs[1].grid(True)
    axs[1].xaxis.grid(False)
    axs[1].set_xticklabels(x_axis_list, rotation=90)

    # # Graph Output
    plt.tight_layout()
    plt.show()

