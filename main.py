from extractor_UdeM import *
from curriculum import *
import glob

def main():
   
   #example of usage 

   economie = Curriculum('economie','https://admission.umontreal.ca/programmes/baccalaureat-en-sciences-economiques/structure-du-programme/')
   #economie.download_html() only once should run this
   soup = economie.soupify()
   #dl_course_pages_UdeM(soup,'economie') also this only once

   #find all the files in the specified directory
   file_list = glob.glob("economie/*.html")

   for file in file_list:
       schema = course_schema_array(file)
       economie.add_course(schema)
   
   economie.write_to_JSON('economie')

if __name__ == '__main__':
    main()   