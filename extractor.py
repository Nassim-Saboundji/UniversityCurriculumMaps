from bs4 import BeautifulSoup
import os
import time
import json
import re

class Curriculum:

    soup_object = None 
    course_list_data = {}

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

    def add_course(self, schema):
        self.course_list_data[schema[0]] = schema[1]

    def get_course_list(self):
        return self.course_list_data

    def write_to_JSON(self, name : str):    
        file = open(name + ".json",'w')
        json.dump(self.course_list_data, file)
    
        
        

# will download the course pages for every course in a curriculum
# at UdeM. Specify a directory name in which the function will put the
# files in. If it does not exist it will create it.
# functions having the UdeM are specific to university of montreal
# later on it could be possible to extend the extractor for other universities
def dl_course_pages_UdeM(soup_object, directory_name : str):
    courses = soup_object.find_all('tbody', class_="programmeCourse fold")
    os.system('mkdir ' + directory_name)
    
    for i in range(len(courses)):
        a_tags_with_links = courses[i].find_all('a', class_='btn')

        if (len(a_tags_with_links) != 0):
            link = a_tags_with_links[0]['href']
            course_name = link.split('/')[3]
            course_info_link = 'https://admission.umontreal.ca' + link
            
            # shell command that will download the pages locally
            # in the folder we want.
            os.system(
            'cd ' + directory_name 
            + '&& curl ' + course_info_link + '> ' + course_name + '.html'
            )

            # we don't want to tank the servers of the university
            time.sleep(1)
    

#dl_course_pages_UdeM(soup, 'test')

# will return an array of prequisites for a given course
# if there is no prerequisites it will return 0
# certain rules must be applied later on to filter obsolete courses
# from the prerequisites.
def parse_prerequisites_UdeM(file_path):
    course_page = open(file_path)
    soup = BeautifulSoup(course_page, 'html.parser')
    raw_prereqs = soup.find_all('p', class_='specDefinition')
    #print(raw_prereqs)
    prereqs_txt = raw_prereqs[len(raw_prereqs) - 1].string
    if prereqs_txt != None:
        # regular expression that checks for a substring
        # which start with three capital letters and continues with
        # 4 numbers. This is to find all prerequisites course codes
        # ex: IFT2015 
        result = re.findall("[A-Z]{3}[0-9]{4}", prereqs_txt)
        if result != None:
            return result
    
    # no prerequisites were found
    return 0            


def course_id_only(course_name : str):
    course_letters = re.findall('[A-Z]{3}', course_name)
    course_number = re.findall('[0-9]{4}',course_name)
    return course_letters[0] + course_number[0]

# Makes a course schema array that will contain the key of the course
# as the first element and a json object containing relevant info
# as the second element. This will make it easy to add key pair values in
# the course_list_data in the Curriculum object.
def course_schema_array(file_path):
    course_page = BeautifulSoup(open(file_path), 'html.parser')
    schema = course_page.find('script', attrs={'type' :'application/ld+json'}).string
    #we now have access to the json schema that was provided in the course
    #webpage so we can use that to transfer some info over to our course schema
    print(schema)
    schema_json = json.loads(schema, strict=False)
    
    useful_schema = {}
    useful_schema["name"] = schema_json["name"]
    useful_schema["description"] = schema_json["description"]
    useful_schema["prereqs"] = parse_prerequisites_UdeM(file_path)
    course_id = course_id_only(useful_schema["name"])

    schema_array = []
    schema_array.append(course_id) 
    schema_array.append(useful_schema)
    return schema_array

