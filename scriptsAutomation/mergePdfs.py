from PyPDF2 import PdfFileMerger, PdfFileReader
import os 
import argparse

#argparse definitions
parser = argparse.ArgumentParser(description='Merge Individual pdfs within a folder to a single file')
parser.add_argument('--files_folder', type=str, default='./pdfs',
                        help='path to folder containing folder pdfs or default is ./pdfs')
                        
parser.add_argument('--final_file',metavar='f', type=str, default='./resultant.pdf',
                        help='path to save final merged file or default is  is ./resultant.pdf')

args=parser.parse_args()

def get_individual_file_from_walk (root):
    for path,_,files in os.walk(root):
        for file_ in files:
            yield path+'/'+file_


def main(path1=args.files_folder,path2=args.final_file):
    #initiate path variable 
    individual_pdfs_folder_path= path1
    path_final_pdf= path2
    # get individual pdfs from the path specified
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