from tkinter import *


class UserInterface:

    def __init__(self):
        def search():

            self.search_for = self.what_to_search.get()
            self.exclude = self.exclusion_criteria.get().split(', ')
            self.window.destroy()

        self.window = Tk()
        self.canvas = Canvas()
        self.exclusion_criteria = Entry()
        self.ex_label = Label(text="What to exclude from the search (separate words with commas): ", justify=LEFT)
        self.what_to_search = Entry()
        self.search_for = self.what_to_search.get()
        self.exclude = self.exclusion_criteria.get().split(', ')
        self.search_label = Label(text="Type what you want to search: ")
        self.search_button = Button(text="Search", command=search)
        self.blurb = Label(text="Want to avoid annoying spoilers on YouTube? Just use the quick and easy YouTube Spoiler Filter! \nType"
                           " what you want to search on YouTube and the YouTube Spoiler Filter will search YouTube and give you "
                           "all the videos without spoiler keywords in the title!\n", font=("Arial", 13, "normal"))

    def start_window(self):

        self.window.config(padx=100, pady=100)
        self.window.title("YouTube Spoiler Filter")
        self.exclusion_criteria.grid(column=2, row=5, columnspan=1)
        self.exclusion_criteria.config(width=100, justify=LEFT)
        self.ex_label.grid(column=1, row=5)
        self.what_to_search.config(width=100)
        self.search_label.grid(column=1, row=4)
        self.search_button.config(width=20)
        self.search_button.grid(column=2, row=6)
        self.what_to_search.grid(column=2, row=4)
        self.blurb.grid(column=0, row=0, columnspan=5, rowspan=3)
        self.window.mainloop()
        return self.search_for, self.exclude

    def curtain(self):
        curtain = Tk()
        curtain.title("Please wait")
        curtain.config(pady=100, padx=100)
        curtain.state("zoomed")
        please_wait = Label(text="Please wait while we search and filter your results",
                            font=("Freestyle script", 70, "bold"), justify="center")
        please_wait.grid(column=0, row=0)
        curtain.after(18000, lambda: curtain.destroy())
        curtain.mainloop()

# Coming soon: the results will be filtered and displayed in a user friendly window!
