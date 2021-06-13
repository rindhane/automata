#! /usr/bin/env python
from pdf_to_img import main as converter 
import os 

def get_inputs(path,file_,final_img_path,prefix,format_,full_check):
    inputs=dict()
    inputs['pdf']=path+'/'+file_
    inputs['imgFolder']=final_img_path
    inputs['prefix']=prefix
    inputs['format']=format_
    inputs['full']=full_check 
    return inputs

def main(path):
    final_img_path='images'
    prefix='temps'
    format_='png'
    full_check='yes'
    files=os.listdir(path)
    for file_ in files:
        inputs=get_inputs(path,file_,final_img_path,prefix,format_,full_check)
        converter(inputs)
    return True

if __name__=='__main__':
    main(path='Conversion')