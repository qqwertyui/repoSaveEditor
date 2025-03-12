Simple save editor for R.E.P.O

Save files can be found under X:\Users\\$USER\AppData\LocalLow\semiwork\Repo\saves

# 1. Installation
> pip3 install -r requirements.txt

# 2. Usage
> python3 edit.py <inputSave.es3> -s \<python assignment statement\> -o <modifiedSavePath.es3>

# 3. Examples
## change round number:
> python3 edit.py inputSave.es3 -s 'data["dictionaryOfDictionaries"]["value"]["runStats"]["level"] = 20' -o modifiedSave.es3

## increase max HP:
> python3 edit.py inputSave.es3 -s 'data["dictionaryOfDictionaries"]["value"]["playerUpgradeHealth"]["\<steamId\>"] = 10' -o modifiedSave.es3
