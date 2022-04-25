## This readme covers how the necessary dictionaries were generated.
* "Brazil geocodes state, city, municipal n=27, 135, 5572.xlsx" comes from mail thread "Brezilya için geocode, adm2 - 2020".
* "gadm40_BRA_3.json" was generated from "gadm40_BRA_3.dbf" file that comes from "https://www.ibge.gov.br/en/geosciences/full-list-geosciences/18890-municipal-mesh.html?=&t=downloads" 2021.

#### For district_coords_dict:
* I used "Brazil geocodes state, city, municipal n=27, 135, 5572.xlsx" to generate this dictionary.
* There were some duplicate names in "Municipality name" column, so I added "State name" to these
values. For example; "São Domingos" occured 5 times, so for "São Domingos" in "Sergipe" I changed
the name to "São Domingos, Sergipe"
* All the Municipality names has locality 6
* Then, I added Intermediarias having locality 3. Most of these names were already in the dictionary as municipality names.
I updated these to have locality 3, and updated their coordinates to have intermediarias coordinates.
* "Rio de Janeiro" and "São Paulo" Intermediarias were also state names. I did not add these to state_alternatives

#### For district_alternatives:
* Don't forget to lower everything
* As usual, I first added the keys in the dictionary as themselves
* Then, I started with "gadm40_BRA_3.json", containing districts
under municipalities. I made sure to match the municipalities to our district_coord_dict first.
* I added the alternatives to municipalities from the excel files sheet named "district to add municipalities"
* Dropped the alternatives that were district names themselves but were alternatives to other district names
* Dropped the alternatives that pointed to multiple names (not themselves)
* I added equivelants of some utf-8 characters such as 'é'->'e' as new entries.
* I added unicodedata.normalize() 'd versions of the names.
* For names with state names appended at the end with ', ', I added '()' paranthesis option.
* Finally, went over place_name_frequencies from pipeline output

#### For state_alternatives:
* Don't forget to lower everything
* As usual, I first added the states as themselves
* I added equivelants of some utf-8 characters such as 'é'->'e' as new entries.
* I added unicodedata.normalize() 'd versions of the names.
* Finally, went over place_name_frequencies from pipeline output