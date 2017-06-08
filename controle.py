import requests


class action_borne(object):
    def act_bor(self, ip):
    
        url = 'http://' + ip + '/update.php'
        
        #Champ et valeur du formulaire
        params = {'control': 'yes'}

        #Envoi de la requête
        req = requests.post(url, data = params)

        #Récupération de la réponse du serveur
        print(req.text)
        return req.text
    
# a = action_borne()
# a.act_bor('10.6.13.18')
