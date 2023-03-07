## This readme covers how the necessary dictionaries were generated.
* "Argentina geocodes provincios deparamentos municipios n=24, 529, 1758.xlsx" comes from mail thread
"Brezilya için geocode, adm2 - 2020".
* "argentina_cities.csv" is a subset of "worldcities.csv" (acquired from https://simplemaps.com/data/world-cities)
that only contains cities from Argentina that are not already in our municipio list in the excel.
* "gobiernoslocales_2020.csv" comes from mail thread "Brezilya için geocode, adm2 - 2020". It contains
municipios, their provincia and coordinates much like the excel file. But, it is more complete than
the excel; it contains municipios for 4 more provincias than the excel. -> "Entre Ríos", "San Juan",
"Santa Cruz", "Santiago del Estero"
* "barrios_comunas_p_Ciencia_de_Datos_y_PP.csv" comes from mail thread "Brezilya için geocode, adm2 - 2020".
It contains barrios inside the Buenos Aires city.

#### For district_coords_dict:
* I used "Argentina geocodes provincios deparamentos municipios n=24, 529, 1758.xlsx" to generate this
dictionary.
* 3 of the municipalities were missing their province(state) names, I filled these manually.
* There were some duplicate names in "mun_name" column, so I added "pro_name" to these
values. For example; "San José" occured 3 times, so for "San José" in "Catamarca" I changed
the name to "San José, Catamarca". After this, there was a single muni that still had a duplicate entry,
so I discarded its duplicate since their coordinates were very close.
* All the Municipality names has locality 6
* Then, I used "argentina_cities.csv" to add the cities of Argentina with locality 3. The "admin_name"
column is the state name for the given city.
* Finally, I used "gobiernoslocales_2020.csv" to add the municipios of the missing 4 provincias.

#### For district_alternatives:
* Don't forget to lower everything
* As usual, I first added the keys in the dictionary as themselves
* I added equivelants of some utf-8 characters such as 'é'->'e' as new entries.
* I added unicodedata.normalize() 'd versions of the names.
* For names with state names appended at the end with ', ', I added '()' paranthesis option.
* I added the barrios that map to Buenos Aires city from "barrios_comunas_p_Ciencia_de_Datos_y_PP.csv"
file.

#### For state_alternatives:
* Don't forget to lower everything
* As usual, I first added the states as themselves
* I added equivelants of some utf-8 characters such as 'é'->'e' as new entries.
* I added unicodedata.normalize() 'd versions of the names.
