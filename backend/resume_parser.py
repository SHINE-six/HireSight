from pydparser import ResumeParser
import json

def parse_resume(file_name):
    data = ResumeParser(f"resume/resume_in/{file_name}").get_extracted_data()
    json_file_path = f"{file_name[:-4]}.json"
    with open(f"resume/resume_out/{json_file_path}", "w") as json_file:
        json.dump(data, json_file, indent=4)
    print("\033[92m200 OK\033[0m: Resume parsed successfully.")
    return data
