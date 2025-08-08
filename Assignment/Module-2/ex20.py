def getdata(id,name,sub='Python'):
    print("Id : ",id)
    print("Name : ",name)
    print("Subject : ",sub)

# getdata(101,'vivek')      # positional argument
# getdata(101,'vivek', 'c#')
# getdata('vivek', 102)

getdata(id=101, name='vivek') # keyword arg.