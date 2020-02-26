#referencia : https://www.devmedia.com.br/validando-o-cnpj-em-uma-aplicacao-java/22374
 
 
#Divisor padrão para resto
divisor_modulo_padrao = 11
#Pesos do CNPJ
cnpj_pesos = ((5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2),
            (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2))
 
#recebe cnpj
cnpj = input("Insira o CNPJ para ser analisado")
 
#limpa simbolos
cnpj_s_pts = cnpj.replace(".","");
cnpj_s_pts = cnpj_s_pts.replace("/","");
cnpj_s_pts = cnpj_s_pts.replace("-","");
 
#função de calculo do digitor verificador 1
def calcula_digito_1(cnpj_aux):
   lista_pesos = cnpj_pesos[0]
   soma = 0;
   for i in range(len(cnpj_aux)):
       soma = soma + int(cnpj_aux[i]) * lista_pesos[i]
  
   resto_div = soma % divisor_modulo_padrao
   if resto_div < 2:
       return '0'
   return str(11 - resto_div);
 
#função de calculo do digitor verificador 2
def calcula_digito_2(cnpj_aux):
   lista_pesos = cnpj_pesos[1]
   soma = 0;
   for i in range(len(cnpj_aux)):
       soma = soma + int(cnpj_aux[i]) * lista_pesos[i]
 
   resto_div = soma % divisor_modulo_padrao
   if resto_div < 2:
       return '0'
   return str(11 - resto_div);
 
#verificação inicial
if len(cnpj_s_pts)!= 14 and len(cnpj)!= 14:
 print ("CNPJ Inválido")
else:
 #monta as variaveis de apoio
 cnpj_aux1 = cnpj_s_pts[:12]
 cnpj_aux2 = cnpj_s_pts[:13]
 dig_verificador_1 = cnpj_s_pts[12]
 dig_verificador_2 = cnpj_s_pts[13]
 
 #Valida o resultado dos metodos [calcula_digito] com os digitos verificadores.
 if (dig_verificador_1 == calcula_digito_1(cnpj_aux1) and dig_verificador_2 == calcula_digito_2(cnpj_aux2)):
     print ("CNPJ Válido")     
 else:
     print ("CNPJ Inválido")
