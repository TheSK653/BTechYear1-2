age=int(input('Enter your age = '))
movie_rating=input('Enter the movie Rating (PG, PG-13, R, NC-17)')
if age>=18:
    rate='Any'
elif age>=17 and movie_rating in ['R', 'NC-17']:
    rate='R or NC-17'
elif age>=13 and movie_rating in ['PG', 'PG-13']:
    rate='PG and PG-13'
elif age>=7 and movie_rating in ['PG']:
    rate='PG'
else :
    rate='non'
print('Movie rating you can watch are =>',rate)