def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('narayan', 'gopal')
print(musician)



def get_formatted_name(first_name, last_name, middle_name=''):
  """Return a full name, neatly formatted."""
  if middle_name:
    full_name = first_name + ' ' + middle_name + ' ' + last_name
  else:
    full_name = first_name + ' ' + last_name
  return full_name.title()

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


# Returning a Dictionary
def name_(first_name, last_name):
   person = {"First": first_name, "Last ": last_name}
   return person
musician = name_("tylor", "Swift")
print(musician)


def build_person(first_name, last_name, age = ''):
   person = {'first': first_name, 'last': last_name}

   if age:
      person['age'] = age
   return person

musician = build_person("jungkook","Sharma", age=26) 
print(musician)