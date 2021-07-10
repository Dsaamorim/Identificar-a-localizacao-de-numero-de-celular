#!/usr/bin/env python
# coding: utf-8

# In[13]:


import phonenumbers 
#Ajustar telefone para usarmos phonerules

telefone = "+5521972875309"
telefone_ajustado = phonenumbers.parse(telefone)
print(telefone_ajustado)

#Descobrir a localização do telefone

from phonenumbers import geocoder 
local = geocoder.description_for_number(telefone_ajustado, 'pt-br')

print(local)

telefone_formulario = "21972875309"

telefone_formulario_ajustado = phonenumbers.parse(telefone_formulario, "BR")

telefone_formatado = phonenumbers.format_number(telefone_formulario_ajustado, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

print(telefone_formatado)

#Descobrir a operadora de telefone

from phonenumbers import carrier 

operadora = carrier.name_for_number(telefone_ajustado, "pt-br")

print(operadora)

corpo_email = """Prezados, quando tiverem uma resposta da proposta favor entrar em contato.
Abraços, Douglas
(21)972875398"""

for telefone in phonenumbers.PhoneNumberMatcher(corpo_email, "BR"):
    
    print(telefone)


# In[ ]:




