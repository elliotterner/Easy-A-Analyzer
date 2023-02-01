from tkinter import *

# Create global filter options

FacultyTypeGlobal = None
ClassSearchTypeGlobal = None
SearchPreferenceGlobal = None
ClassCountGlobal = False

FilterOptions = None


#initialize tkinter window
root = Tk()
root.title("Easy A")
root.geometry("1000x400")

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
ClassSearchLabel.place(relx = .22, rely = .5, anchor= 'w')
TypeofSearch.place(relx = .45, rely = .5, anchor= 'w')
ClassCountLabel.place(relx = .66, rely = .5, anchor= 'w')


# filter buttons
FacultyButton1 = Button(root, text = "All instructors  ", command=lambda: FacultySearchFunc("All Instructors"))
FacultyButton2 = Button(root, text = "Regular faculty", command=lambda: FacultySearchFunc("Regular Faculty"))

ClassSearchButton1 = Button(root, text = "Single Class Search", command=lambda: ClassSearchFunc("Single Class Search"))
ClassSearchButton2 = Button(root, text = "Department Search", command=lambda: ClassSearchFunc("Department Search"))
ClassSearchButton3 = Button(root, text = "All Classes Within A Certain Level", command=lambda: ClassSearchFunc("All Classes Within A Certain Level"))

TypeofSearchButton1 = Button(root, text= 'Easy A   ', command=lambda: TypeofSearchFunc("Easy A"))
TypeofSearchButton2 = Button(root, text= 'Just Pass', command=lambda: TypeofSearchFunc("Just Pass"))

ShowClassCountButton = Button(root, text = "Yes", command= ShowClassCountFunc)


# Placing buttons
FacultyButton1.place(relx = .05, rely = .60, anchor= 'w')
FacultyButton2.place(relx = .05, rely = .7, anchor= 'w')

ClassSearchButton1.place(relx = .24, rely = .6, anchor= 'w')
ClassSearchButton2.place(relx = .24, rely = .7, anchor= 'w')
ClassSearchButton3.place(relx = .22, rely = .8, anchor= 'w')

TypeofSearchButton1.place(relx = .49, rely = .6, anchor= 'w')
TypeofSearchButton2.place(relx = .49, rely = .7, anchor= 'w')

ShowClassCountButton.place(relx = .685, rely = .6, anchor= 'w')



# create list of filter options to pass to backend
def combineFilters():
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
    FilterOptions = [FacultyTypeGlobal, ClassSearchTypeGlobal, SearchPreferenceGlobal, ClassCountGlobal]
    print(FilterOptions)


# Execute button creation
ExecuteButton = Button(root, text = "Execute", command= combineFilters)
ExecuteButton.place(relx = .8, rely = .5, anchor= 'w')



root.mainloop()