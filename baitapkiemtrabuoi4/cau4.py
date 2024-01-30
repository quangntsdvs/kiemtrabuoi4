def la_dao_chu(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()

    sorted_word1 = ''.join(sorted(word1))
    sorted_word2 = ''.join(sorted(word2))

    return sorted_word1 == sorted_word2

#example
tu1 = "renga"
tu2 = "garen"
ket_qua = la_dao_chu(tu1, tu2)
print(ket_qua)