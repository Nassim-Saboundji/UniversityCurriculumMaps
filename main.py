from extractor import *
import glob

def main():
   
#    informatique = Curriculum('informatique','https://admission.umontreal.ca/programmes/baccalaureat-en-informatique/structure-du-programme/')
#    soup = informatique.soupify()
#    dl_course_pages_UdeM(soup,'informatique')

#    file_list = glob.glob("informatique/*.html")
   
#    for file in file_list:
#        schema = course_schema_array(file)
#        informatique.add_course(schema)
   
#    informatique.write_to_JSON('informatique')

   economie = Curriculum('economie','https://admission.umontreal.ca/programmes/baccalaureat-en-sciences-economiques/structure-du-programme/')
   #economie.download_html() only once should run this
   soup = economie.soupify()
   #dl_course_pages_UdeM(soup,'economie') also this only once

   file_list = glob.glob("economie/*.html")
   
   for file in file_list:
       schema = course_schema_array(file)
       economie.add_course(schema)
   
   economie.write_to_JSON('economie')

if __name__ == '__main__':
    main()   