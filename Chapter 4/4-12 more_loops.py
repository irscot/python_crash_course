# All versions of foods.py in this section have avoided using
# for loops when printing to save space. Choose a version of foods.py, and
# write two for loops to print each list of foods.

# No... no I don't think I will. How about anime characters?

anime_characters_m = ['edogawa conan', 'kiriyama rei', 'okabe rintaro']

anime_characters_f = ['tsubasa hanekawa', 'misaka makoto', 'makise kurisu']

print("\nMy favorite male anime characters are:")
for anime_character_m in anime_characters_m:
    print(f"- {anime_character_m.title()}")

print("\nMy favorite female anime characters are:")
for anime_character_f in anime_characters_f:
    print(f"- {anime_character_f.title()}")