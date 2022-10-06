import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    #It takes microphone ae input from user to print string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
            print(f"You said: {query}\n")  #User query will be printed.
    
        except Exception as e:
          # print(e)    
          print("Say that again please...")   #Say that again will be printed in case of improper voice 
          return "None" #None string will be returned

        return query


class Library:
    def __init__(self,list):
        self.books=list
        
    def displayBooks(self):
        speak("These are the books present in the Library:")
        print("These are the books present in the Library:")
        for book in self.books:
            print("\t :-) "+book)
            #speak(book)
            
    def issueBook(self, bookName):
        if bookName in self.books:
            speak(f"You have been issued {bookName}. Please keep it safe and return it within 15 days or else you be charged for it my dear friend")
            print(f"You have been issued {bookName}. Please keep it safe and return it within 15 days or else you be charged for it my dear friend")
            self.books.remove(bookName)
            return True
        else:
            speak("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False
    
    def addBook(self,bookName):
        self.books.append(bookName)
        speak("The book has been added to your list")
        print("The book has been added to your list")
        
       
         
    def returnBook(self,bookName):
        self.books.append(bookName)
        speak("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")
       
        

class Student:
    def issueBook(self):
        speak("Enter the name of the book you want to borrow")
        self.book = str(takecommand())
        
        return self.book

    def returnBook(self):
        speak("Enter the name of the book you want to return: ")
        self.book = str(takecommand())
        
        return self.book

    def addBook(self):
        speak("Enter the name of the book you want to add to library: ")
        self.book = str(takecommand())
        
        return self.book   
    

if __name__ == '__main__':
    studentlibrary = Library(["python","c","java","chemistry","stld","physics","maths","english"])
    student = Student()
    # studentlibrary.displayBooks()
    while (True):
        welcomeMsg = '''\n Welcome to Sri Vasavi Engineering College Library
        Please choose an option :
        1 List of the books
        2 Add a book
        3 Exit the Library
        '''
    
        print(welcomeMsg)
        speak(welcomeMsg)
        #speak("Please Choose a Option from above :")
        #print("Please Choose a Option from above :")
        query = takecommand().lower()

    
        if "1" in query or "one" in query:       
            studentlibrary.displayBooks()
            while  (True):
                options = '''\nPlease choose a option from 
                1 Issue a book
                2 Return a book
                3 Go back to Main Menu
                '''
                print(options)
                #speak(options)
                query = takecommand().lower()
    
    
                if "1" in query or "one" in query:         
                    studentlibrary.issueBook(student.issueBook())
                
                elif "2" in query or "two" in query:         
                    studentlibrary.returnBook(student.returnBook())
    
                elif "3" in query or "three" in query:
                    print(welcomeMsg)
                    break
         

        elif "2" in query or "three" in query:        
                studentlibrary.addBook(student.addBook())

        elif "3" in query or "five" in query:                 
            print("Thanks For Choosing Sri Vasavi Engineering College Library. Have a good day!")
            speak("Thanks For Choosing Sri Vasavi Engineering College Library. Have a good day!")
            exit()
            
        else:
            print("You have choose a Invalid Choice ")    
            speak("You have choose a Invalid Choice ") 