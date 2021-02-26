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
    
        
        
