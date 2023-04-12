try:
    age=int(input('age '))
    income=20000
    risk=income/age
    print(risk)
except ZeroDivisionError:
    print('age cannot br 0')
except ValueError:
    print("invalid value")
    
    

