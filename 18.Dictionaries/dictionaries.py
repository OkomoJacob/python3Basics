'''
Used esp in Situations which comes in key vaue pairs

e.g 
Name : John Smith
Age: 40
weight:30
'''
customer = {
    'name ':"John smith",
    "age":40,
    "is_authentiacted":True
}
customer["name"] = "John Doe"
print(customer.get("name"))
print(customer.get("birthday","Jan 1998"))

