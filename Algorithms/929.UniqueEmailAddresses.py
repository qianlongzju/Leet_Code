class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()
        for email in emails:
            local, host = email.split("@")
            if '+' in local:
                local = local[:local.index('+')]
            local = "".join(local.split("."))
            unique_emails.add(local+"@"+host)
        return len(unique_emails)
