def find_defining_class(obj, method_name):
	""" Find the class which has the definition of the method """
	for ty in type(obj).mro():
		if method_name in ty.__dict__:
			return ty
		