from PyPDF2 import PdfFileMerger, PdfFileReader
import os 
import argparse
import re

#argparse definitions
parser = argparse.ArgumentParser(description='Merge Individual pdfs within a folder to a single file')
parser.add_argument('--files_folder', type=str, default='./pdfs',
                        help='path to folder containing folder pdfs or default is ./pdfs')
                        
parser.add_argument('--final_file',metavar='f', type=str, default='./resultant.pdf',
                        help='path to save final merged file or default is  is ./resultant.pdf')
parser.add_argument('--order_merge',metavar='o', type=str, default=None,
                        help='if ordering regex is defined in the function within the program')

args=parser.parse_args()

def get_individual_file_from_walk (root):
    for path,_,files in os.walk(root):
        for file_ in files:
            yield path+'/'+file_

def regexSorting(reg,string):
	return int(re.findall(re.compile(reg),string)[0])

def order_the_files(path):
	reg='\d+'
	file_iterator=get_individual_file_from_walk(path)
	seq=dict()
	files=list()
	for file_ in file_iterator:
		seq[file_]=regexSorting(reg,file_)
		files.append(file_)
	return sorted(files, key=lambda x : seq[x])  


def main(path1=args.files_folder,path2=args.final_file,order=args.order_merge):
    #initiate path variable 
    individual_pdfs_folder_path= path1
    path_final_pdf= path2
    # get individual pdfs from the path specified
    if order :
        files=order_the_files(individual_pdfs_folder_path)
    else:
        files=get_individual_file_from_walk(individual_pdfs_folder_path)
    # Call the PdfFileMerger
    mergedObject = PdfFileMerger() 
    # Write all the files into a file which is named as shown below
    for fileName in files:
        mergedObject.append(PdfFileReader(fileName, 'rb'))
    mergedObject.write(path_final_pdf)
    print(f'Merged file saved at location : {path_final_pdf}')

if __name__ =="__main__":
    main(path1=args.files_folder,path2=args.final_file)
