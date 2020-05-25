#!/bin/bash

ls *.pdf > list.txt
python even.py list.txt

# マージする
ls even_*.pdf > even_list.txt
python merge_pdf.py even_list.txt
