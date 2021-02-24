from bs4 import BeautifulSoup
import os

class Curriculum:

    curriculum_links = {
        'informatique':'https://admission.umontreal.ca/programmes/baccalaureat-en-informatique/structure-du-programme/'
    }
    soup_object = None 
    course_list_json = None

    def __init__(self, discipline):
        self.discipline = discipline 

    #Downloads the html page of the curriculum at umontreal.ca
    #if it's not already in the working directory.
    def download_html(self):    
        if(os.path.exists(self.discipline + '.html') == False):
            os.system('curl ' + self.curriculum_pages[self.discipline] 
            + ' > ' + self.discipline + '.html')
        

test = Curriculum('informatique')
test.download_html()