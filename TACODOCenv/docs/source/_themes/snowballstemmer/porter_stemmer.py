# Generated by Snowball 2.2.0 - https://snowballstem.org/

from .basestemmer import BaseStemmer
from .among import Among


class PorterStemmer(BaseStemmer):
    '''
    This class implements the stemming algorithm defined by a snowball script.
    Generated by Snowball 2.2.0 - https://snowballstem.org/
    '''

    a_0 = [
        Among(u"s", -1, 3),
        Among(u"ies", 0, 2),
        Among(u"sses", 0, 1),
        Among(u"ss", 0, -1)
    ]

    a_1 = [
        Among(u"", -1, 3),
        Among(u"bb", 0, 2),
        Among(u"dd", 0, 2),
        Among(u"ff", 0, 2),
        Among(u"gg", 0, 2),
        Among(u"bl", 0, 1),
        Among(u"mm", 0, 2),
        Among(u"nn", 0, 2),
        Among(u"pp", 0, 2),
        Among(u"rr", 0, 2),
        Among(u"at", 0, 1),
        Among(u"tt", 0, 2),
        Among(u"iz", 0, 1)
    ]

    a_2 = [
        Among(u"ed", -1, 2),
        Among(u"eed", 0, 1),
        Among(u"ing", -1, 2)
    ]

    a_3 = [
        Among(u"anci", -1, 3),
        Among(u"enci", -1, 2),
        Among(u"abli", -1, 4),
        Among(u"eli", -1, 6),
        Among(u"alli", -1, 9),
        Among(u"ousli", -1, 11),
        Among(u"entli", -1, 5),
        Among(u"aliti", -1, 9),
        Among(u"biliti", -1, 13),
        Among(u"iviti", -1, 12),
        Among(u"tional", -1, 1),
        Among(u"ational", 10, 8),
        Among(u"alism", -1, 9),
        Among(u"ation", -1, 8),
        Among(u"ization", 13, 7),
        Among(u"izer", -1, 7),
        Among(u"ator", -1, 8),
        Among(u"iveness", -1, 12),
        Among(u"fulness", -1, 10),
        Among(u"ousness", -1, 11)
    ]

    a_4 = [
        Among(u"icate", -1, 2),
        Among(u"ative", -1, 3),
        Among(u"alize", -1, 1),
        Among(u"iciti", -1, 2),
        Among(u"ical", -1, 2),
        Among(u"ful", -1, 3),
        Among(u"ness", -1, 3)
    ]

    a_5 = [
        Among(u"ic", -1, 1),
        Among(u"ance", -1, 1),
        Among(u"ence", -1, 1),
        Among(u"able", -1, 1),
        Among(u"ible", -1, 1),
        Among(u"ate", -1, 1),
        Among(u"ive", -1, 1),
        Among(u"ize", -1, 1),
        Among(u"iti", -1, 1),
        Among(u"al", -1, 1),
        Among(u"ism", -1, 1),
        Among(u"ion", -1, 2),
        Among(u"er", -1, 1),
        Among(u"ous", -1, 1),
        Among(u"ant", -1, 1),
        Among(u"ent", -1, 1),
        Among(u"ment", 15, 1),
        Among(u"ement", 16, 1),
        Among(u"ou", -1, 1)
    ]

    g_v = [17, 65, 16, 1]

    g_v_WXY = [1, 17, 65, 208, 1]

    B_Y_found = False
    I_p2 = 0
    I_p1 = 0

    def __r_shortv(self):
        if not self.out_grouping_b(PorterStemmer.g_v_WXY, 89, 121):
            return False
        if not self.in_grouping_b(PorterStemmer.g_v, 97, 121):
            return False
        if not self.out_grouping_b(PorterStemmer.g_v, 97, 121):
            return False
        return True

    def __r_R1(self):
        if not self.I_p1 <= self.cursor:
            return False
        return True

    def __r_R2(self):
        if not self.I_p2 <= self.cursor:
            return False
        return True

    def __r_Step_1a(self):
        self.ket = self.cursor
        among_var = self.find_among_b(PorterStemmer.a_0)
        if among_var == 0:
            return False
        self.bra = self.cursor
        if among_var == 1:
            if not self.slice_from(u"ss"):
                return False
        elif among_var == 2:
            if not self.slice_from(u"i"):
                return False
        elif among_var == 3:
            if not self.slice_del():
                return False

        return True

    def __r_Step_1b(self):
        self.ket = self.cursor
        among_var = self.find_among_b(PorterStemmer.a_2)
        if among_var == 0:
            return False
        self.bra = self.cursor
        if among_var == 1:
            if not self.__r_R1():
                return False
            if not self.slice_from(u"ee"):
                return False
        else:
            v_1 = self.limit - self.cursor
            if not self.go_out_grouping_b(PorterStemmer.g_v, 97, 121):
                return False
            self.cursor -= 1
            self.cursor = self.limit - v_1
            if not self.slice_del():
                return False

            v_2 = self.limit - self.cursor
            among_var = self.find_among_b(PorterStemmer.a_1)
            if among_var == 0:
                return False
            self.cursor = self.limit - v_2
            if among_var == 1:
                c = self.cursor
                self.insert(self.cursor, self.cursor, u"e")
                self.cursor = c
            elif among_var == 2:
                self.ket = self.cursor
                if self.cursor <= self.limit_backward:
                    return False
                self.cursor -= 1
                self.bra = self.cursor
                if not self.slice_del():
                    return False

            else:
                if self.cursor != self.I_p1:
                    return False
                v_3 = self.limit - self.cursor
                if not self.__r_shortv():
                    return False
                self.cursor = self.limit - v_3
                c = self.cursor
                self.insert(self.cursor, self.cursor, u"e")
                self.cursor = c
        return True

    def __r_Step_1c(self):
        self.ket = self.cursor
        try:
            v_1 = self.limit - self.cursor
            try:
                if not self.eq_s_b(u"y"):
                    raise lab1()
                raise lab0()
            except lab1: pass
            self.cursor = self.limit - v_1
            if not self.eq_s_b(u"Y"):
                return False
        except lab0: pass
        self.bra = self.cursor
        if not self.go_out_grouping_b(PorterStemmer.g_v, 97, 121):
            return False
        self.cursor -= 1
        if not self.slice_from(u"i"):
            return False
        return True

    def __r_Step_2(self):
        self.ket = self.cursor
        among_var = self.find_among_b(PorterStemmer.a_3)
        if among_var == 0:
            return False
        self.bra = self.cursor
        if not self.__r_R1():
            return False
        if among_var == 1:
            if not self.slice_from(u"tion"):
                return False
        elif among_var == 2:
            if not self.slice_from(u"ence"):
                return False
        elif among_var == 3:
            if not self.slice_from(u"ance"):
                return False
        elif among_var == 4:
            if not self.slice_from(u"able"):
                return False
        elif among_var == 5:
            if not self.slice_from(u"ent"):
                return False
        elif among_var == 6:
            if not self.slice_from(u"e"):
                return False
        elif among_var == 7:
            if not self.slice_from(u"ize"):
                return False
        elif among_var == 8:
            if not self.slice_from(u"ate"):
                return False
        elif among_var == 9:
            if not self.slice_from(u"al"):
                return False
        elif among_var == 10:
            if not self.slice_from(u"ful"):
                return False
        elif among_var == 11:
            if not self.slice_from(u"ous"):
                return False
        elif among_var == 12:
            if not self.slice_from(u"ive"):
                return False
        else:
            if not self.slice_from(u"ble"):
                return False
        return True

    def __r_Step_3(self):
        self.ket = self.cursor
        among_var = self.find_among_b(PorterStemmer.a_4)
        if among_var == 0:
            return False
        self.bra = self.cursor
        if not self.__r_R1():
            return False
        if among_var == 1:
            if not self.slice_from(u"al"):
                return False
        elif among_var == 2:
            if not self.slice_from(u"ic"):
                return False
        else:
            if not self.slice_del():
                return False

        return True

    def __r_Step_4(self):
        self.ket = self.cursor
        among_var = self.find_among_b(PorterStemmer.a_5)
        if among_var == 0:
            return False
        self.bra = self.cursor
        if not self.__r_R2():
            return False
        if among_var == 1:
            if not self.slice_del():
                return False

        else:
            try:
                v_1 = self.limit - self.cursor
                try:
                    if not self.eq_s_b(u"s"):
                        raise lab1()
                    raise lab0()
                except lab1: pass
                self.cursor = self.limit - v_1
                if not self.eq_s_b(u"t"):
                    return False
            except lab0: pass
            if not self.slice_del():
                return False

        return True

    def __r_Step_5a(self):
        self.ket = self.cursor
        if not self.eq_s_b(u"e"):
            return False
        self.bra = self.cursor
        try:
            v_1 = self.limit - self.cursor
            try:
                if not self.__r_R2():
                    raise lab1()
                raise lab0()
            except lab1: pass
            self.cursor = self.limit - v_1
            if not self.__r_R1():
                return False
            v_2 = self.limit - self.cursor
            try:
                if not self.__r_shortv():
                    raise lab2()
                return False
            except lab2: pass
            self.cursor = self.limit - v_2
        except lab0: pass
        if not self.slice_del():
            return False

        return True

    def __r_Step_5b(self):
        self.ket = self.cursor
        if not self.eq_s_b(u"l"):
            return False
        self.bra = self.cursor
        if not self.__r_R2():
            return False
        if not self.eq_s_b(u"l"):
            return False
        if not self.slice_del():
            return False

        return True

    def _stem(self):
        self.B_Y_found = False
        v_1 = self.cursor
        try:
            self.bra = self.cursor
            if not self.eq_s(u"y"):
                raise lab0()
            self.ket = self.cursor
            if not self.slice_from(u"Y"):
                return False
            self.B_Y_found = True
        except lab0: pass
        self.cursor = v_1
        v_2 = self.cursor
        try:
            while True:
                v_3 = self.cursor
                try:
                    try:
                        while True:
                            v_4 = self.cursor
                            try:
                                if not self.in_grouping(PorterStemmer.g_v, 97, 121):
                                    raise lab4()
                                self.bra = self.cursor
                                if not self.eq_s(u"y"):
                                    raise lab4()
                                self.ket = self.cursor
                                self.cursor = v_4
                                raise lab3()
                            except lab4: pass
                            self.cursor = v_4
                            if self.cursor >= self.limit:
                                raise lab2()
                            self.cursor += 1
                    except lab3: pass
                    if not self.slice_from(u"Y"):
                        return False
                    self.B_Y_found = True
                    continue
                except lab2: pass
                self.cursor = v_3
                break
        except lab1: pass
        self.cursor = v_2
        self.I_p1 = self.limit
        self.I_p2 = self.limit
        v_5 = self.cursor
        try:
            if not self.go_out_grouping(PorterStemmer.g_v, 97, 121):
                raise lab5()
            self.cursor += 1
            if not self.go_in_grouping(PorterStemmer.g_v, 97, 121):
                raise lab5()
            self.cursor += 1
            self.I_p1 = self.cursor
            if not self.go_out_grouping(PorterStemmer.g_v, 97, 121):
                raise lab5()
            self.cursor += 1
            if not self.go_in_grouping(PorterStemmer.g_v, 97, 121):
                raise lab5()
            self.cursor += 1
            self.I_p2 = self.cursor
        except lab5: pass
        self.cursor = v_5
        self.limit_backward = self.cursor
        self.cursor = self.limit
        v_6 = self.limit - self.cursor
        self.__r_Step_1a()
        self.cursor = self.limit - v_6
        v_7 = self.limit - self.cursor
        self.__r_Step_1b()
        self.cursor = self.limit - v_7
        v_8 = self.limit - self.cursor
        self.__r_Step_1c()
        self.cursor = self.limit - v_8
        v_9 = self.limit - self.cursor
        self.__r_Step_2()
        self.cursor = self.limit - v_9
        v_10 = self.limit - self.cursor
        self.__r_Step_3()
        self.cursor = self.limit - v_10
        v_11 = self.limit - self.cursor
        self.__r_Step_4()
        self.cursor = self.limit - v_11
        v_12 = self.limit - self.cursor
        self.__r_Step_5a()
        self.cursor = self.limit - v_12
        v_13 = self.limit - self.cursor
        self.__r_Step_5b()
        self.cursor = self.limit - v_13
        self.cursor = self.limit_backward
        v_14 = self.cursor
        try:
            if not self.B_Y_found:
                raise lab6()
            while True:
                v_15 = self.cursor
                try:
                    try:
                        while True:
                            v_16 = self.cursor
                            try:
                                self.bra = self.cursor
                                if not self.eq_s(u"Y"):
                                    raise lab9()
                                self.ket = self.cursor
                                self.cursor = v_16
                                raise lab8()
                            except lab9: pass
                            self.cursor = v_16
                            if self.cursor >= self.limit:
                                raise lab7()
                            self.cursor += 1
                    except lab8: pass
                    if not self.slice_from(u"y"):
                        return False
                    continue
                except lab7: pass
                self.cursor = v_15
                break
        except lab6: pass
        self.cursor = v_14
        return True


class lab0(BaseException): pass


class lab1(BaseException): pass


class lab2(BaseException): pass


class lab3(BaseException): pass


class lab4(BaseException): pass


class lab5(BaseException): pass


class lab6(BaseException): pass


class lab7(BaseException): pass


class lab8(BaseException): pass


class lab9(BaseException): pass
