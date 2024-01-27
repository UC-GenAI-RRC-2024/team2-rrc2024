import os

def extract_text(file_path):
    with open("/home/team-2/PG-Data-main/Project 2/promed_email_newsletters/" + file_path, 'r') as file:
        content = file.read()

    # Find the indices of the second occurrence of "Mime-Version: 1.0" and the first occurrence of "Byline"
    mime_version_index = content.find("Mime-Version: 1.0", content.find("Mime-Version: 1.0") + 1)
    byline_index = content.find("ProMED map")

    # Extract and print the text between the two indices
    extracted_text = content[mime_version_index+19:byline_index-2].strip()


    newFile = open("/home/team-2/ExtractedEmails/{0}.txt".format(file_path), "w")
    newFile.write(extracted_text)
    newFile.close()


for email in os.listdir("/home/team-2/PG-Data-main/Project 2/promed_email_newsletters"):
    extract_text(email)




