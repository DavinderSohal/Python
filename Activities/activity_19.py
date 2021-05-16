import csv
import matplotlib.pyplot as plt
import numpy as np
def k(a,b):
    print("Enter the word:")
    w=input("")
    wr = w[::-1]
    if w=='quit':
        p = np.array( [a, b] )
        mylabels = ["Palindromes", "NotAPalindrome"]
        plt.pie( p, labels=mylabels )
        plt.savefig( "image.png" )
        plt.show()
        exit()
    else:
        if w==wr:
            o1.write( str( w ) )
            o1.write( '\n' )
            a=a+1
            p = np.array( [a, b] )
            mylabels = ["Palindromes", "NotAPalindrome"]
            plt.pie( p, labels=mylabels )
            plt.show()
        else:
            o2.write( str( w ) )
            o2.write( '\n' )
            b=b+1
            p = np.array( [a,b] )
            mylabels = ["Palindromes", "NotAPalindrome"]
            plt.pie( p, labels=mylabels )
            plt.show()
        k(a,b)

o1 = open( "Palindromes" + '.txt', 'w' )
o2= open( "NotAPalindrome"+ '.txt', 'w' )
k(0,0)