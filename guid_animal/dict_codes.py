dict_gender = {"M":["M","MALE"],
               "F":["F","FEMALE"]}

dict_origin = {"R": ["ROUSSET"],
               "S": ["STRASBOURG"],
               "I": ["INT", "MARSEILLEINT",'INTMARSEILLE'],
               "J": ["JOSEPHAIGUIER", "JOSEPHAIGUIERMARSEILLE","MARSEILLEJOSEPHAIGUIER"]}

dict_species = {"F" : ["MACACAFASCICULARIS"],
                "M": ["MACACAMULATTA"],
                "O":["MARMOUSET", "OUISTITI"],
                "P":["PAPIO","PAPIOHPAPIO"],
                "S": ["SAIMIRI","SAIMIRISCIUREUS"]}

from generate_GUID.strip_accents import text_to_id

def return_code_from_dict(cur_str, cur_dict):

    for key, elem in cur_dict.items():
        print (elem)
        print (text_to_id(cur_str))
        if text_to_id(cur_str) in elem:
            return key
    return 0

def check_num_tat(num_tat):
    assert 0 < len(str(num_tat)) and  len(str(num_tat)) < 8, \
        "Error, {} not proper length".format(num_tat)
    return "{:07d}".format(num_tat)


def return_guid_animal(gender, origin, species, num_tat):
    return "{}{}{}-{}".format(
        return_code_from_dict(gender, dict_gender),
        return_code_from_dict(origin, dict_origin),
        return_code_from_dict(species, dict_species),
        check_num_tat(num_tat)
        )

print (return_guid_animal("Male",'INT',"Marmouset", 3592264))


print (return_guid_animal("F",'Joseph Aiguier',"MACACAMULATTA", 129494))
