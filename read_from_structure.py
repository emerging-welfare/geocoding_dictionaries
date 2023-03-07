import pandas as pd
import json
import unicodedata
import ipdb

# input_filename = "/home/omutlu/geocoding_dictionaries/argentina/lanacion_non_matched_place_name_frequencies_fd_cleaned.tsv"
input_filename = "/home/omutlu/geocoding_dictionaries/brazil/Eduardo_20221206_non_matched_place_name_freqs.xlsx"
out_dir = "/home/omutlu/geocoding_dictionaries/brazil"

dist_filename = "{}/district_alternatives.tsv".format(out_dir)
state_filename = "{}/state_alternatives.tsv".format(out_dir)
foreign_filename = "{}/foreign_alternatives.tsv".format(out_dir)
ignore_filename = "{}/ignore_list.json".format(out_dir)

dist_alts = pd.read_csv(dist_filename, sep="\t")
state_alts = pd.read_csv(state_filename, sep="\t")
foreign_alts = pd.read_csv(foreign_filename, sep="\t")
with open(ignore_filename, "r", encoding="utf-8") as f:
    ignore_list = json.loads(f.read())

# df = pd.read_csv(input_filename, sep="\t")
df = pd.read_excel(input_filename)
df = df.fillna(0)
if len(df[df.State + df.District + df.Ignore + df.Foreign > 1]) > 0:
    # TODO: Some rows can have value 2. Prefer the column with the value 1 in that case.
    ipdb.set_trace()

df = df[df.State + df.District + df.Ignore + df.Foreign == 1]

ignore_list = ignore_list + df[df.Ignore == 1].place_name.str.lower().tolist()
ignore_list = ignore_list + [unicodedata.normalize("NFKD", name) for name in df[df.Ignore == 1].place_name.str.lower().tolist()]
ignore_list = list(set(ignore_list))

to_be_added = []
for freq, alt, name in zip(df[df.State == 1].frequency.tolist(), df[df.State == 1].place_name.tolist(), df[df.State == 1]["linked place entity"].tolist()):
    if name not in state_alts.name.unique().tolist():
        print("State name not known: {}. Its alternative is {}. Its frequency is {}".format(name, alt, freq))
        continue
    alt = alt.lower()
    to_be_added.append({"alt": alt, "name": name})
    unicode_alt = unicodedata.normalize("NFKD", alt)
    if unicode_alt != alt:
        to_be_added.append({"alt": unicode_alt, "name": name})
if to_be_added:
    state_alts = state_alts.append(to_be_added, ignore_index=True)

to_be_added = []
for freq, alt, name in zip(df[df.District == 1].frequency.tolist(), df[df.District == 1].place_name.tolist(), df[df.District == 1]["linked place entity"].tolist()):
    if name not in dist_alts.name.unique().tolist():
        print("District name not known: {}. Its alternative is {}. Its frequency is {}".format(name, alt, freq))
        continue
    alt = alt.lower()
    to_be_added.append({"alt": alt, "name": name})
    unicode_alt = unicodedata.normalize("NFKD", alt)
    if unicode_alt != alt:
        to_be_added.append({"alt": unicode_alt, "name": name})
if to_be_added:
    dist_alts = dist_alts.append(to_be_added, ignore_index=True)

to_be_added = []
for alt in df[df.Foreign == 1].place_name.tolist():
    name = alt
    alt = alt.lower()
    to_be_added.append({"alt": alt, "name": name})
    unicode_alt = unicodedata.normalize("NFKD", alt)
    if unicode_alt != alt:
        to_be_added.append({"alt": unicode_alt, "name": name})
if to_be_added:
    foreign_alts = foreign_alts.append(to_be_added, ignore_index=True)

with open(ignore_filename + "2", "w", encoding="utf-8") as f:
    f.write(json.dumps(ignore_list, ensure_ascii=False))
dist_alts.to_csv(dist_filename + "2", sep="\t", index=False)
state_alts.to_csv(state_filename + "2", sep="\t", index=False)
foreign_alts.to_csv(foreign_filename + "2", sep="\t", index=False)
