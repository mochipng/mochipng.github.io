import os

# Define input and output locations for files
inputLo = "./HTML/Posts/Text/"
outputLo = "./HTML/Posts/"

# Lists txt files in the input directory and makes html files in the output directory
for filename in os.listdir(inputLo):
    if filename.endswith(".txt"):

        # Make sure dictonary is empty after previous posts
        infoDict = {}

        # Read the txt files and extract key and value into dict on each line (with ":")
        with open(os.path.join(inputLo, filename),"r", encoding="utf-8") as file:
            for line in file:
                if ":" in line:
                    key, value = line.split(":", 1)
                    # Get rid of whitespace and adds new key-value pair to the dictionary
                    infoDict[key.strip()] = value.strip()

        # Read template file and format string copy with the infoDict
        with open("./HTML/Posts/blogTemplate.html", "r", encoding="utf-8") as templateFile:
            template = templateFile.read()
            blogFile = template.format(
                title = infoDict.get("title", ""),
                date = infoDict.get("date", ""),
                text = infoDict.get("text", "")
            )

            # create output file name in directory and makes proper file title
            outputFile = os.path.join(outputLo + infoDict.get("title","post").replace(" ","_") + ".html")

            # Write formated string to the output file
            with open(outputFile, "w", encoding="utf-8") as file:
                file.write(blogFile)

# Success message
print("Successfully created blog post(s): " + outputFile)
