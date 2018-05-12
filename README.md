# Python_3_na_WEB_com_Django

Projeto Realizadado seguindo os procedimentos da aula [Python 3 na Web_com_Django](https://www.udemy.com/python-3-na-web-com-django-basico-intermediario/learn/v4/)

## Índice

+ [Ferramentas e Versões](#ferramentas_e_versoes)
+ [Procedimentos de Aulas](#procedimentos_de_aulas)



## <a name="ferramentas_e_versoes"></a>Ferramentas e Versões
  - [Python 3.7.0b4](https://www.python.org/downloads/windows/)
  - [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
  - [Django 2.0.5](https://www.djangoproject.com/download/)
  - [Atom](https://atom.io/)
  - [SQLite Studio 3.1.1](https://sqlitestudio.pl/index.rvt?act=download)



## <a name="procedimentos_de_aulas"></a>Procedimentos De Aulas

#### Índice

  - [Até a Aula 11](#aula_11)
  - [Aula 12](#aula_12)

#### <a name="aula_11"></a>Até a aula 11
___
##### Descrição:

Criei este projeto a partir desta aula.

##### Procedimentos:

1. Instalado [Python 3.7.0b4](https://www.python.org/downloads/windows/)
2. Instalado [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
3. Configurado Ambiente de desenvolvimentos com VirtualEnv, Simplemooc
4. Instalado [Django 2.0.5](https://www.djangoproject.com/download/) No Ambiente Virtual e iniciado projeto SimpleMooc
5. Feito configurações necessárias.
6. Criado app core e feito modificações necessárias.
7. Aplicado templates, arquivos files e css.
8. Realizado herança com tags padrão do django.

##### <a name="notas_11"></a>Notas:

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

#### <a name="aula_12"></a>Aula 12
---

##### Descrição:
Esta aula tem o objetivo criar models para manipular o banco de dados sem a utilização de comandos de banco de dados

##### Procedimentos:

1. Criar novo app "courses", com o objetivo de gerenciar os cursos do simplemooc
2. Criar Models do app courses.
3. Atualizar o banco de dados, com os modelos criados, [uso de migrate](#notas_11).

##### <a name="notas_12"></a>Notas:

- A Objetos do tipo image (models.ImageField) precisam da biblioteca Pillow que não esta instalada por padrão, para instalar é preciso usar o comandos:
  > $ pip install Pillow


#### <a name="aula_13"></a>Aula 13
---

##### Descrição:
Demonstração dos metodos usados dentro da classe models. nem um procedimento de alteração nesta aula. Apenas demonstração dos métodos do django.
##### Procedimentos:

##### <a name="notas_13"></a>Notas:

- Não apagar o banco de dados como dito em aula, A nova versão de Django faz comparação de informações com o banco e muda, sem precisar remover diretamente
- Método save() em models, é extremamente importante pois é ele que lança a informação do modelo no banco de dados do Django.
- Delete() remove os dados.
- Os objetos models são relacionados as suas respectivas linhas de banco de dados no django
- Por enquanto não foi ensinado como modificar models via uso de id.

#### <a name="aula_14"></a>Aula 14
---

##### Descrição:

##### Procedimentos:
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

##### <a name="notas_14"></a>Notas
- [Mais uma vez](#notas_13) não apagar banco de dados como mostrado na aula.
- Por causa da Atualização do Django, para realizar o equivalente a sqlall da versão antiga usa-se este [procedimento](#pr_14_sqlall_deprecated).
- [Importante] Acessando Model.objects.all() ele retorna um modo de acesso a todos os objetos criados porém ele não faz a consulta no BD ainda, para isso usa-se os métodos nele.
- [Importante] O Método Model.objects.filter() retorna o mesmo modo de acesso, porém filtrado via [lookups](https://docs.djangoproject.com/en/2.0/ref/models/lookups/).
- model_name.objects é um object tipo manager. 
<!-- Criando uma aula
#### <a name="aula_x"></a>Aula x
---

##### Descrição:
Crie uma descrição
##### Procedimentos:
1. digite os procedimentos
2. siga sem detalhes
##### <a name="notas_x"></a>Notas
preencha caso precise.

-->
