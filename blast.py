# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 13:32:53 2018

@author: Alfredo Gonzalez-Sulser, University of Edinburgh
email: agonzal2@staffmail.ed.ac.uk
"""
#lines = []
#for line in open('blast_result.txt'):
#    lines.append(line)
#print(lines)



def comment_filter(lines): 
    return not lines.startswith('#') 

hit_lines = filter(comment_filter, open('blast_result.txt'))

def mismatch_filter(hit_string): 
    mismatch_count = int(hit_string.split("\t")[4]) 
    return mismatch_count < 20 

#mismatch_count=mismatch_filter(hit_lines)
    
#print(len(list(filter(mismatch_filter, hit_lines))))


def get_percent_id(hit_string): 
    return float(hit_string.split("\t")[2]) 


#x=get_percent_id(hit_lines)

s= sorted(hit_lines, key=get_percent_id)
        
low_id_hits = s[0:10] 

print(low_id_hits)

#
#
