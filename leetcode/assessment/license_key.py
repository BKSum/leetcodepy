class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        output = s.upper().replace("-", "")[::-1]
        output = '-'.join([output[i:i+k] for i in range(0, len(output), k)])
        return output[::-1]
