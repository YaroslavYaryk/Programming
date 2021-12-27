import tkinter as tk
import tkinter.font as TkFont
from datetime import datetime
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

from about_netepad_text import text


class Window():

    def __init__(self,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Tk() #build te main root
        #make it more beautiful
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+350+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])
        self.save_auto = tk.BooleanVar()
        #program it while the buttom is clicked
        self.root.bind_all("<Control-s>", self.save)
        self.root.bind_all("<Control-w>", self.make_work)
        self.root.bind_all("<Control-d>", self.save_as)
        self.root.bind_all("<Control-n>", self.new)
        self.root.bind_all("<Control-m>", self.new_win)
        self.root.bind_all("<Control-o>", self.open)
        self.root.focus_set()
        self.root.grab_set()
        #function of closing window
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.close_window("root"))
        #initialization of all objects that i'm gonna use
        self.name = None
        self.word_wrap_choice = tk.BooleanVar(value = True)

    def run(self): #run function
        self.draw_menu()
        self.draw_scrolled_text()
        self.root.mainloop()

    def close_window(self, word): #function that apears when we close_window 
        #and asks as wanna we sawe material or not
        if word == "root":
            if  len(self.st.get("0.0", "1.1")) == 0 or self.name is not None:
                self.root.destroy()
            else:
                choice = messagebox.askyesnocancel (' action Box','Do you wanna save your changes??') 
                if choice is True:
                    self.save_as()
                elif choice is False:
                    self.root.destroy()
                elif choice is None:
                    pass    
            return self.st     

        elif word == "win":
            if  len(self.win_st.get("0.0", "1.1")) == 0 or self.name is not None:
                self.win.destroy()
            else:
                choice = messagebox.askyesnocancel (' action Box','Do you wanna save your changes??') 
                if choice:
                    self.save_as()
                elif choice is False:
                    self.win.destroy()
                elif choice is None:
                    pass    
            return self.win_st      


    def make_work(self, *args, **kwargs): #function that gets the selected text and
        #uses another function to aneble our labels ('cut', 'copy', 'paste')
        self.get_selected = self.st.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.work_with_selected_text("root")
        
        return  self.get_selected

    def make_work_new_win(self, *args, **kwargs):
        #the sae one as the previoys but it works with new window
        self.get_selected = self.win_st.get(tk.SEL_FIRST, tk.SEL_LAST)
        self.work_with_selected_text("win")
        return  self.get_selected    


    #function that open the folders and save our information
    #can use just clicking 'Ctrl+d'
    def save_as(self, *args, **kwargs):
        try:
            #open main terminal to save our results
            self.name = fd.asksaveasfilename(filetypes = (("Text file", "*.txt"), ("Python files", "*.py" ))) 
            #when we chosed file if opens it            
            with open(self.name, "w") as f:
                f.write(self.st.get("0.0", tk.END))# and write there information that there is in this file
        except FileNotFoundError:
            pass  
              
        return self.name        
    #function that save our information but nou open folders when it was used already
    #can use just clicking 'Ctrl+s'
    def save(self, *args, **kwargs):
        try:
            if self.name is None:
                #open main terminal to save our results
                self.name = fd.asksaveasfilename(filetypes = (("Text file", "*.txt"), ("Python files", "*.py" ))) 
                #when we chosed file if opens it            
                with open(self.name, "w") as f:
                    f.write(self.st.get("0.0", tk.END))# write there information that there is in this file
        except FileNotFoundError:
            pass            
        return self.name
                     

    #open folders to open file that we're looking for
    def open(self,name_type ,*args, **kwargs):
        name = fd.askopenfilename()
        if name_type == "root": #main operation
            if name:
                with open(name, "r") as f: #open main teminal
                    self.st.delete("0.0", tk.END)
                    self.st.insert(tk.END, f.read()) #insert the text that we have chosen
        elif name_type == "win": # the same but only for new_win
            if name:
                with open(name, "r") as f:
                    self.win_st.delete("0.0", tk.END)
                    self.win_st.insert(tk.END, f.read())              

    def work_with_selected_text(self, name_type): #function that nake our labelf feel NORMAL
        if name_type == "root":
            if len(self.get_selected) != 0:#if len of selected text is not zero
                self.new_menu2.entryconfig(0, state = tk.NORMAL) #anebling our labels
                self.new_menu2.entryconfig(1, state = tk.NORMAL)
                self.new_menu2.entryconfig(2, state = tk.NORMAL)
                self.new_menu2.entryconfig(3, state = tk.NORMAL)
                self.new_menu2.entryconfig(4, state = tk.NORMAL)

        elif name_type == "win":
            if len(self.get_selected) != 0:#if len of selected text is not zero
                self.new_menu_new_win.entryconfig(0, state = tk.NORMAL)#anebling our labels
                self.new_menu_new_win.entryconfig(1, state = tk.NORMAL)
                self.new_menu_new_win.entryconfig(2, state = tk.NORMAL)
                self.new_menu_new_win.entryconfig(3, state = tk.NORMAL)



    #main function that creates new window in our Noetepad
    def new_win(self, *args, **kwargs):
        #asks if we wanna save our changes 
        choice = messagebox.askyesnocancel ('Yes or No or Cancel action Box','Do you wanna save your changes??') 
        if  choice is False: #if answer is No
            self.win = tk.Toplevel(self.root) #we create new win
            #make it looks a bit attractive
            self.win.title("Untitled")
            self.win.geometry(f"{900}x{520}+500+150")
            self.win.config(bg = "white")
            #creating scrollText to meke it like a real Notepadd
            self.win_st = ScrolledText(self.win, selectforeground = "white", fg = "black", font = ("Consolas", 11, "bold"),
                            wrap = "word", width = 200, height = 100)
            self.win_st.pack() #pack it in our screen 
            #create a status bur into our screen
            menu_bar = tk.Menu(self.win)
            self.win.bind_all("<Control-w>", self.make_work_new_win)#to uneble our ('cut','copy','paste') labels
            #creating adition little-memu on our status bar
            new_menu = tk.Menu(menu_bar, tearoff = 0)
            self.new_menu_new_win = tk.Menu(menu_bar, tearoff = 0) #we created it as self_object because we're gonna use into
            #out of this function
            new_Format = tk.Menu(menu_bar, tearoff = 0)
            new_font = tk.Menu(menu_bar, tearoff = 0)
            new_view = tk.Menu(menu_bar, tearoff = 0)
            new_zoom = tk.Menu(menu_bar, tearoff = 0)
            new_help = tk.Menu(menu_bar, tearoff = 0)

            #add kabels on the each little-menu
            new_menu.add_command(label = "New                    Ctrl+N",)
            new_menu.add_command(label = "New Window    Ctrl+M", command = self.new_win)
            new_menu.add_command(label = "Open                  Ctrl+O", command =lambda: self.open("win"))#add function

            new_menu.add_separator()#add separator for this little-menu

            new_menu.add_command(label = "Save                    Ctrl + s")
            new_menu.add_cascade(label = "Save as               Ctrl + d")
            new_menu.add_separator()
            new_menu.add_command(label = "exit", command = lambda: self.close_window("win"))

            #adding special labels 
            self.new_menu_new_win.add_command(label = "Cut",  command = lambda: self.get_cut("win"))
            self.new_menu_new_win.add_command(label = "Copy",  command = lambda: self.get_copy("win"))
            self.new_menu_new_win.add_command(label = "Paste",  command = lambda: self.get_paste("win"))
            self.new_menu_new_win.add_command(label = "Delete", command = lambda: self.get_delete("win"))

            self.new_menu_new_win.add_separator()
            self.new_menu_new_win.add_command(label = "Select All", command = lambda: self.get_select_text("win"))
            self.new_menu_new_win.add_command(label = "Time/Data", command = lambda: self.get_current_time("win"))
            self.new_menu_new_win.entryconfig(0, state = tk.DISABLED)#make all of this labels disabled
            self.new_menu_new_win.entryconfig(1, state = tk.DISABLED)#make all of this labels disabled
            self.new_menu_new_win.entryconfig(2, state = tk.DISABLED)#make all of this labels disabled
            self.new_menu_new_win.entryconfig(3, state = tk.DISABLED)#make all of this labels disabled

            #add checkbutton list of fonts if we wanna change this one
            new_Format.add_checkbutton(label = "Word wrap", variable = self.word_wrap_choice, onvalue = True, offvalue =False, command = self.word_wrap_funk)

            new_font.add_command(label = "Arial", command = lambda: self.make_font("Arial",  "win"))
            new_font.add_command(label = "Consolas", command = lambda: self.make_font("Consolas", "win"))
            new_font.add_command(label = "Calibri", command = lambda: self.make_font("Calibri", "win"))
            new_font.add_command(label = "Modern", command = lambda: self.make_font("Modern", "win"))
            #add zoom labels with commands
            new_zoom.add_command(label = "Zoom in", command = lambda: self.zoom_in_command("zoom in", "win"))
            new_zoom.add_command(label = "Zoom out", command = lambda: self.zoom_in_command("zoom out", "win"))
            new_zoom.add_command(label = "Restore to default settings", command = lambda: self.zoom_in_command("default", "win"))
            #add this all little-menu to our main menu
            menu_bar.add_cascade(label = "File", menu = new_menu)
            menu_bar.add_cascade(label = "Edit", menu = self.new_menu_new_win)
            menu_bar.add_cascade(label = "Format", menu = new_Format)
            new_Format.add_cascade(label = "Font...", menu = new_font)
            menu_bar.add_cascade(label = "View", menu = new_view)
            menu_bar.add_cascade(label = "Help", menu = new_help)

            new_view.add_cascade(label = "Zoom", menu = new_zoom)

            self.win.configure(menu = menu_bar) #add our main menu to main root
        elif choice is True: #in choice is true save_as (wanna save our changes)
            self.save_as() 
        elif choice is None: #if choice is None, means we cliked on 'Cancel'
            pass    #dont do anything
        
        self.win.protocol("WM_DELETE_WINDOW", lambda: self.close_window("win"))#funk closing new_window
        
        return self.win_st, self.win, self.new_menu_new_win     #return all elements we will use later
    

    def new(self, *args, **kwargs): #new_funk just clean the whole field
        self.st.delete("0.0", tk.END)


    def draw_scrolled_text(self): #funk that draw scrolled text on our main root
        self.st = ScrolledText(self.root, selectforeground = "white", fg = "black", font = ("Consolas", 11, "bold"),
                             width = 200, height = 100)#all the parameters
        self.st.pack()  
        return self.st  

    def word_wrap_funk(self):#if we wanna end our line with word we use this funk
        if self.word_wrap_choice: #checkbuttom that has two types ("true", "false")
            self.st.configure(wrap = "word")#if true we change configuration of dcrilled text

    def make_font(self, chosenfont, place): #change size of our font
        if place == "root": #on main root
            self.st.configure(font = (chosenfont, 11))
        elif place == "win": #on new window
            self.win_st.configure(font = (chosenfont, 11))


    def zoom_in_command(self, type_size, place): #funk zooms out font
        #for main root
        if type_size =="zoom in" and place == "root":  #if zoom_in  font getting bigger
            self.default_font +=2
            self.st.configure(font = ("Arial", self.default_font))
        elif type_size =="zoom out" and place == "root":  #if zoom_our  font getting smaller
            self.default_font -=2
            self.st.configure(font = ("Arial", self.default_font))
        elif type_size =="default" and place == "root":  #if default  returns start font size 
            self.st.configure(font = ("Arial", 11))

        #for new window
        elif type_size =="zoom in" and place == "win": #if zoom_in  font getting bigger
            self.default_font +=2
            self.win_st.configure(font = ("Arial", self.default_font))
        elif type_size =="zoom out" and place == "win": #if zoom_our  font getting smaller
            self.default_font -=2
            self.win_st.configure(font = ("Arial", self.default_font))
        elif type_size =="default" and place == "win": #if default  returns start font size
            self.win_st.configure(font = ("Arial", 11))    

        return self.default_font    

    def get_cut(self, name_type): #funk that cut selected text
        if name_type == "root": #for root
            try:
                self.storage_for_copy_cut_paste = self.st.get(tk.SEL_FIRST, tk.SEL_LAST) #get selected text
                self.st.delete("sel.first", "sel.last") #delete selected
            except Exception:
                pass
            return self.storage_for_copy_cut_paste
        elif name_type == "win": #for new window       
            try:
                self.storage_for_copy_cut_paste = self.win_st.get(tk.SEL_FIRST, tk.SEL_LAST)  #get selected text
                self.win_st.delete("sel.first", "sel.last") #delete selected
            except Exception:
                pass
        return self.storage_for_copy_cut_paste

    def get_copy(self,name_type):  #funk that copy selected text
        if name_type == "root": #for root
            try:
                self.st.clipboard_clear()
                self.storage_for_copy_cut_paste = self.st.get(tk.SEL_FIRST, tk.SEL_LAST) #get selected text
                text = self.storage_for_copy_cut_paste
                self.st.clipboard_append(text)
            except Exception:
                pass   
            return self.storage_for_copy_cut_paste  
        elif name_type == "win": #for new window 
            try:
                self.win_st.clipboard_clear()
                self.storage_for_copy_cut_paste = self.win_st.get(tk.SEL_FIRST, tk.SEL_LAST)  #get selected text
                text = self.storage_for_copy_cut_paste
                self.win_st.clipboard_append(text)
            except Exception:
                pass   
            return self.storage_for_copy_cut_paste          

    def get_paste(self, name_type): #funk that paste selected text
        if name_type == "root": #for root
            try:
                text = self.storage_for_copy_cut_paste   #get text that has already been set             
                self.st.insert('insert', text)  #add it to scrolled text
            except Exception:
                pass
            return self.storage_for_copy_cut_paste 
             
        elif name_type == "win": #for root
            try:
                text = self.storage_for_copy_cut_paste  #get text that has already been set               
                self.win_st.insert('insert', text)  #add it to scrolled text
            except Exception:
                pass
            return self.storage_for_copy_cut_paste             

    def get_delete(self, name_type): #delete whole selected text
        if name_type == "root": #for root
            try:
                self.st.delete("sel.first", "sel.last") 
            except Exception:
                pass  
        elif name_type == "win": #for new win
            try:
                self.win_st.delete("sel.first", "sel.last") 
            except Exception:
                pass          

    def about_notepad_command(self): #func thet creates new field to see the
        #information of this notepad
        new_win = tk.Toplevel(self.root, width = 500, height = 500)
        new_win.geometry("500x400+500+200")
        new_win.title("About")
        new_st = ScrolledText(new_win)  
        new_st.insert(tk.END, text)
        new_st.pack()  


    def get_select_text(self, name_type):
        
        if name_type == "root":
            self.st.tag_add("sel", "1.0", "end")  #get selected from root
        elif name_type == "win":
            self.win_st.tag_add("sel", "1.0", "end")  #get selected from new win

    def find_word(self):
        self.win_new = tk.Toplevel(self.root)
        tk.Label(self.win_new, text = "What ti find").grid(row = 0, column = 0)
        self.what_to_find = tk.Entry(self.win_new)
        self.what_to_find.grid(row =0, column = 1, columnspan = 3)
        button = tk.Button(self.win_new, text = "Find", command = self.find_word_main)
        button.grid(row = 1, column = 1)
        return self.what_to_find, self.new_win
        
    
    def find_word_main(self):

        position_of_word = self.st.get("0.0","end").find(self.what_to_find.get())
        pos = 1
        while position_of_word > len(self.st.get(f"{pos}.0", f"{pos}.100")):
            
            position_of_word -= len(self.st.get(f"{pos}.0", f"{pos}.100"))
            pos +=1
                
        else:
            position_of_word = self.st.get(f"{pos}.0","end").find(self.what_to_find.get())       
            self.st.tag_add("sel", f"{pos}.{position_of_word}", f"{pos}.{position_of_word + len(self.what_to_find.get())}")
        self.win_new.destroy()
            

    def get_current_time(self, name_type):  #show current time
        d = datetime.today()
        if name_type == "root": 
            self.st.insert("end", d.strftime("%d-%B-%Y %H:%M:%S"))  
        elif name_type == "win": 
            self.win_st.insert("end", d.strftime("%d-%B-%Y %H:%M:%S"))       

    def new_delete_whole_text(self): #delete everything
        self.st.delete("1.0", "end")


    def draw_menu(self): #creating tme main menu on root

        menu_bar = tk.Menu(self.root) #main menu
        #creating little menues
        new_menu = tk.Menu(menu_bar, tearoff = 0)
        self.new_menu2 = tk.Menu(menu_bar, tearoff = 0) #we use iy out of this function to make

        #label in there state Normal
        new_Format = tk.Menu(menu_bar, tearoff = 0)
        new_font = tk.Menu(menu_bar, tearoff = 0)
        new_view = tk.Menu(menu_bar, tearoff = 0)
        new_zoom = tk.Menu(menu_bar, tearoff = 0)
        new_help = tk.Menu(menu_bar, tearoff = 0)

        #adding label and their command to each little menu bar

        new_menu.add_command(label = "New                    Ctrl+N",command = self.new_delete_whole_text)
        new_menu.add_command(label = "New Window    Ctrl+M", command = self.new_win)
        new_menu.add_command(label = "Open                  Ctrl+O", command = lambda: self.open("root"))

        new_menu.add_separator()# add separator

        new_menu.add_command(label = "Save                    Ctrl + s", command =  self.save)
        new_menu.add_cascade(label = "Save as               Ctrl + d",command =  self.save_as)
        new_menu.add_separator()
        new_menu.add_command(label = "exit", command = lambda: self.close_window("root"))

        
        self.new_menu2.add_command(label = "Cut", command = lambda: self.get_cut("root"))
        self.new_menu2.add_command(label = "Copy", command = lambda: self.get_copy("root"))
        self.new_menu2.add_command(label = "Paste", command =lambda:  self.get_paste("root"))
        self.new_menu2.add_command(label = "Delete", command = lambda: self.get_delete("root"))
        self.new_menu2.add_command(label = "Find", command = self.find_word)
        self.new_menu2.add_separator()
        self.new_menu2.add_command(label = "Select All", command = lambda: self.get_select_text("root"))
        self.new_menu2.add_command(label = "Time/Data", command = lambda: self.get_current_time("root"))

        #making labels disabled
        self.new_menu2.entryconfig(0, state= tk.DISABLED)
        self.new_menu2.entryconfig(1, state= tk.DISABLED)
        self.new_menu2.entryconfig(2, state= tk.DISABLED)
        self.new_menu2.entryconfig(3, state= tk.DISABLED)
        self.new_menu2.entryconfig(4, state= tk.DISABLED)


        #add checkbutton to wrap funk
        new_Format.add_checkbutton(label = "Word wrap", variable = self.word_wrap_choice, onvalue = True, offvalue =False, command = self.word_wrap_funk)
        # for canging our font
        new_font.add_command(label = "Arial", command = lambda: self.make_font("Arial", "root"))
        new_font.add_command(label = "Consolas", command = lambda: self.make_font("Consolas", "root"))
        new_font.add_command(label = "Calibri", command = lambda: self.make_font("Calibri", "root"))
        new_font.add_command(label = "Modern", command = lambda: self.make_font("Modern", "root"))
        #zoom funk
        new_zoom.add_command(label = "Zoom in", command = lambda: self.zoom_in_command("zoom in", "root"))
        new_zoom.add_command(label = "Zoom out", command = lambda: self.zoom_in_command("zoom out", "root"))
        new_zoom.add_command(label = "Restore to default settings", command = lambda: self.zoom_in_command("default", "root"))

        new_help.add_command(label = "About Notepad", command = self.about_notepad_command)
        

        #add little menus to main menu_bar
        menu_bar.add_cascade(label = "File", menu = new_menu)
        menu_bar.add_cascade(label = "Edit", menu = self.new_menu2)
        menu_bar.add_cascade(label = "Format", menu = new_Format)
        new_Format.add_cascade(label = "Font...", menu = new_font)
        menu_bar.add_cascade(label = "View", menu = new_view)
        new_view.add_cascade(label = "Zoom", menu = new_zoom)
        menu_bar.add_cascade(label = "Help", menu = new_help)

        #add main menu to root
        self.root.configure(menu = menu_bar)

        return self.new_menu2     


win = Window("Notepad", 500,900, "#5199FF") #inicialization
win.run()        #starting
