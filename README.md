# University Curriculum Maps
Visualizations to help students select their courses. 

Some curriculums offer a lot of freedom in how you approach taking your courses. However, if you're not careful your progress could be slowed down because you didn't acquire the right prerequisites at the right time. Therefore, your graduation would be delayed. University Curriculum Map is a project that aims to help avoid this situation.

(Currently supports only University of Montréal)
## Curriculum Map Data Extractor
 
 A Python script for extracting courses and their prerequisites from a curriculum at https://admission.umontreal.ca ex: BSc in Computer Science, BSc in economic science and so on. The data is extracted locally and then transformed to output a .json file with select information (ex: prerequisite courses) that can be used to map out a network of all courses. 


 The main.py presents an example of how the extraction is done for the curriculum of the BSc in Computer Science at UdeM.
 
The program was made with extension in mind so it could be used as base for more universities than UdeM:

- Every code specific in extracting content from University of Montréal (UdeM) is located inside of the extractor_UdeM.py file.

- curriculum.py contains a Curriculum class which holds the information extracted.


Visualizations are made in the visjs library :

-[Bsc Computer Science (Informatique) visualization](https://nassim-saboundji.github.io/UniversityCurriculumMaps/BScInformatique/)

  ![screenshot of the BSc Computer Science](BsInformatiqueScreenshot.png)

-[Bsc Mathematics (Mathématique) visualization](https://nassim-saboundji.github.io/UniversityCurriculumMaps/BScMath/)
  ![screenshot of the BSc Mathematics](BsMathScreenshot.png)


## How to run?  
Running the data extractor:
 - install bs4 (BeautifulSoup) module by doing `pip3 install beautifulsoup4`
 - go to main.py and add 
```
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


```

Replace math with the discipline you want to extract the curriculum from. Ex: Replace `math` with `physics`. At this point it's just name. It' required because we extract the data and put them in folders and files that uses that name.

Inside the Curriculum object replace the current link with a link from
admission.umontreal.ca (It's the link you get when you click on the tab structure du programme of a given curriculum)

For physics it would be : https://admission.umontreal.ca/programmes/baccalaureat-en-physique/structure-du-programme/

Run by doing `python3 main.py`.
Wait until the program finishes.

Once this is done. Create a new folder. copy the index.html and makeCurriculumMap.js from ex: BScMath and put them in that folder.

Now replace `fetch("./math.json")` from makeCurriculumMap.js with 
`fetch("./nameYouChose.json")`

Now simply open the index.html file and you should see the map being 
generated.