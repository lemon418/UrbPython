immutable_var = 1984, ["green", "red"], False
print(immutable_var)

immutable_var[2] = True
# кортеж нельзя изменить, но можно изменять объекты на которые он ссылается.
# Это что то вроде списка ссылок, которые ведут к объектам, к которым, в свою очередь можно обращаться и работать с ними".

mutable_list = ["comedy", "fantasy", "action"]
mutable_list[0] = "drama"
mutable_list[1] = "horror"
mutable_list[2] = "fantastic"
print(mutable_list)