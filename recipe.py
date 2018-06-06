import argparse

parser = argparse.ArgumentParser(description='Diablo2 Recipe Searcher')
parser.add_argument('basepath', metavar='BASEPATH', nargs='?', help="The Base path containing the D2 recipe files")
parser.add_argument("--verbosity", help="Set logging level", type=int)
args = parser.parse_args()
basepath = args.basepath if args.basepath else "."
verbosity = args.verbosity if args.verbosity else 0

def debug(*args):
	global verbosity
	if verbosity >= 1: print(' '.join(args))


def splitline(line):
	return line.strip().split('\t')

def readfile_txt(path):
	data = []
	with open(path, 'rU') as f:
		headers = splitline(f.readline())
		debug(repr(headers))
		for line in f:
			values = splitline(line)
			if len(values) == len(headers):
				values = dict(zip(headers, values))
				#values = {k: v for k, v in values.items() if v != ""}
				data.append(values)
	return data

def call_with_time_log(start, stop, func, *args, **kwargs):
	import time
	print("-- " + start)
	t = time.time()
	res = func(*args, **kwargs)
	t = time.time() - t
	print("-- " + stop + " (" + str(float(int(t*1000))*0.001) + "s)")
	return res

def misc_dict(misc):
	return {m['code']: (m['name'].lower(), m) for m in misc}

def update_recipes_with_names(recipes):
	global names
	recipes = [recipe.copy() for recipe in recipes if recipe['enabled'] == '1']
	#often = int(len(recipes) / 10)
	#c = 1
	#state = 0
	#print(often)
	for recipe in recipes:
		#if c % often == 0:
		#	print(state, end='', flush=True)
		#	state = state + 1
		#print(c, often, c%often)
		#c = c + 1
		for k, v in recipe.items():
			if v != "":
				if v in names:
					recipe[k] = '"' + names[v][0] + ' (' + v + ')"'
				vv = v.strip('"').split(',')
				if len(vv)>0 and vv[0] in names:
					vv[0] = '"' + names[vv[0]][0] + ' (' + vv[0] + ')"'
					recipe[k] = ','.join(vv)
	return recipes


def process_cases(recipes, misc):
	for recipe in recipes:
		for key in ['input 1', 'input 2', 'input 3', 'input 4', 'input 5', 'input 6', 'input 7', 'output', 'output b', 'output c']:
			recipe[key] = recipe[key].lower()
	for item in misc:
		item['code'] = item['code'].lower()


from os import path

recipes = call_with_time_log("Importing recipes", "Importing recipes complete", readfile_txt, path.join(basepath, "cubemain.txt"))
misc = call_with_time_log("Importing items", "Importing items complete", readfile_txt, path.join(basepath, "misc.txt"))
call_with_time_log("Processing cases...", "Processing cases complete", process_cases, recipes, misc)
names = call_with_time_log("Processing names", "Processing names complete", misc_dict, misc)
#recipes = call_with_time_log("Applying names", "Applying names complete", update_recipes_with_misc, recipes, misc)

#print(repr(recipes[0].keys()))
#print(repr(misc['elix'].keys()))
#print(misc['cblk']['name'])
#print(repr({k: v for k, v in recipes[200].items() if v != ""}))
#print(repr(recipes[1700]))



def cmd_help():
	global cmds
	lst = [(k, v[1]) for k, v in cmds.items()]
	lst.sort()
	print("Known commands:")
	for cmd in lst:
		print("%s: %s"%(cmd[0], cmd[1]))


def match_items(*ands):
	global names
	matches = []
	ands = [s.lower() for s in ands]
	if len(ands) > 0:
		for _, data in names.items():
			name = data[0]
			found = len(ands)
			for s in ands:
				if s in name:
					found = found - 1
			if found == 0:
				matches.append(data[1])
	return matches

