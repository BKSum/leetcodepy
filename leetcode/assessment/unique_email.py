from typing import List


class UniqueEmail:
    @staticmethod
    def handleDot(email: str) -> str:
        indexAt = email.index("@")
        beforeAt = email[:indexAt]
        afterAt = email[indexAt:]
        return beforeAt.replace(".", "") + afterAt

    @staticmethod
    def handleFirstPlus(email: str) -> str:
        try:
            plusIndex = email.index("+")
        except ValueError:
            return email
        indexAt = email.index("@")
        beforeAt = email[:indexAt]
        afterAt = email[indexAt:]
        beforePlus = beforeAt[:plusIndex]
        return beforePlus + afterAt

    def actualEmail(self, email: str) -> str:
        return self.handleDot(self.handleFirstPlus(email))

    def numUniqueEmails(self, emails: List[str]) -> int:
        outputSet = set()
        for email in emails:
            outputSet.add(self.actualEmail(email))
        return len(outputSet)
