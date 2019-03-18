# https://imgur.com/a/mvts0Ot

# jes = JobExpirationState();
# jes.isExpired(10); // -> false
# jes.expire(10);
# jes.isExpired(10); // -> true

class JobExpirationState:
    def __init__(self):
        # 1,2,3,4,5,6  range(1,6)
        # maximum job ID:
        # bits[]
        # old jobs and new jobs
        #   10000
        # new jobs : set()
        # old jobs: record the not yet expired job ids
        # 
        
        
        #1,2,3       10001,10002~11000,   110000-120000
        # (1000+3+
        self.old_not_expired = set()
        self.new_expired = set()
        self.sep = 0
        self.threshold = 10000
        self.max_job_id = 0
        
    def expire(self, jobID):
        self.max_job_id = max(self.max_job_id, jobID)
        if jobID > self.sep:
            self.new_expired.add(jobID)
            if len(self.new_expired) > self.threshold:
                self.adjust()
        elif jobID in self.old_not_expired:
            self.old_not_expired.pop(jobID)

        
    def isExpired(self, jobID):
        if jobID > self.sep:
            return jobID in self.new_expired
        else:
            return jobID not in self.old_not_expired

    def adjust(self):
        count = 0
        # go from i to    x ( i <= x <= max_job_id)
        # time : O(x_1-i)
        # time : O(x_2-x_1)
        # ...
        # time: O(max_job_id - x_n)
        # added up to : O(max_job_id) 
        for i in range(self.sep, self.max_job_id):
            if i not in self.new_expired: continue
            count += 1
            if count > 100 and count*1.0/(i-self.sep) < 0.9:
                break
        if count > 100:
            for j in range(self.sep, i):
                if i in self.new_expired:
                    self.new_expired.pop(i)
                else:
                    self.old_not_expired.add(i)
            self.sep = i
                
        
        
