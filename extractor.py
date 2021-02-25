from bs4 import BeautifulSoup
import os
import time

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

# will download the course pages for every course in a curriculum
# at UdeM. Specify a directory name in which the function will put the
# files in. If it does not exist it will create it.
# functions having the UdeM are specific to university of montreal
# later on it could be possible to extend the extractor for other universities
def dl_course_pages_UdeM(soup_object, directory_name):
    courses = soup.find_all('tbody', class_="programmeCourse fold")
    os.system('mkdir ' + directory_name)
    
    for i in range(len(courses)):
        a_tags_with_links = courses[i].find_all('a', class_='btn')

        if (len(a_tags_with_links) != 0):
            link = a_tags_with_links[0]['href']
            course_name = link.split('/')[3]
            course_info_link = 'https://admission.umontreal.ca' + link
            
            # shell commande that will download the pages locally
            # in the folder we want.
            os.system(
            'cd ' + directory_name 
            + '&& curl ' + course_info_link + '> ' + course_name + '.html'
            )

            # we don't want to tank the servers of the university
            time.sleep(3)
    

dl_course_pages_UdeM(soup, 'test')

# will return an array of prequisites for a given course
def parse_prerequisites_UdeM(course_page):
    pass






    