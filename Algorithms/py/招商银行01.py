class Solution(object):
    def deleteText(self, article, index):
        """
        :type article: str
        :type index: int
        :rtype: str
        """
        if article[index] == ' ':
            return article
        i, j = index, index
        while i >= 1 and article[i-1] != ' ':
            i -= 1
        while j <= len(article)-2 and article[j+1] != ' ':
            j += 1
        article = article[:i] + article[j+1:]
        return " ".join(word for word in article.split(" ") if word != '')