def cmd_items(*ands):
	matches = match_items(*ands)
	if len(ands) == 0:
		print("Need argument to search")
	elif len(matches) == 0:
		print("No matches found")
	else:
		matches = [" - ".join([item['code'], item['name'], item['*name'], item['szFlavorText']]) for item in matches]
		matches.sort()
		print('\n'.join(matches))


def whitespace_extra_key(key):
	if " " in key:
		return "ZZZ" + key
	return key
def cmd_itemdetail(code):
	global names
	if code not in names:
		print("Unknown item code")
	else:
		item = names[code][1]
		keys = list(item.keys())
		sorted(keys, key=whitespace_extra_key)
		for key in keys:
			v = item[key]
			if v != '' and v != '0': # Hide default fields
				print(": ".join([key, v]))


def recipe_contains_code(recipe, codes):
	keys = list(recipe.keys())
	keys.sort()
	for code in codes:
		#codea = code+","
		codeb = '"'+code+","
		for key in ['input 1', 'input 2', 'input 3', 'input 4', 'input 5', 'input 6', 'input 7', 'output', 'output b', 'output c']:
			value = recipe[key]
			if value != "":
				if value == code or value.startswith(codeb): # or value.startswith(codea)
					return True
	return False


def display_recipes(recipes):
	recipes = update_recipes_with_names(recipes)
	for recipe in recipes:
		print("%s : %s <- %s" % (
			recipe['description'],
			' + '.join([x for x in [recipe['output'], recipe['output b'], recipe['output c']] if x != ""]),
			' + '.join([x for x in [recipe['input 1'], recipe['input 2'], recipe['input 3'], recipe['input 4'], recipe['input 5'], recipe['input 6'], recipe['input 7']] if x != ""]),
			))

def cmd_itemrecipesnamed(*ands):
	global recipes
	matches = match_items(*ands)
	if len(ands) == 0:
		print("Need argument to search")
	elif len(matches) == 0:
		print("No matches found")
	else:
		[print("Item %s (%s) type: %s" % (item['name'], item['code'], item['type'])) for item in matches]
		print("")
		out_recipes = []
		often = int(len(recipes) / 10)
		c = 0
		state = 0
		print("Scanning: ", end='')
		for recipe in recipes:
			if (c % often) == 0:
				print(state, end='0% ', flush=True)
				state = state + 1
			c = c + 1
			for item in matches:
				if recipe_contains_code(recipe, [item['code'], item['type']]):
					out_recipes.append(recipe)
					break
		print("\n")
		display_recipes(out_recipes)

def cmd_itemrecipes(*codes):
	global recipes
	if len(codes) == 0:
		print("Need argument to search")
	else:
		codes = [code.lower() for code in codes]
		out_recipes = []
		often = int(len(recipes) / 10)
		c = 0
		state = 0
		print("Scanning: ", end='')
		for recipe in recipes:
			if (c % often) == 0:
				print(state, end='0% ', flush=True)
				state = state + 1
			c = c + 1
			for code in codes:
				if recipe_contains_code(recipe, [code]):
					out_recipes.append(recipe)
					break
		print("\n")
		display_recipes(out_recipes)


import sys

cmds = {
	'quit': (lambda: sys.exit(0), "Exit the program"),
	'help': (cmd_help, "Show this help"),
	'?': (cmd_help, "Show this help"),
	'in': (cmd_items, "Search item names, the item code is listed first on each line"),
	'id': (cmd_itemdetail, "Show Item Details by code"),
	'rin': (cmd_itemrecipesnamed, "Search Recipes by item names"),
	'ri': (cmd_itemrecipes, "Search Recipes by item code")
}


while True:
	print("\nEnter command ('help' for help, 'quit' to quit):\n> ", end='')
	inp = input().strip().split(' ')
	print('')
	if len(inp) >= 1 and inp[0].lower() in cmds:
		cmds[inp[0].lower()][0](*(inp[1:]))
	else:
		print("Invalid command\n")
