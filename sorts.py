#=============================================================
#  This is an implementation of the higher order function "sort" which is commonly found in high level languages
#  The original procedures were written in Scheme and I implemented them into python 
# 
#  The original procedures (which, as you can see, are very recursive) were:

# (define (sort sent)
#   (if (empty? sent)
#       '()
#       (insert (first sent)
#               (sort (bf sent)) )))

# (define (insert num sent)
#   (cond ((empty? sent) (se num))
#         ((< num (first sent)) (se num sent))
#         (else (se (first sent) (insert num (bf sent)))) ))
# ==========================================================

def sorts(sent):
# sent = [6,23,5,100,7,12.4,545,313453,65652,2,5674,6901]
    
    if(len(sent) == 0):
        return [];
    
    return insert( sent[0:1], sorts(sent[1:]) )


def insert(num, sent):
# num = [6]
    
    first = sent[0:1]
    butfirst = sent[1:] 

    if(len(sent) == 0):
        return num
   

    if(num < first):
        return num + sent
    else:
        return first + insert(num,butfirst) 


print(sorts([6,23,5,100,7,12.4,545,313453,65652,2,5674,6901]))
