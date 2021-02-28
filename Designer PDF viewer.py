#Link: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

#Code:
def designerPdfViewer(h, word):
    s = "abcdefghijklmnopqrstuvwxyz"
    l = []
    for i in word:
        t = s.index(i)
        l.append(t)
    m = 0    
    for r in l :
        if h[r] > m:
            m = h[r]
    return(m*len(word))        
          
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
