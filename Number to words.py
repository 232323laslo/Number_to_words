def number_to_words(num):

    l1 = ["один", "два", "три", "чотири", "п‘ять", "шість", "сім", "вісім", "дев‘ять",
          "десять", "одинадцять", "дванадцять", "тринадцять", "чотирнадцять", "п‘ятнадцать",
          "шістнадцять", "сімнадцять", "вісімнадцять", "дев‘ятнадцять", "двадцять"]
    l2 = ["двадцять", "тридцять", "сорок", "п‘ятдесят", "шістдесят", "сімдесят", "вісімдесят", 'дев‘яносто']

    if n <= 20:
        return l1[n - 1]
    elif n > 20:
        d = n // 10
        o = n % 10
        if d == 2:
            aab = l2[d - 2], l1[o - 1]
            ab = ' '.join(aab)
            return ab
        if o >= 1:
            a = l2[d - 2], l1[o - 1]
            aa = ' '.join(a)
            return aa
        if o == 0:
            return l2[d - 2]

n = int(input('Your number/твоє число: '))

print(number_to_words(n))