"""Generate resume based on input"""
import os

class Resume:

    def __init__(self, log: object):
        self.log = log
        self.resume_path = os.path.join(os.getcwd(), 'resumes')
        if not os.path.exists(self.resume_path):
            os.makedirs(self.resume_path)


    def generate_resume(self, candidate: dict):
        """Generate resume as TXT file and store it on folder"""

        try:
            resume_name =  candidate["full_name"].replace(" ", "-") + '.txt'
            resume_full_path = os.path.join(self.resume_path,resume_name)

            name = "Full Name = " + candidate["full_name"]
            email = "Email = " + candidate["email"]
            vacancy = "Vancancy = " + candidate["vacancy"]

            infos = [name, email, vacancy]
            with open(resume_full_path, 'w') as f:
                for item in infos:
                    f.write(item)
                    f.write('\n')

            self.log.register_info("Resume generated succesfully")
            return resume_full_path
        except Exception as error:
            self.log.register_error("Resume for candidate {} not generated. Description of error: {} ".format(candidate["full_name"], error))
            raise error
        
        