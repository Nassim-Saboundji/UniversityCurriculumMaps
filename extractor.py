from bs4 import BeautifulSoup
import os


class Curriculum:

    soup_object = None 
    course_list_json = None

    def __init__(self, discipline, link):
        self.discipline = discipline
        self.link = link 

    #Downloads the html page of the curriculum at umontreal.ca
    #if it's not already in the working directory.
    def download_html(self):    
        if(os.path.exists(self.discipline + '.html') == False):
            os.system('curl ' + self.link + ' > ' + self.discipline + '.html')

    def soupify(self):
        file = open(self.discipline +'.html')
        self.soup_object = BeautifulSoup(file, 'html.parser')

        return self.soup_object

        

test = Curriculum('informatique','https://admission.umontreal.ca/programmes/baccalaureat-en-informatique/structure-du-programme/')
test.download_html()
soup = test.soupify()

# function that will extract all course information from
# University of Montreal (UdeM).
# returns a json object with relevant informations for each courses.
# extraction is different for different universities
def get_courses_UdeM(soup_object):
    courses = soup.find_all('tbody', class_="programmeCourse fold")
    print(courses[0].find_all('a', class_='btn')[0]['href'])
    courses_json = {}

get_courses_UdeM(soup)




def get_courses_McGill(soup_object):
    pass

def get_courses_Concordia(soup_object):
    pass

def get_courses_USherbrooke(soup_object):
    pass





    