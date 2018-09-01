#coding: utf-8

__author__ = "Marcelo Medeiros de Vasconcellos"
__copyright__ = "Copyright 2018"
__email__ = "marcelomdevasconcellos@gmail.com"



import datetime
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from emensageriapro.padrao import *
from emensageriapro.r2040.forms import *
from emensageriapro.r2040.models import *
from emensageriapro.controle_de_acesso.models import *
import base64

#IMPORTACOES


def salvar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        r2040_recursosrep_id = int(dict_hash['id'])
        if 'tab' not in dict_hash.keys():
            dict_hash['tab'] = ''
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2040_recursosrep')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    if r2040_recursosrep_id:
        r2040_recursosrep = get_object_or_404(r2040recursosRep.objects.using( db_slug ), excluido = False, id = r2040_recursosrep_id)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos
    dados_evento = {}
    dados_evento['status'] = 0
    if r2040_recursosrep_id:
        dados_evento = r2040_recursosrep.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['r2040_recursosrep_apagar'] = 0
            dict_permissoes['r2040_recursosrep_editar'] = 0

    if permissao.permite_visualizar:
        mensagem = None
        if r2040_recursosrep_id:
            r2040_recursosrep_form = form_r2040_recursosrep(request.POST or None, instance = r2040_recursosrep, slug = db_slug)
        else:
            r2040_recursosrep_form = form_r2040_recursosrep(request.POST or None, slug = db_slug, initial={})
        if request.method == 'POST':
            if r2040_recursosrep_form.is_valid():
                dados = r2040_recursosrep_form.cleaned_data
                import json
                from django.forms.models import model_to_dict
                if r2040_recursosrep_id:
                    if dados_evento['status'] == 0:
                        dados['modificado_por_id'] = usuario_id
                        dados['modificado_em'] = datetime.datetime.now()
                        #r2040_recursosrep_campos_multiple_passo1
                        r2040recursosRep.objects.using(db_slug).filter(id=r2040_recursosrep_id).update(**dados)
                        obj = r2040recursosRep.objects.using(db_slug).get(id=r2040_recursosrep_id)
                        #r2040_recursosrep_editar_custom
                        #r2040_recursosrep_campos_multiple_passo2
                        messages.success(request, 'Alterado com sucesso!')
                        gravar_auditoria(json.dumps(model_to_dict(r2040_recursosrep), indent=4, sort_keys=True, default=str),
                                         json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                         'r2040_recursosrep', r2040_recursosrep_id, usuario_id, 2)
                    else:
                        messages.error(request, 'Somente é possível alterar eventos com status "Cadastrado"!')
                else:

                    dados['criado_por_id'] = usuario_id
                    dados['criado_em'] = datetime.datetime.now()
                    dados['excluido'] = False
                    #r2040_recursosrep_cadastrar_campos_multiple_passo1
                    obj = r2040recursosRep(**dados)
                    obj.save(using = db_slug)
                    #r2040_recursosrep_cadastrar_custom
                    #r2040_recursosrep_cadastrar_campos_multiple_passo2
                    messages.success(request, 'Cadastrado com sucesso!')
                    gravar_auditoria('{}',
                                     json.dumps(model_to_dict(obj), indent=4, sort_keys=True, default=str),
                                     'r2040_recursosrep', obj.id, usuario_id, 1)
                    if request.session['retorno_pagina'] not in ('r2040_recursosrep_apagar', 'r2040_recursosrep_salvar', 'r2040_recursosrep'):
                        return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
                    if r2040_recursosrep_id != obj.id:
                        url_hash = base64.urlsafe_b64encode( '{"print": "0", "id": "%s"}' % (obj.id) )
                        return redirect('r2040_recursosrep_salvar', hash=url_hash)
            else:
                messages.error(request, 'Erro ao salvar!')
        r2040_recursosrep_form = disabled_form_fields(r2040_recursosrep_form, permissao.permite_editar)
        if r2040_recursosrep_id:
            if dados_evento['status'] != 0:
                r2040_recursosrep_form = disabled_form_fields(r2040_recursosrep_form, 0)
        #r2040_recursosrep_campos_multiple_passo3

        for field in r2040_recursosrep_form.fields.keys():
            r2040_recursosrep_form.fields[field].widget.attrs['ng-model'] = 'r2040_recursosrep_'+field
        if int(dict_hash['print']):
            r2040_recursosrep_form = disabled_form_for_print(r2040_recursosrep_form)

        r2040_inforecurso_form = None
        r2040_inforecurso_lista = None
        r2040_infoproc_form = None
        r2040_infoproc_lista = None
        if r2040_recursosrep_id:
            r2040_recursosrep = get_object_or_404(r2040recursosRep.objects.using( db_slug ), excluido = False, id = r2040_recursosrep_id)

            r2040_inforecurso_form = form_r2040_inforecurso(initial={ 'r2040_recursosrep': r2040_recursosrep }, slug=db_slug)
            r2040_inforecurso_form.fields['r2040_recursosrep'].widget.attrs['readonly'] = True
            r2040_inforecurso_lista = r2040infoRecurso.objects.using( db_slug ).filter(excluido = False, r2040_recursosrep_id=r2040_recursosrep.id).all()
            r2040_infoproc_form = form_r2040_infoproc(initial={ 'r2040_recursosrep': r2040_recursosrep }, slug=db_slug)
            r2040_infoproc_form.fields['r2040_recursosrep'].widget.attrs['readonly'] = True
            r2040_infoproc_lista = r2040infoProc.objects.using( db_slug ).filter(excluido = False, r2040_recursosrep_id=r2040_recursosrep.id).all()
        else:
            r2040_recursosrep = None
        #r2040_recursosrep_salvar_custom_variaveis#
        tabelas_secundarias = []
        #[FUNCOES_ESPECIAIS_SALVAR]
        if dict_hash['tab'] or 'r2040_recursosrep' in request.session['retorno_pagina']:
            request.session["retorno_hash"] = hash
            request.session["retorno_pagina"] = 'r2040_recursosrep_salvar'
        controle_alteracoes = Auditoria.objects.using( db_slug ).filter(identidade=r2040_recursosrep_id, tabela='r2040_recursosrep').all()
        context = {
            'ocorrencias': dados_evento['ocorrencias'],
            'validacao_precedencia': dados_evento['validacao_precedencia'],
            'validacoes': dados_evento['validacoes'],
            'status': dados_evento['status'],
            'controle_alteracoes': controle_alteracoes,
            'r2040_recursosrep': r2040_recursosrep,
            'r2040_recursosrep_form': r2040_recursosrep_form,
            'mensagem': mensagem,
            'r2040_recursosrep_id': int(r2040_recursosrep_id),
            'usuario': usuario,

            'hash': hash,

            'r2040_inforecurso_form': r2040_inforecurso_form,
            'r2040_inforecurso_lista': r2040_inforecurso_lista,
            'r2040_infoproc_form': r2040_infoproc_form,
            'r2040_infoproc_lista': r2040_infoproc_lista,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'for_print': int(dict_hash['print']),
            'tabelas_secundarias': tabelas_secundarias,
            'tab': dict_hash['tab'],
            #r2040_recursosrep_salvar_custom_variaveis_context#
        }
        return render(request, 'r2040_recursosrep_salvar.html', context)
    else:
        context = {
            'usuario': usuario,

            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

def apagar(request, hash):
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        r2040_recursosrep_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2040_recursosrep')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)

    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos

    r2040_recursosrep = get_object_or_404(r2040recursosRep.objects.using( db_slug ), excluido = False, id = r2040_recursosrep_id)
    dados_evento = {}
    if r2040_recursosrep_id:
        dados_evento = r2040_recursosrep.evento()
        if dados_evento['status'] != 0:
            dict_permissoes['r2040_recursosrep_apagar'] = 0
            dict_permissoes['r2040_recursosrep_editar'] = 0
    if request.method == 'POST':
        if dados_evento['status'] == 0:
            import json
            from django.forms.models import model_to_dict
            situacao_anterior = json.dumps(model_to_dict(r2040_recursosrep), indent=4, sort_keys=True, default=str)
            r2040recursosRep.objects.using( db_slug ).filter(id = r2040_recursosrep_id).delete()
            #r2040_recursosrep_apagar_custom
            #r2040_recursosrep_apagar_custom
            messages.success(request, 'Apagado com sucesso!')
            gravar_auditoria(situacao_anterior,
                             '',
                             'r2040_recursosrep', r2040_recursosrep_id, usuario_id, 3)
        else:
            messages.error(request, 'Não foi possivel apagar o evento, somente é possível apagar os eventos com status "Cadastrado"!')

        if request.session['retorno_pagina']== 'r2040_recursosrep_salvar':
            return redirect('r2040_recursosrep', hash=request.session['retorno_hash'])
        else:
            return redirect(request.session['retorno_pagina'], hash=request.session['retorno_hash'])
    context = {
        'usuario': usuario,

        'modulos_permitidos_lista': modulos_permitidos_lista,
        'paginas_permitidas_lista': paginas_permitidas_lista,

        'permissao': permissao,
        'data': datetime.datetime.now(),
        'pagina': pagina,
        'dict_permissoes': dict_permissoes,
        'hash': hash,
    }
    return render(request, 'r2040_recursosrep_apagar.html', context)

def render_to_pdf(template_src, context_dict={}):
    from io import BytesIO
    from django.http import HttpResponse
    from django.template.loader import get_template
    from xhtml2pdf import pisa
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def listar(request, hash):
    for_print = 0
    db_slug = 'default'
    try:
        usuario_id = request.session['usuario_id']
        dict_hash = get_hash_url( hash )
        #retorno_pagina = dict_hash['retorno_pagina']
        #retorno_hash = dict_hash['retorno_hash']
        #r2040_recursosrep_id = int(dict_hash['id'])
        for_print = int(dict_hash['print'])
    except:
        usuario_id = False
        return redirect('login')
    usuario = get_object_or_404(Usuarios.objects.using( db_slug ), excluido = False, id = usuario_id)
    pagina = ConfigPaginas.objects.using( db_slug ).get(excluido = False, endereco='r2040_recursosrep')
    permissao = ConfigPermissoes.objects.using( db_slug ).get(excluido = False, config_paginas=pagina, config_perfis=usuario.config_perfis)
    dict_permissoes = json_to_dict(usuario.config_perfis.permissoes)
    paginas_permitidas_lista = usuario.config_perfis.paginas_permitidas
    modulos_permitidos_lista = usuario.config_perfis.modulos_permitidos


    if permissao.permite_listar:
        filtrar = False
        dict_fields = {}
        show_fields = {
            'show_excluido': 0,
            'show_modificado_por': 0,
            'show_modificado_em': 0,
            'show_criado_por': 0,
            'show_criado_em': 0,
            'show_vlrtotalnret': 0,
            'show_vlrtotalret': 1,
            'show_vlrtotalrep': 1,
            'show_cnpjassocdesp': 1,
            'show_r2040_evtassocdesprep': 1, }
        post = False
        if request.method == 'POST':
            post = True
            dict_fields = {
                'vlrtotalnret': 'vlrtotalnret',
                'vlrtotalret': 'vlrtotalret',
                'vlrtotalrep': 'vlrtotalrep',
                'cnpjassocdesp__icontains': 'cnpjassocdesp__icontains',
                'r2040_evtassocdesprep': 'r2040_evtassocdesprep',}
            for a in dict_fields:
                dict_fields[a] = request.POST.get(a or None)
            for a in show_fields:
                show_fields[a] = request.POST.get(a or None)
            if request.method == 'POST':
                dict_fields = {
                'vlrtotalnret': 'vlrtotalnret',
                'vlrtotalret': 'vlrtotalret',
                'vlrtotalrep': 'vlrtotalrep',
                'cnpjassocdesp__icontains': 'cnpjassocdesp__icontains',
                'r2040_evtassocdesprep': 'r2040_evtassocdesprep',}
                for a in dict_fields:
                    dict_fields[a] = request.POST.get(dict_fields[a] or None)
        dict_qs = clear_dict_fields(dict_fields)
        r2040_recursosrep_lista = r2040recursosRep.objects.using( db_slug ).filter(**dict_qs).filter(excluido = False).exclude(id=0).all()
        if not post and len(r2040_recursosrep_lista) > 100:
            filtrar = True
            r2040_recursosrep_lista = None
            messages.warning(request, 'Listagem com mais de 100 resultados! Filtre os resultados um melhor desempenho!')

        #r2040_recursosrep_listar_custom
        request.session["retorno_hash"] = hash
        request.session["retorno_pagina"] = 'r2040_recursosrep'
        context = {
            'r2040_recursosrep_lista': r2040_recursosrep_lista,

            'usuario': usuario,
            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'dict_fields': dict_fields,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
            'show_fields': show_fields,
            'for_print': for_print,
            'hash': hash,
            'filtrar': filtrar,

        }
        if for_print in (0,1):
            return render(request, 'r2040_recursosrep_listar.html', context)
        elif for_print == 2:
            #return render_to_pdf('tables/s1000_evtinfoempregador_pdf_xls.html', context)
            from wkhtmltopdf.views import PDFTemplateResponse
            response = PDFTemplateResponse(
                request=request,
                template='r2040_recursosrep_listar.html',
                filename="r2040_recursosrep.pdf",
                context=context,
                show_content_in_browser=True,
                cmd_options={'margin-top': 10,
                             'margin-bottom': 10,
                             'margin-right': 10,
                             'margin-left': 10,
                             'zoom': 1,
                             'dpi': 72,
                             'orientation': 'Landscape',
                             "viewport-size": "1366 x 513",
                             'javascript-delay': 1000,
                             'footer-center': '[page]/[topage]',
                             "no-stop-slow-scripts": True},
            )
            return response
        elif for_print == 3:
            from django.shortcuts import render_to_response
            response = render_to_response('r2040_recursosrep_listar.html', context)
            filename = "r2040_recursosrep.xls"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'application/vnd.ms-excel; charset=UTF-8'
            return response
        elif for_print == 4:
            from django.shortcuts import render_to_response
            response = render_to_response('tables/r2040_recursosrep_csv.html', context)
            filename = "r2040_recursosrep.csv"
            response['Content-Disposition'] = 'attachment; filename=' + filename
            response['Content-Type'] = 'text/csv; charset=UTF-8'
            return response
    else:
        context = {
            'usuario': usuario,

            'modulos_permitidos_lista': modulos_permitidos_lista,
            'paginas_permitidas_lista': paginas_permitidas_lista,

            'permissao': permissao,
            'data': datetime.datetime.now(),
            'pagina': pagina,
            'dict_permissoes': dict_permissoes,
        }
        return render(request, 'permissao_negada.html', context)

