favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['C'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    if len(languages) < 2:
        continue
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())