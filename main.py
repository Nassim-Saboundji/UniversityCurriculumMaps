from extractor_UdeM import *
from curriculum import *
import glob

def main():
   
   #example of usage 

#    informatique = Curriculum('informatique','https://admission.umontreal.ca/programmes/baccalaureat-en-informatique/structure-du-programme/')
#    informatique.download_html() #you should only run this once or when you want up to date data
#    soup = informatique.soupify()
#    dl_course_pages_UdeM(soup,'informatique') #also this 

#    #find all the files in the specified directory
#    file_list = glob.glob("informatique/*.html")

#    for file in file_list:
#        schema = course_schema_array(file)
#        informatique.add_course(schema)
   
#    informatique.write_to_JSON('informatique')

   math = Curriculum('math','https://admission.umontreal.ca/programmes/baccalaureat-en-mathematiques/structure-du-programme/')
   math.download_html() #you should only run this once or when you want up to date data
   soup = math.soupify()
   dl_course_pages_UdeM(soup,'math') #also this 

   #find all the files in the specified directory
   file_list = glob.glob("math/*.html")

   for file in file_list:
       schema = course_schema_array(file)
       math.add_course(schema)
   
   math.write_to_JSON('math')


if __name__ == '__main__':
    main()   