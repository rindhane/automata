#! /usr/bin/env python

from pdf2image import convert_from_path
import argparse
import img2pdf

def get_all_pages_pdf(pdf_path):
    print('file in conversion',pdf_path)
    imgPages = convert_from_path(pdf_path)
    return imgPages


def save_imgPages(imgPages,imgFolder,prefix,format_):
    imgs=list()
    for _idx, page in enumerate(imgPages):
        path=imgFolder+'/'+prefix+f'__{_idx}'+'.'+format_
        page.save(path,format_)
        imgs.append(path)
    return imgs

def get_splits(ls):
    tmp=ls[:-1]
    out=''
    for string in tmp:
        out=out+string+'.'
    return out

def run_parser():
    parser = argparse.ArgumentParser(description='Img to pdf and vice versa converters')
    parser.add_argument('pdf', metavar='i',
                    help='relative path to pdf')
    parser.add_argument('--output_path', metavar='o',dest='imgFolder' , 
            default='.', help='relative path to pdf')
    parser.add_argument('--format', metavar='f' ,dest='format', 
                    default='png', help='filetype of image')
    parser.add_argument('--prefix', metavar='p' ,dest='prefix', 
                    default='img', help='prefix initals of output image')
    parser.add_argument('--fullconvert', metavar='z', dest='full',
                     default='None', help='final output to pdf')
    return parser

def parser_to_inputs(parser):
    args=parser.parse_args()
    inputs=dict()
    inputs['pdf']=args.pdf
    inputs['imgFolder']=args.imgFolder
    inputs['prefix']=args.prefix
    inputs['format']=args.format
    inputs['full']=args.full
    return inputs

def main(inputs):
    imgPages=get_all_pages_pdf(inputs['pdf'])
    imgs=save_imgPages(imgPages,inputs['imgFolder'],inputs['prefix'],inputs['format'])
    if inputs['full']!='None':
        name_without_suffix=get_splits(inputs['pdf'].split('.'))
        final_name=name_without_suffix[:-1]+'__new'+'.pdf'
        with open(final_name,'wb') as fp:
            fp.write(img2pdf.convert(imgs))
        print(f'file created {final_name}')
    return True

if __name__=='__main__':
    inputs=parser_to_inputs(run_parser())
    main(inputs)