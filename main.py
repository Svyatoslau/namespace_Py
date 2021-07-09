def create(namespace, parent):
    space_parent[namespace]=parent

def add(namespace, var):
    if namespace not in space_var:
        space_var[namespace]=[var]
    else:
        space_var.get(namespace).append(var)

def get(namespace, var):
    print(space_parent)
    print(space_var)
    if namespace in space_var and var in space_var[namespace]:
        print(namespace)
        return
    if namespace in space_parent:
        get(space_parent[namespace],var)
        return
    else:
        print('None')
        return

space_parent={}
space_var={}
n = int(input("Quantity of comand: "))
for i in range(n):
    command, namespace, var_par =input().split()
    if str(command) == 'create':
        create(namespace,var_par)
        continue
    elif str(command) == 'add':
        add(namespace,var_par)
        continue
    elif str(command) == 'get':
        get(namespace,var_par)

print(space_parent)
print(space_var)



