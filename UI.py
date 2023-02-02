from tkinter import *
from database_functions import *

# Create global variables

FacultyTypeGlobal = None
ClassSearchTypeGlobal = None
SearchPreferenceGlobal = None
ClassCountGlobal = False

dep_selectedGlobal = None
class_selectedGlobal = None
level_selectedGlobal = None

FilterOptions = None


#initialize tkinter window
root = Tk()
root.title("Easy A")
root.geometry("1200x600")

Title = Label(root, text = "Easy A Program", font = ("20"))
Title.place(relx=0.5, rely=0.1,anchor=CENTER)

Description = Label(root, text = """
                                The Easy A System is designed to help students determine which classes to take 
                                based off of a number of different criteria. The user can filter class selection based off of
                                Faculty, type of class search, type of grade, as well as if they want to see the class count.
                                Additionally, instructors who wish to add to the database may do so with the text entry box
                                """)
Description.place(relx=0.45, rely=0.3,anchor=CENTER)

#filter functions
def FacultySearchFunc(FacultyType):
    global FacultyTypeGlobal 
    FacultyTypeGlobal= FacultyType

def ClassSearchFunc(ClassSearchType):

    
    #updates department and class varibale to be passed to filter options later,
    def update_dep_clicked():
        global dep_selectedGlobal
        dep_selectedGlobal = dep_clicked.get()

        # if single class search is selected, also update class variable to be passed to filter optionss
        if ClassSearchType == "Single Class Search":
            indiv_course_options = list_indiv_courses_within_department(dep_selectedGlobal)

            #datatype of dropdown
            class_clicked = StringVar()

            #initial menu text
            class_clicked.set("Select a course")
            def update_class_clicked():
                global class_selectedGlobal
                class_selectedGlobal = class_clicked.get()

            #create dropdown
            class_DD = OptionMenu(root,class_clicked, *indiv_course_options)
            class_DD.place(relx = .415, rely = .55, anchor= 'w')

            class_select_button = Button(root, text = "confirm", command = update_class_clicked).place(relx = .415, rely = .6, anchor= 'w') 

    #sets level variable to be passed into filter options
    def update_level_clicked():
        global level_selectedGlobal
        level_selectedGlobal = level_clicked.get()
    
    if ClassSearchType == "Single Class Search":
        classOptions = list_departments()

        #datatype of dropdown text
        dep_clicked = StringVar()

        #initial menu text
        dep_clicked.set("Select department")

        #create dropdown menu
        department_DD = OptionMenu(root, dep_clicked, *classOptions)
        department_DD.place(relx = .35, rely = .55, anchor= 'w')
        
        dep_select_button = Button(root, text = "confirm", command = update_dep_clicked).place(relx = .35, rely = .6, anchor= 'w')
        
    
    if ClassSearchType == "Department Search":
        classOptions = list_departments()

        #datatype of dropdown text
        dep_clicked = StringVar()

        #initial menu text
        dep_clicked.set("Select department")

        #create dropdown menu
        department_DD = OptionMenu(root, dep_clicked, *classOptions)
        department_DD.place(relx = .35, rely = .55, anchor= 'w')
        
        dep_select_button = Button(root, text = "confirm", command = update_dep_clicked).place(relx = .35, rely = .6, anchor= 'w')


    if ClassSearchType == "All Classes Within A Certain Level":
        levelOptions = ["100","200","300", "400", "500", "600"]
        level_clicked = StringVar()
        level_clicked.set("Select a course level")

        level_DD = OptionMenu(root, level_clicked, *levelOptions)
        level_DD.place(relx = .35, rely = .55, anchor= 'w')

        level_select_button = Button(root, text = "confirm", command = update_level_clicked).place(relx = .35, rely = .6, anchor= 'w')

    global ClassSearchTypeGlobal 
    ClassSearchTypeGlobal = ClassSearchType


def TypeofSearchFunc(SearchPreference):
    global SearchPreferenceGlobal
    SearchPreferenceGlobal = SearchPreference

def ShowClassCountFunc():
    global ClassCountGlobal 
    ClassCountGlobal = True

