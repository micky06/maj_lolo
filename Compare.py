import time


class Compare_log_nsrtgv(object):

    def __init__(self):
        self.counter = 0
        self.deplace = 0

    def compare(self, list_log, list_nsrtgv, index):
        long = len(list_nsrtgv), len(list_log)
        #print("longueur au depard =   ", long)
        # for i, l in enumerate(list_log):
        l = list_log[index]
        ok, lign = self.boucle(list_nsrtgv, l)
        if not ok:
            if len(lign) > 1:
                a = False
                for o in lign:
                    # print(o)
                    if l['emplacement'] == list_nsrtgv[o]['emplacement']:
                        a = True
                        break
                    else:
                        a = False
                if not a:
                    self.deplace += 1

            else:
                for x in lign:
                    if l['emplacement'] != list_nsrtgv[x]['emplacement']:
                        self.deplace += 1
        self.counter = (float(index) / float(len(list_log))) * 100

        if len(list_log) == index + 1:
            return (len(list_log),
                    {'deplace': self.deplace,
                     'nouveau': self.delOrNew(list_log, list_nsrtgv),
                     'supprime': self.delOrNew(list_log, list_nsrtgv,
                                               "del")})
        else:
            return (len(list_log), None)

    def boucle(self, tab, dico):
        lign = []
        ok = False
        for i, v in enumerate(tab):
            if v['symbole'] == dico['symbole']:
                if v['emplacement'] == dico['emplacement']:
                    ok = True
                else:
                    lign.append(i + 1)
        return (ok, lign)

    def delOrNew(self, tab1, tab2, del_or_new="new"):
        if del_or_new == "del":
            tab1, tab2 = tab2, tab1
        # len tab - 1 : car le for commence à 0
        count = len(tab1)
        #print("{0} : {1}".format(del_or_new, count))
        for a in tab1:
            for b in tab2:
                if a['symbole'] == b['symbole']:
                    count -= 1
                    break
        return count
