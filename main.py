from extractor_UdeM import *
from curriculum import *
import glob
import sys

def main():
   
   discipline = Curriculum(sys.argv[1], sys.argv[2])
   discipline.download_html() #you should only run this once or when you want up to date data
   soup = discipline.soupify()
   dl_course_pages_UdeM(soup, sys.argv[1]) #also this 

   #find all the files in the specified directory
   file_list = glob.glob(sys.argv[1] + "/*.html")

   for file in file_list:
       schema = course_schema_array(file)
       discipline.add_course(schema)
   
   discipline.write_to_JSON(sys.argv[1])


if __name__ == '__main__':
    main()   