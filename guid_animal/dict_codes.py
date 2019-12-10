
import json
from guid_core.strip_accents import (text_to_id, format_age)

def return_code_from_json(cur_str, cur_json):

    with open(cur_json) as json_file:
        cur_dict = json.load(json_file)
        for key, elem in cur_dict.items():
            if text_to_id(cur_str) in elem:
                print("Found {}, corresponds to {}".format(
                    text_to_id(cur_str), key))
                return key
    print("Error {} could not be found in {}".format(
        text_to_id(cur_str), cur_json))
    return 0

def check_num_tat(num_tat):
    assert 0 < len(str(num_tat)) and  len(str(num_tat)) < 8, \
        "Error, {} not proper length".format(num_tat)
    return "{:07d}".format(num_tat)


def return_guid_animal_json(gender, origin, species, dob, index_anim = "A"):
    return "{}{}{}-{}{}".format(
        return_code_from_json(gender, "dict_gender.json"),
        return_code_from_json(origin, "dict_origin.json"),
        return_code_from_json(species, "dict_species.json"),
        format_age(dob, length_year = 2),
        index_anim
        )

print ("***", return_guid_animal_json("Male",'INT',"Marmouset", "01/01/1970"))
print ("***", return_guid_animal_json("Male",'INT',"Marmouset", "1970-01-01"))
print ("***", return_guid_animal_json("Male",'INT',"Marmouset", "1970-01/01","B"))
