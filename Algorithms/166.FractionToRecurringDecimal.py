class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        if numerator * denominator >= 0:
            result = ""
        else:
            result = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator % denominator == 0:
            return result + str(numerator / denominator)
        left = numerator / denominator
        numerator %= denominator
        reminders = []
        numerators = [numerator]
        numerator *= 10
        while numerator:
            reminders.append(str(numerator / denominator))
            numerator %= denominator
            if numerator in numerators:
                i = numerators.index(numerator)
                return result + "%s.%s(%s)" % (left, "".join(reminders[:i]), "".join(reminders[i:]))
            numerators.append(numerator)
            numerator *= 10
        return result + "%s.%s" % (left, "".join(reminders))
