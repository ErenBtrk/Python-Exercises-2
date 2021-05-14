'''
9. Write a Python program to display the examination schedule.
 (extract the date from exam_st_date). 
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014

'''



exam_st_date = (11,12,2014)
print( "The examination will start from : %i / %i / %i"%exam_st_date)

myString = "The examination will start from : "

for index in range(len(exam_st_date)):
    if(index == len(exam_st_date)-1):
        myString += str(exam_st_date[index])
    else:
        myString += str(exam_st_date[index]) + ' / '

print(myString)