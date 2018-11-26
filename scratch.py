#Sudo Code
###############################################################
test button clicked
def create_Familytree
    gets name
    calls 

#Scratched Code
################################################################

    def create_Familytree2(self):
        name = self.name2Entry.text()
        counter = 0
        childrendict = {}
        imediatefamily = self.get_Imediatefamily(name)
        returnlist = {}
        stra = '''----------------------\nDirty: {}'''.format(imediatefamily)
        # returnlist['stra'] = stra
        if imediatefamily['Mother'] != 'N/A':
            motherimediatefamily = self.get_Imediatefamily(imediatefamily['Mother'])
        print("JJJJJJJJJJJJJ: {}".format(imediatefamily['Children']))
        if len(imediatefamily['Children']) > 0:
            for string in imediatefamily['Children']:
                childrendict[counter] = self.get_Imediatefamily(string[0])
                counter = counter + 1
        strb = '{} (M, birthday={})'.format(imediatefamily['Father'], \
                                           imediatefamily['FatherBday'])
        returnlist['strb'] = strb
        strc = '{} (F, birthday={})'.format(imediatefamily['Mother'], \
                                           imediatefamily['MotherBday'])
        returnlist['strc'] = strc
        if imediatefamily['Gender'] == 'female':
            strd = '\t{} (F, birthday={})'.format(imediatefamily['Name'], \
                                                 imediatefamily['Bday'])
            returnlist['strd'] = strd
        elif imediatefamily['Gender'] == 'male' \
             or imediatefamily['Gender'] == 'weather':
            strd = '\t{} (M, birthday={})'.format(imediatefamily['Name'], \
                                                 imediatefamily['Bday'])
            returnlist['strd'] = strd
        if len(imediatefamily['Siblings']) > 0:
            for string in imediatefamily['Siblings']:
                if string[2] == 'female':
                    returnlist['stre{}'.format(counter)] = '\t{} (F, birthday={})'.format(string[0], string[1])
                    counter = counter + 1
                elif string[2] == 'male' or string[2] == 'weather':
                    returnlist['stre{}'.format(counter)] = '\t{} (M, birthday={})'.format(string[0], string[1])
                    counter = counter + 1
        if len(imediatefamily['Children']) > 0:
            if imediatefamily['Gender'] == 'female':
                strf = '{} (M)'.format(childrendict[0]['Father'])
                returnlist['strf'] = strf
                strg = '{} (F, birthday={})'.format(imediatefamily['Name'], \
                                                   imediatefamily['Bday'])
                returnlist['strg'] = strg
            elif imediatefamily['Gender'] == 'male' \
                 or imediatefamily['Gender'] == 'weather':
                strf = '{} (M, birthday={})'.format(imediatefamily['Name'], \
                                                   imediatefamily['Bday'])
                returnlist['strf'] = strf
            for string in imediatefamily['Children']:
                if string[2] == 'female':
                    returnlist['strg{}'.format(counter)] = '\t{} (F, birthday={})'.format(string[0], string[1])
                    counter = counter + 1
                if string[2] == 'male' or string[2] == 'weather':
                    returnlist['strg{}'.format(counter)] = '\t{} (M, birthday={})'.format(string[0], string[1])
                    counter = counter + 1
        return returnlist

    def create_Familytree(self):
        name = self.name2Entry.text()
        counter = 0
        childrendict = {}
        imediatefamily = self.get_Imediatefamily(name)
        # print('----------------------')
        print('Dirty: {}'.format(imediatefamily))
        # for key, var in imediatefamily.items():
            # print('{}: {}'.format(key, var))
        print('----------------------')
        # if imediatefamily['Mother'] != 'N/A':
        #     motherimediatefamily = self.get_Imediatefamily(imediatefamily['Mother'])
            # print('----------------------')
            # print('Mother Imediate Family')
            # for key, var in motherimediatefamily.items():
                # print('{}: {}'.format(key, var))
        if len(imediatefamily['Children']) > 0:

            print('XXXXXXXXXXXXXXXXX: {}'.format(imediatefamily['Children']))

            for string in imediatefamily['Children']:
                childrendict[counter] = self.get_Imediatefamily(string[0])
                counter = counter + 1

            print("CHILDDICT: {}".format(childrendict))
        # print('----------------------')
        # print('----------------------')
        print('{} (M, birthday={})'.format(imediatefamily['Father'], \
                                           imediatefamily['FatherBday']))
        print('{} (F, birthday={})'.format(imediatefamily['Mother'], \
                                           imediatefamily['MotherBday']))
        if imediatefamily['Gender'] == 'female':
            print('\t{} (F, birthday={})'.format(imediatefamily['Name'], \
                                                 imediatefamily['Bday']))
        elif imediatefamily['Gender'] == 'male' \
             or imediatefamily['Gender'] == 'weather':
            print('\t{} (M, birthday={})'.format(imediatefamily['Name'], \
                                                 imediatefamily['Bday']))
        if len(imediatefamily['Siblings']) > 0:
            for string in imediatefamily['Siblings']:
                if string[2] == 'female':
                    print('\t{} (F, birthday={})'.format(string[0], string[1]))
                elif string[2] == 'male' or string[2] == 'weather':
                    print('\t{} (M, birthday={})'.format(string[0], string[1]))
        if len(imediatefamily['Children']) > 0:
            if imediatefamily['Gender'] == 'female':
                print('{} (M)'.format(childrendict[0]['Father']))
                print('{} (F, birthday={})'.format(imediatefamily['Name'], \
                                                   imediatefamily['Bday']))
            elif imediatefamily['Gender'] == 'male' \
                 or imediatefamily['Gender'] == 'weather':
                print('{} (M, birthday={})'.format(imediatefamily['Name'], \
                                                   imediatefamily['Bday']))
                print('MOTHER')
            for string in imediatefamily['Children']:
                if string[2] == 'female':
                    print('\t{} (F, birthday={})'.format(string[0], string[1]))
                if string[2] == 'male' or string[2] == 'weather':
                    print('\t{} (M, birthday={})'.format(string[0], string[1]))
        print('----------------------')

    def get_Imediatefamily(self, name):
        if len(name) == 0:
            self.msg('', 'Info', \
                     'Please enter a name of goat to build family tree.', '')
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        curs.execute('''select mother, father, bday, gender
                        from cleananimals where name = ?''', (name,))
        mfvar = curs.fetchall()
        if len(mfvar) > 0:
            mother = mfvar[0][0]
            father = mfvar[0][1]
            bday = mfvar[0][2]
            gender = mfvar[0][3]
        elif len(mfvar) == 0:
            mother = 'N/A'
            father = 'N/A'
            bday = 'N/A'
            gender = 'N/A'
            self.msg('', 'Info', 'Name not found', '')
        try:
            curs.execute('select bday from cleananimals where name = ?', \
                         (mother,))
            motherbdayfetch = curs.fetchall()
            motherbday = motherbdayfetch[0][0]
        except:
            motherbday = "0000-00-00"
        try:
            curs.execute('select bday from cleananimals where name = ?', \
                         (father,))
            fatherbdayfetch = curs.fetchall()
            fatherbday = fatherbdayfetch[0][0]
        except:
            fatherbday = "0000-00-00"

        #get siblings
        try:
            siblings = self.get_Siblings(name, mother)
        except:
            siblings = []

        #Check if they have children
        print("NAME ====== {}".format(name))
        print(self.check_Onepartner(name, gender)[1])
        # try:
        if self.check_Onepartner(name, gender)[1] == 1:
            children = self.get_Children(name, gender)
        elif self.check_Onepartner(name, gender)[1] == 0:
            children = self.get_Children2(name, gender, self.check_Onepartner(name, gender)[0])
        elif self.check_Onepartner(name, gender)[1] == 2:
            children = []
        # except:
            # children = []
        print('CHIIIIIIIIIIIIIIIIIILD: {}'.format(children))
        imediatefamily = {'Name':name,
                      'Gender':gender,
                      'Bday':bday,
                      'Mother':mother,
                          'MotherBday':motherbday,
                          'Father':father,
                          'FatherBday':fatherbday,
                          'Children':children,
                          'Siblings':siblings}

        return imediatefamily

    def check_Onepartner(self, name, gender):
        conn = sqlite3.connect(database)
        curs = conn.cursor()

        if gender == 'female':
            curs.execute('''select father from cleananimals where mother = ?''', (name,))
            x = curs.fetchall()
            print('Partners: {}'.format(x))
            myset = set(x)
            mynewx = list(myset)
            print('Partners pre-clean: {}'.format(mynewx))
            partnerlist = []
            for l in mynewx:
                partnerlist.append(l[0])
            if len(partnerlist) == 1:
                print("SHES MONOGOMOUS(SP?)")
                onepartner = 1
            elif len(partnerlist) > 1:
                print("MORE thAN ONE partner")
                onepartner = 0
            elif len(partnerlist) == 0:
                onepartner = 5
        elif gender == 'male' or gender == 'weather':
            partnerlist = []
            partnerlist.append('N/A')
            onepartner = 2
            pass
        else:
            partnerlist = []
            onepartner = 3
        conn.close()
        return partnerlist, onepartner

    def get_Children2(self, name, gender, partnerlist):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        counter = 0
        children = []
        childrendict = {}
        if gender == 'female':
            for father in partnerlist:
                curs.execute('''select name, bday, gender from
                cleananimals where mother = ? and father = ?''', (name, father))
                childrenfetchall = curs.fetchall()
                childrendict['{}'.format(father)] = childrenfetchall
        print("CHILDRENDICT: {}".format(childrendict))

        conn.close()
        for father, children in childrendict.items():
            for children in childrendict[father]:
                print("CHILDREN: {} : {}".format(father, children))

        return children

    def get_Children(self, name, gender):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        if gender == 'female':
            curs.execute('''select name, bday, gender
                        from cleananimals where mother = ?''', (name,))
            childrenfetch = curs.fetchall()
            children = []
            if len(childrenfetch) > 0:
                for string in childrenfetch:
                     children.append(string)
        if gender == 'male':
            curs.execute('''select name, bday, gender
                        from cleananimals where father = ?''', (name,))
            childrenfetch = curs.fetchall()
            children = []
            if len(childrenfetch) > 0:
                for string in childrenfetch:
                     children.append(string)
        elif gender == 'weather':
            children = []
        conn.close()
        return children

    def get_Siblings(self, name, mother):
        conn = sqlite3.connect(database)
        curs = conn.cursor()
        if mother != 'N/A':
            try:
                curs.execute('select name, bday, gender from ' \
                    'cleananimals where mother = ? and name != ?', \
                             (mother, name,))
                siblingsfetch = curs.fetchall()
                siblings = []
                for string in siblingsfetch:
                    siblings.append(string)
            except:
                siblings = []
        elif mother == 'N/A':
            siblings = []
        conn.close()
        return siblings
