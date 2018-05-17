# Python_3_na_WEB_com_Django

Projeto Realizadado seguindo os procedimentos da aula [Python 3 na Web_com_Django](https://www.udemy.com/python-3-na-web-com-django-basico-intermediario/learn/v4/). o Principal objetico deste projeto é esclarecer diferenças de versões apresentada para registrar futuras complicações

## Índice

+ [Ferramentas e Versões](#ferramentas_e_versoes)
+ [Notas Pessoais](#notas_pessoais)
+ [Procedimentos de Aulas](#procedimentos_de_aulas)
  - [Sessão 1](#sessao_1)
  - [Sessão 2](#sessao_2)
  - [Sessão 3](#sessao_3)



## <a name="ferramentas_e_versoes"></a>Ferramentas e Versões
  - [Python 3.7.0b4](https://www.python.org/downloads/windows/)
  - [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
  - [Django 2.0.5](https://www.djangoproject.com/download/)
  - [Atom](https://atom.io/)
  - [SQLite Studio 3.1.1](https://sqlitestudio.pl/index.rvt?act=download)

## <a name="notas_pessoais"></a>Notas Pessoais
- Django 2 carece de uma forma de deletar os dados do banco de dados ou um app completamente de forma segura ou simples, a vários métodos na internet sobre isso, mas nem um deles é uma extensão de comandos ou plugins para django que realize o procedimento de forma automatizada. Depois realizar uma pesquisa melhor sobre, talvez encontre uma forma.


## <a name="procedimentos_de_aulas"></a>Procedimentos De Aulas

### <a name="sessao_1"></a>Sessão 1

##### Índice

  - [Até a Aula 11](#aula_11)

##### <a name="aula_11"></a>Até a aula 11
___
###### Descrição:

Criei este projeto a partir desta aula.

###### Procedimentos:

1. Instalado [Python 3.7.0b4](https://www.python.org/downloads/windows/)
2. Instalado [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. Configurado Ambiente de desenvolvimentos com VirtualEnv, Simplemooc
4. Instalado [Django 2.0.5](https://www.djangoproject.com/download/) No Ambiente Virtual e iniciado projeto SimpleMooc
5. Feito configurações necessárias.
6. Criado app core e feito modificações necessárias.
7. Aplicado templates, arquivos files e css.
8. Realizado herança com tags padrão do django.

###### <a name="notas_11"></a>Notas:

- A versão do Django apresentada no Curso é diferente a usada neste Projeto
  - Curso: versão 1.x
  - Este Projeto: versão 2.0.5
- Devido a diferença de Versão as seguintes alterações são necessárias
  - [syncdb foi descontinuada](https://docs.djangoproject.com/en/1.7/releases/1.7/#what-s-new-in-django-1-7) usar os [comandos migrate](https://docs.djangoproject.com/en/2.0/topics/migrations/) para tal
  - A forma de adicionar url ao url_patterns foi alterada:
    - A forma apresentada abaixo foi a indicada no curso:
      ```Python
      from django.conf.urls import patterns, include, url
      urlpatterns = patterns('',
        url(r'^$', 'SimpleMooc.core.views.home', name='home'),
        url(r'^contato/$', 'SimpleMooc.core.views.contact', name='contact')
      )
      ```
    - Deve-se usar a seguinte forma para a versão deste Projeto:
      ```Python
      from django.urls import path
      from simplemooc.core.views import home, contact

      app_name = 'core'
      urlpatterns = [
          path('', home, name="home"),
          path('contact/', contact, name="contact"),
      ]

      ```
    - Incluir urls de outros arquivos:
        ```Python
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('', include('simplemooc.core.urls', namespace='core')),
            path('admin/', admin.site.urls)
        ]

        ```

### <a name="sessao_2"></a>Sessão 2

----

#### Índice
1. [Aula 12](#aula_12)
2. [Aula 13](#aula_13)
3. [Aula 14](#aula_14)
4. [Aula 15](#aula_15)
5. [Aula 16](#aula_16)
6. [Aula 17](#aula_17)
7. [Aula 18](#aula_18)

##### <a name="aula_12"></a>Aula 12
---

###### Descrição:
Esta aula tem o objetivo criar models para manipular o banco de dados sem a utilização de comandos de banco de dados

###### Procedimentos:

1. Criar novo app "courses", com o objetivo de gerenciar os cursos do simplemooc
2. Criar Models do app courses.
3. Atualizar o banco de dados, com os modelos criados, [uso de migrate](#notas_11).

###### <a name="notas_12"></a>Notas:

- A Objetos do tipo image (models.ImageField) precisam da biblioteca Pillow que não esta instalada por padrão, para instalar é preciso usar o comandos:
  > $ pip install Pillow


##### <a name="aula_13"></a>Aula 13
---

###### Descrição:
Demonstração dos metodos usados dentro da classe models. nem um procedimento de alteração nesta aula. Apenas demonstração dos métodos do django.
###### Procedimentos:

###### <a name="notas_13"></a>Notas:

- Não apagar o banco de dados como dito em aula, A nova versão de Django faz comparação de informações com o banco e muda, sem precisar remover diretamente
- Método save() em models, é extremamente importante pois é ele que lança a informação do modelo no banco de dados do Django.
- Delete() remove os dados.
- Os objetos models são relacionados as suas respectivas linhas de banco de dados no django
- Por enquanto não foi ensinado como modificar models via uso de id.

##### <a name="aula_14"></a>Aula 14
---

###### Descrição:

###### Procedimentos:
1. <a name="pr_14_sqlall_deprecated"></a> Procedimento alternativo ao sqlall
    ```bash
    $ py manage.py showmigrations
    ```
    - Este comando irá mostrar a lista de migrations executadas agrupadas por app
    - Procure seu app e lá terá todos os nomes das modificações feitas pelas migrações, então execute:
    ```bash
    $ py manage.py sqlmigrate app_name migrate_name
    ```
    - O resultado será o comando sql para realizar a migração do código.

2. O acesso e manipulação do dos objetos do django dar-se na utilização do objeto do model_name.objects.método(), consultar tudo (all()), filtrar (filter(lookups)).

###### <a name="notas_14"></a>Notas
- [Mais uma vez](#notas_13) não apagar banco de dados como mostrado na aula.
- Por causa da Atualização do Django, para realizar o equivalente a sqlall da versão antiga usa-se este [procedimento](#pr_14_sqlall_deprecated).
- [Importante] Acessando Model.objects.all() ele retorna um modo de acesso a todos os objetos criados porém ele não faz a consulta no BD ainda, para isso usa-se os métodos nele.
- [Importante] O Método Model.objects.filter() retorna o mesmo modo de acesso, porém filtrado via [lookups](https://docs.djangoproject.com/en/2.0/ref/models/lookups/).
- model_name.objects é um object tipo manager.

##### <a name="aula_15"></a>Aula 15
---

###### Descrição:
Aula sobre Custom [Manager](https://docs.djangoproject.com/en/2.0/topics/db/managers/)
###### Procedimentos:
1. Nem um procedimento que requer atenção. Igual a aula.
###### <a name="notas_15"></a>Notas
- É possível fazer um controle lógico avançado na consulta ao banco com models.Q.
- Detalhe, a consulta é sensível a caixa.

##### <a name="aula_16"></a>Aula 16
---

###### Descrição:
Aula Sobre [admin](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/) e como fazer um admin administrar models criados.
###### Procedimentos:
1. Nem um procedimento que requer atenção. Igual a aula.
###### <a name="notas_16"></a>Notas
- Utilizar o admin.site.register dentro de admin.py, para que o user admin possa alterar via interface.

##### <a name="aula_17"></a>Aula 17
---

###### Descrição:
continuação da aula sobre adimin.
###### Procedimentos:
1.
###### <a name="notas_17"></a>Notas
- Use a Função \_\_str\_\_ para mudar a informação de nome apresentada na interface de usuário.
- Classe [META](https://docs.djangoproject.com/en/2.0/ref/models/options/) __dentro__ do model criado é usado para mudar os dados META do modelo.
- Um [ModelAdmin](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#modeladmin-options) pode ser usado para mudar a interface da model associada a mesma.

##### <a name="aula_18"></a>Aula 18
---

###### Descrição:
Aula sobre edição de models adicionados ao admin via interface.
###### Procedimentos:
1. Nem um procedimento que requer atenção. Igual a aula.
###### <a name="notas_18"></a>Notas
- prepopulated_fields é uma variável interessante para dar valores iniciais as variáveis de model, ao que parece usa um array associativo.

```
A partir desta aula e do commit "aula 18" o repositório do git foi mudado para incluir apenas o projeto DJANGO.
Ou seja a subpasta simplemooc agora é a pasta padrão.
```
### <a name="sessao_3"></a>Sessão 3
---
#### Índice

1. [aula 19](#aula_19)

##### <a name="aula_19"></a>Aula 19
---

###### Descrição:
Criando a interface de views dos Cursos
###### Procedimentos:
1. Quando solicitar para edição de url, usar esta [referencia](#notas 11) como procedimento
###### <a name="notas_19"></a>Notas

##### <a name="aula_20"></a>Aula 20
---

###### Descrição:
Criando uma listagem dos cursos na Página Cursos
###### Procedimentos:
1. Nem um procedimento que requer atenção. Igual a aula.
##### <a name="notas_20"></a>Notas
- Referencia para [tags e filtros](https://docs.djangoproject.com/pt-br/2.0/ref/templates/builtins/)

##### <a name="aula_21"></a>Aula 21
---

###### Descrição:
Requisição de imagens do banco de dados para a interface html.
###### Procedimentos:
1. Nem um procedimento que requer atenção. Igual a aula.
###### <a name="notas_21"></a>Notas
- A imagem carregada pelos modulos são copiados em uma pasta "/media/"
- É preciso configurar o arquivo settings para poder "servir" os dados dentro de media
- Estranhamente, a pasta media fica no projeto principal do Django, não na pasta do app

##### <a name="aula_22"></a>Aula 22
---

###### Descrição:
Criando a página de um único curso
###### Procedimentos:
1. NÃO apagar a Tabela, Usar o [migrate](https://docs.djangoproject.com/en/2.0/topics/migrations/) para auterar o banco.
2. Expressão regular em URL foi mudada para [URLDispacher](https://docs.djangoproject.com/en/2.0/topics/http/urls/), logo o procedimento foi alterado. O modelo é apresentado em [notas](#notas_22), quanto ao que acontece depois a aula segue igual.
###### <a name="notas_22"></a>Notas
 - A diferença no uso de expressão regular é mostrado a seguir
   - Apresentado em aula:
     ```Python
      # File /courses/urls.py
      from django.conf.urls import patterns, include, url

      urlpatterns = patterns('simplemooc.courses.views',
          url(r'^$', 'index', name='index'),
          url(r'^(?P<pk>\d+)/$', 'details', name='details')
      )
     ```
   - Código em Django 2:
     ```Python
      # File /courses/urls.py
      from django.urls import path
      from simplemooc.courses.views import index, details

      app_name = 'courses' # namespace
      urlpatterns = [
          path('', index, name="index"),
          path('<int:pk>', details, name='details')# acredito que tenha sido melhor usar slug ao invés da id do curso.
      ]
     ```
- Acredito que exista uma forma mais adequada de tratar expressões regulares em django 2, porém seguirei a aula.

##### <a name="aula_23"></a>Aula 23
---

###### Descrição:
Editando a página de curso
###### Procedimentos:
1. Nem um procedimento que requer atenção. Igual a aula.
###### <a name="notas_23"></a>Notas


##### <a name="aula_24"></a>Aula 24
---

###### Descrição:
Alterando a expressão regular para aceitar slugs como url e definindo get_absolute_url.
###### Procedimentos:
1. como apresentado em [notas 22](#notas_22) procedimento de expressão regular na url é diferente ver nas notas a baixo.
###### <a name="notas_24"></a>Notas
- Como dito na aula anterior, URLDispacher foi atualizado, permitindo um expressão regular melhor neste caso, a expressão regular com slug muda para apenas slug
  - Apresentado em aula:
    ```Python
         url(r'^(?P<slug>[\w_-])/$', 'details', name='details')
    ```
  - Código em Django 2:
    ```Python
         path('<slug:slug>', details, name='details')
    ```

##### <a name="aula_25"></a>Aula 25
---

###### Descrição:
Apenas uma introdução a [forms](https://docs.djangoproject.com/en/2.0/topics/forms/) do django
###### Procedimentos:
1. Nem um procedimento.
###### <a name="notas_25"></a>Notas
- Django tem sua própria formulação de formulários, o que quer dizer que são criados via classes similar ao models, porém direcionado a exibição e captura de dados no site.

##### <a name="aula_26"></a>Aula 26
---

###### Descrição:
Criando um model e manipulando via shell
###### Procedimentos:
1. Nem um procedimento que requer atenção. Igual a aula.
###### <a name="notas_26"></a>Notas
- forms possui [opções de Renderização](https://docs.djangoproject.com/en/2.0/topics/forms/#form-rendering-options)

##### <a name="aula_27"></a>Aula 27
---

###### Descrição:
Uso de forms no template do django
###### Procedimentos:
1. Nem um procedimento que requer atenção. Igual a aula.
###### <a name="notas_27"></a>Notas
- a tag [csrf_token](https://docs.djangoproject.com/en/2.0/ref/csrf/) é um modelo de defesa contra [csrt](https://pt.wikipedia.org/wiki/Cross-site_request_forgery)

##### <a name="aula_28"></a>Aula 28
---

###### Descrição:
Submissão de formulários do python
###### Procedimentos:
1. Nem um procedimento que requer atenção. Igual a aula.
###### <a name="notas_28"></a>Notas
- Sempre que houver uma requisição na url dos detalhes do curso, django vai invocar o método details() em Course/views.py como definido em course/urls.py e lá pode ser tratado o tipo de request verificando request.method.
- Quando o método is_valid() é executado, o acesso aos campos de form acontecem apenas via método cleaned_data que é um array associativo.



<!--
Criando uma Sessão

### <a name="sessao_xn"></a>Sessão xn
---
#### Índice


Criando uma aula
##### <a name="aula_xn"></a>Aula xn
---

###### Descrição:
Crie uma descrição
###### Procedimentos:
1. digite os procedimentos
2. siga sem detalhes
###### <a name="notas_xn"></a>Notas
preencha caso precise.




-->