# filter option labels:
FacultyLabel = Label(root, text = "Select type of faculty for search: ")
ClassSearchLabel = Label(root, text = "Select a type of class search:")
TypeofSearch = Label(root, text = "Select Easy A or Just Pass:")
ClassCountLabel = Label(root, text = "Class count:")


# placing labels
FacultyLabel.place(relx = .01, rely = .5, anchor= 'w')
ClassSearchLabel.place(relx = .18, rely = .5, anchor= 'w')
TypeofSearch.place(relx = .55, rely = .5, anchor= 'w')
ClassCountLabel.place(relx = .7, rely = .5, anchor= 'w')


# filter buttons
FacultyButton1 = Button(root, text = "All instructors  ", command=lambda: FacultySearchFunc("All Instructors"))
FacultyButton2 = Button(root, text = "Regular faculty", command=lambda: FacultySearchFunc("Regular Faculty"))

ClassSearchButton1 = Button(root, text = "Single Class Search                         ", command=lambda: ClassSearchFunc("Single Class Search"))
ClassSearchButton2 = Button(root, text = "Department Search                         ", command=lambda: ClassSearchFunc("Department Search"))
ClassSearchButton3 = Button(root, text = "All Classes Within A Certain Level", command=lambda: ClassSearchFunc("All Classes Within A Certain Level"))

TypeofSearchButton1 = Button(root, text= 'Easy A   ', command=lambda: TypeofSearchFunc("Easy A"))
TypeofSearchButton2 = Button(root, text= 'Just Pass', command=lambda: TypeofSearchFunc("Just Pass"))

ShowClassCountButton = Button(root, text = "Yes", command= ShowClassCountFunc)


# Placing buttons
FacultyButton1.place(relx = .015, rely = .55, anchor= 'w')
FacultyButton2.place(relx = .015, rely = .6, anchor= 'w')

ClassSearchButton1.place(relx = .19, rely = .55, anchor= 'w')
ClassSearchButton2.place(relx = .19, rely = .6, anchor= 'w')
ClassSearchButton3.place(relx = .19, rely = .65, anchor= 'w')

TypeofSearchButton1.place(relx = .56, rely = .55, anchor= 'w')
TypeofSearchButton2.place(relx = .56, rely = .6, anchor= 'w')

ShowClassCountButton.place(relx = .71, rely = .55, anchor= 'w')



# create list of filter options to pass to graphing function
def Execute():
    global FacultyTypeGlobal
    global SearchPreferenceGlobal
    global ClassSearchTypeGlobal

    if FacultyTypeGlobal == None or SearchPreferenceGlobal == None or ClassSearchTypeGlobal == None:
        print("The following filters have not been selected: ")
        if FacultyTypeGlobal == None:
            print("-- Faculty Type")
        if  ClassSearchTypeGlobal == None:
            print("-- Class Search Type")
        if SearchPreferenceGlobal == None:
            print("-- Search Type")

        print("Please select these filters before executing\n")
        return

    global FilterOptions

    """
    FacultyTypeGlobal: determines whether or not faculty selected is "all instructors" or "regularfaculty"
    ClassSearchTypeGlobal: determines class search type -> "Single Class Search", "Department Search",
        "All Courses Within A Certain Level"
    SearchPreferenceGlobal: determines search preference -> "Easy A" or "Just Pass"
    ClassCountGlobal: Determines if class count is turned off or on -> False:off True:on
    dep_selectedGlobal: holds value of department selected by user
    class_selectedGlobal: holds individual class within department that user has selected
    level_selectedGlobal: holds the level that the user is searching for

    ***Note***
    the last 3 variables (dep_selectedGlobal, class_selectedGlobal, level_selectedGlobal) will not always
    hold values within them depending on the type of search

    you probably don't need all of this information but I figured I would give you everything in
    list so that you can pick and choose what you need for making the graphs 

    """

    FilterOptions = [FacultyTypeGlobal, ClassSearchTypeGlobal, SearchPreferenceGlobal, ClassCountGlobal,dep_selectedGlobal, class_selectedGlobal, level_selectedGlobal]
    print(FilterOptions)




# Execute button creation
ExecuteButton = Button(root, text = "Execute", command= Execute)
ExecuteButton.place(relx = .8, rely = .5, anchor= 'w')



root.mainloop()