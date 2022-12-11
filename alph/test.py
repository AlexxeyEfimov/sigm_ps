dict_2 = {}
dict_1 = {}
var = []
dict_1['global'] = 'None'

def create(namespace,arg):
    dict_1.setdefault(namespace,[]).append(arg)
    dict_2.setdefault(namespace,[]).append('')

def add(namespace,arg):
    dict_2.setdefault(namespace,[]).append(arg)
    var.append(arg)

def get(namespace,arg):

	if (arg in var) == False:
		result = None
		print(result)
		return

	if dict_2.get(namespace) != None:

		if (arg in dict_2.get(namespace)) == True:
			result = namespace
			print(result)
			return
		else:

			parent = str(dict_1.get(namespace)).replace('[','').replace(']','').replace("'",'')
			obj = True

			while obj == True:

				parent = str(dict_1.get(namespace)).replace('[','').replace(']','').replace("'",'')
				if (parent == 'None') and ((arg in dict_2.get(namespace)) == True):
					obj = False
					result = 'global'
					print(result)
					return
				elif dict_2.get(parent) != None:
					if (arg in dict_2.get(parent)) == True:
						result = parent
						print(result)
						obj = False
						return

				else:
					result = 'None'
					print(result)
					return

				namespace = parent
				parent = str(dict_1.get(namespace))
	else:
		result = 'None'
		print(result)
		return
