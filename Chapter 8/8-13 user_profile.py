# Building my own profile with build_profile() function.
# Use first_name and last_name as key-value pairs.
# Add three other key-value pairs.

def build_profile(first_name, last_name, **profile_info):
    profile_info['first_name'] = first_name.title()
    profile_info['last_name'] = last_name.title()
    return profile_info


profile = build_profile('isiah', 'scott',
                        blood_type='O',
                        language='Japanese',
                        location='Kentucky')
print(profile)
