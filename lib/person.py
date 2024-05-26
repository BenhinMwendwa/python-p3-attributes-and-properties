
APPROVED_JOBS = [
"Admin",
"Customer Service",
"Human Resources",
"ITC",
"Production",
"Legal",
"Finance",
"Sales",
"General Management",
"Research & Development",
"Marketing",
"Purchasing"
]

class Person:
  def __init__(self,job="sales"):
    self.job = job
  def get_job(self):
     return self._job 
  def set_job(self, job): 
     if job not in APPROVED_JOBS:
        print("Job must be in list of approved jobs.")
      return
        self._job = job
