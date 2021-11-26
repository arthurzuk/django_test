Aplicação desenvolvida para finalidade de teste,
utilizando-se Python e DJango.


Requerimentos:

Para rodar a aplicação é necessário Python instalado na máquina

Instruções:

-Rode o script setup.bat para instalação de dependências
e levantamento do server(host padrão 127.0.0.1/8000/)

-Para inserção e/ou download de dados utilize uma das seguintes vias:

. interface web
	
	127.0.0.1/8000/GUI/

. interface admin(somente cadastro)

	127.0.0.1/8000/admin/
	
. linha de comando
	
	#comando para criação de cadastro
		
		curl -X POST -d "username=nome&password=senha&born_date=2021-11-27" http://127.0.0.1:8000/create/
	
	# comando para download de cadastros

		curl http://127.0.0.1:8000/log/ --output cadastros.xlsx 


