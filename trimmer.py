import ruamel.yaml

# Create the YAML parser object
yaml = ruamel.yaml.YAML()

print("Loading YAML file...")
# Open the YAML file in binary mode for better performance
with open("bitnami/index.yaml", "r") as f:
    data = yaml.load(f)

print("Read the entries...")
# Remove all the entries except postgresql-ha
for key in list(data["entries"].keys()):
    if key != "postgresql-ha":
        print("Removing entry: %s" % key)
        del data["entries"][key]

print("Write the entries...")
# Write the entries back to the file
with open("bitnami/index.yaml", "w") as f:
    yaml.dump(data, f)

print("Done!")