# Nested Dictionary : Inner list dictionary..... [{___}].

# data = [{"id":101, "name":"Vivek", "age":21}, 
#         {"id":102, "name":"Meet", "age":24},
#         {"id":103, "name":"Aarav", "age":18}]

# print(data)

# --------------------------------------- #

# for i in data:
#     print(i)

# --------------------------------------- #

# for i in data:
#     print(i["name"])

# --------------------------------------- #

# Nested Dict.. : Inner dictionary {{___}}.

data = {
    "st1" : {"id":101, "name":"Vivek", "age":21},
    "st2" : {"id":102, "name":"Meet", "age":24},
    "st3" : {"id":103, "name":"Aarav", "age":18}
}

# --------------------------------------- #

print(data)
print(data["st1"])
print(data["st1"]["name"])

# --------------------------------------- #
