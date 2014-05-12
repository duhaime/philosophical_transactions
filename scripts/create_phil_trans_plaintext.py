'''This script extracts the xml from Jstor's EJC distribution of the Philosophical Transactions.
More specifically, it reads in each of the three main directories of the EJC distribution, (one by one),
and, for each of those directories, transforms each PT article in that directory's subdirectories into a plain text file.
This script also produces a bare bones metadata file that contains text, author, publication date, language, and title info for each file.'''

import glob, codecs, os
from bs4 import BeautifulSoup
from os.path import basename
    
#if fed a directory as input, this function returns a list object containing all of the names of subdirectories within that higher-level directory
def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]

#define root dir that holds all sub_dirs of interest 
root_directory = "C:\\Text\\Professional\\Text Data\\EJC\\Philosophical Transactions 1775-1870 (Perhaps)"

#create handle for metadata output
with codecs.open("philosophical_transactions_metadata.txt", "w", "utf-8") as metadata_out:
        
    #write headers to metadata output
    metadata_out.write("file_id" + "\t" + "year" + "\t" + "language" + "\t" + "title" + "\t" + "given_name" + "\t" + "surname" + "\n")

    #create loop, each iteration of which analyzes a single xml file
    for sub_directory in get_immediate_subdirectories(root_directory):
        
        #here we're just reconstructing the path to the desired file. The 10.2307_ bit is a constant prefix within the PT works in the first main subdirectory (1665-1678)
        path_to_xml = root_directory + "\\" + sub_directory + "\\" + "10.2307_" + sub_directory.split("-")[1] + ".xml"
        print path_to_xml
     
        with codecs.open( ".".join(basename(path_to_xml).split(".")[:-1]) + ".txt", "w", "utf-8") as out:
            fp = codecs.open(path_to_xml, "r", "utf-8").read()
            soup = BeautifulSoup(fp)
            
            text_nodes = soup.findAll("text", text = True)
            clean_text = ""
            for j in text_nodes:
                clean_text += " ".join(j)
                #it seems that when EJC exported xml, hypenated words at end of lines got a little ruffled, so now read "Ju- gler Vein..."; let's join these words back together 
            clean_text = clean_text.replace("- ","")
            #print clean_text
            
            #get title:
            clean_title = ""
            title = soup.findAll("title", text = True)
            for j in title:
                clean_title += " ".join(j)
            
            #get surname:
            clean_surname = ""
            surname = soup.findAll("surname", text = True)
            for j in surname:
                clean_surname += " ".join(j)
                
            #get givennames:
            clean_givennames = ""
            givennames = soup.findAll("givennames", text = True)
            for j in givennames:
                clean_givennames += " ".join(j)
                
            #get pub year:
            clean_year = ""
            year = soup.findAll("year", text = True)
            for j in year:
                clean_year += " ".join(j)
                
            #get language:
            try:
                clean_languages = soup.article.languages.contents[1].string
            except Exception as e:
                print e
                clean_languages = ""
                
            out.write(clean_text)
            metadata_out.write( basename(path_to_xml) + "\t" +
                               clean_year + "\t" +
                               clean_languages + "\t" +
                               clean_title + "\t" +
                               clean_givennames + "\t" +
                               clean_surname + "\n" )
            
            
            