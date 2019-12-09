
import json
from generate_GUID.strip_accents import text_to_id

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


def return_guid_animal_json(gender, origin, species, num_tat):
    return "{}{}{}-{}".format(
        return_code_from_json(gender, "dict_gender.json"),
        return_code_from_json(origin, "dict_origin.json"),
        return_code_from_json(species, "dict_species.json"),
        check_num_tat(num_tat)
        )

print (return_guid_animal_json("Male",'INT',"Marmouset", 3592264))
print (return_guid_animal_json("F",'Joseph Aiguier',"MACACAMULATTA", 129494))
