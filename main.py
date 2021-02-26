from extractor_UdeM import *
from curriculum import *
import glob

def main():
   
   #example of usage 

   informatique = Curriculum('informatique','https://admission.umontreal.ca/programmes/baccalaureat-en-informatique/structure-du-programme/')
   informatique.download_html() #you should only run this once or when you want up to date data
   soup = informatique.soupify()
   dl_course_pages_UdeM(soup,'informatique') #also this 

   #find all the files in the specified directory
   file_list = glob.glob("informatique/*.html")

   for file in file_list:
       schema = course_schema_array(file)
       informatique.add_course(schema)
   
   informatique.write_to_JSON('informatique')

if __name__ == '__main__':
    main()   