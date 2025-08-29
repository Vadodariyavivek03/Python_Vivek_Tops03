import pandas

data = {
        'id': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
        'name' : ['Vivek', 'Yash', 'Ravi', 'Kiran', 'Sagar', 'Ramesh', 'Raj', 'Rahul', 'Karan', 'Kishan'],
        'age' : [21, 22, 23, 24, 25, 26, 27, 28, 29, 30], 
        'city' : ['Rajkot', 'Surat', 'Ahmedabad', 'Mumbai', 'Pune', 'Banglore', 'Chennai', 'Hydrabad', 'Delhi', 'Noida']
        }

df = pandas.DataFrame(data)
print(df)

