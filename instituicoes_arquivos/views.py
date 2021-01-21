from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Instituicoes_Arquivos # , Anuncio
from .forms import CreateInstituicoes_ArquivosForm
from .forms import BuscaInstituicoes_ArquivosForm, BuscaResumoForm
# from .forms import InserirAnuncioForms


class Instituicoes_ArquivosCreate(LoginRequiredMixin, CreateView):
    model = Instituicoes_Arquivos
    template_name = 'instituicoes_arquivos/inc_instituicoes_arquivos.html'
    form_class = CreateInstituicoes_ArquivosForm
    success_url = reverse_lazy('lista_instituicoes_arquivos')

    def form_valid(self, form):
        form.instance.id_agencia = self.request.user
        retorno = super(Instituicoes_ArquivosCreate, self).form_valid(form)
        my_obj_instituicoes_arquivos = self.object
        self.request.session['codigo_arquivo'] = my_obj_instituicoes_arquivos.id
        self.request.session['nome_arquivo'] = my_obj_instituicoes_arquivos.nome
        return retorno

    def get_form_kwargs(self):
        kwargs = super(Instituicoes_ArquivosCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class Instituicoes_ArquivosList(LoginRequiredMixin, ListView):
    template_name = "instituicoes_arquivos/listar_instituicoes_arquivos.html"
    model = Instituicoes_Arquivos
    paginate_by = 10
    context_object_name = "instituicoes_arquivos"

    def get_queryset(self):
        nome = self.request.GET.get('nome')
        camp = self.request.GET.get('nome_camp')
        place = self.request.GET.get('palce')

        if self.request.user.is_superuser == True:
            if nome is not None:
                if nome == 'Ativas':
                    qs = Instituicoes_Arquivos.objects.select_related('id_agencia', 'id_anunciante').filter(ativa='S')
                if nome == 'Encerradas':
                    qs = Instituicoes_Arquivos.objects.select_related('id_agencia', 'id_anunciante').filter(ativa='N')

                if nome == 'Todas':
                    qs = Instituicoes_Arquivos.objects.select_related('id_agencia', 'id_anunciante').all()

                if camp != '':
                    qs = Instituicoes_Arquivos.objects.filter(nome__icontains=camp)

            else:
                qs = Instituicoes_Arquivos.objects.select_related('id_agencia', 'id_anunciante').all()

        else:
            if nome is not None:
               #  if nome == 'Ativas':
               #     qs = Anuncio.objects.prefetch_related('id_campanha', 'id_agencia', 'id_anunciante').filter(
               #         ativa='S', id_agencia=self.request.user)
                if nome == 'Encerradas':
                    qs = Instituicoes_Arquivos.objects.select_related('id_agencia', 'id_anunciante').filter(ativa='N',
                                                                                               id_agencia=self.request.user)

                if nome == 'Todas':
                    qs = Instituicoes_Arquivos.objects.select_related('id_agencia', 'id_anunciante').filter(
                        id_agencia=self.request.user)

                if camp != '':
                    qs = Instituicoes_Arquivos.objects.filter(nome__icontains=camp, id_agencia=self.request.user)

            else:
                qs = Instituicoes_Arquivos.objects.select_related('id_agencia', 'id_anunciante').filter(id_agencia=self.request.user,
                                                                                           ativa='S')

        return qs

    def get_context_data(self, **kwargs):
        context = super(Instituicoes_ArquivosList, self).get_context_data(**kwargs)
        form = BuscaResumoForm()
        context['form'] = form
        return context


class Instituicoes_ArquivosUpdate(LoginRequiredMixin, UpdateView):
    model = Instituicoes_Arquivos
    template_name = "instituicoes_arquivos/upd_instituicoes_arquivos.html"
    form_class = CreateInstituicoes_ArquivosForm
    success_url = reverse_lazy('lista_instituicoes_arquivos')

    def form_valid(self, form):
        retorno = super(Instituicoes_ArquivosUpdate, self).form_valid(form)
        my_obj = self.object
        self.request.session['codigo_arquivo'] = my_obj.id
        return retorno

    def get_form_kwargs(self):
        kwargs = super(Instituicoes_ArquivosUpdate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class Instituicoes_ArquivosDelete(LoginRequiredMixin, DeleteView):
    model = Instituicoes_Arquivos
    template_name = "instituioes_arquivos/confirma_delete.html"
    success_url = reverse_lazy('lista_campanha')


# class AnuncioCreate(LoginRequiredMixin, CreateView):
    #     model = Anuncio
    #     template_name = 'campanha/inc_anuncio.html'
    #     form_class = InserirAnuncioForms
    #     success_url = reverse_lazy('lista_anuncio')

    #     def dispatch(self, request, *args, **kwargs):
    #         self.id_campanha = kwargs['codigo_campanha']
    #         self.request.session['codigo_campanha'] = kwargs['codigo_campanha']
    #         campanha = Campanha.objects.filter(id=self.id_campanha).first()
    #         request.session['nome_campanha'] = campanha.nome

    #        return super().dispatch(request, *args, **kwargs)

    #    def form_valid(self, form):
    #        form.instance.id_campanha = Campanha.objects.get(id=self.id_campanha)
    #         return super(AnuncioCreate, self).form_valid(form)

    #     def get_form_kwargs(self):
    #         kwargs = super(AnuncioCreate, self).get_form_kwargs()
    #        kwargs.update({'user': self.request.user})
#        return kwargs


class AvaliacoesList(LoginRequiredMixin, ListView):
    template_name = "instituicoes_arquvos/listar_avaliacoes.html"
    model = Instituicoes_Arquivos
    paginate_by = 10
    context_object_name = "avaliacoes"

    def get_queryset(self):
        codigo_arquivo = self.request.session['codigo_arquivo']
        qs = Instituicoes_Arquivos.objects.select_related('id_arquico').filter(id_arquivo=codigo_arquivo)
        nome = self.request.GET.get('nome')

        if nome is not None:
            qs = Instituicoes_Arquivos.objects.filter(id_arquivo=codigo_arquivo, nome__icontains=nome)

        return qs

    def get_context_data(self, **kwargs):
        context = super(AvaliacoesList, self).get_context_data(**kwargs)
        form = BuscaInstituicoes_ArquivosForm()
        context['form'] = form
        return context


# class AvaliacoesUpdate(LoginRequiredMixin, UpdateView):
#    model = Instituicoes_Arquivos
#    form_class = CreateAvaliacoesForms
#    template_name = "instituicoes_arquivos/upd_avaliacoes.html"
#    success_url = reverse_lazy('lista_avaliacoes')

#    def get_form_kwargs(self):
#        kwargs = super(Instituicoes_ArquivosUpdate, self).get_form_kwargs()
#        kwargs.update({'user': self.request.user})
#        return kwargs


# class CampAnuncioList(LoginRequiredMixin, ListView):
#    template_name = 'campanha/listar_camp_anuncios.html'
#    model = Anuncio
#    context_object_name = "camp_anuncios"

#    def get_queryset(self):
#        codigo_campnha = self.request.session['codigo_campanha']
#        qs = Anuncio.objects.select_related('id_campanha').filter(id_campanha=codigo_campnha).order_by('nome')

#        return qs

#    def dispatch(self, request, *args, **kwargs):
#        self.id_campanha = kwargs['codigo_campanha']
#        self.request.session['codigo_campanha'] = kwargs['codigo_campanha']
#        return super().dispatch(request, *args, **kwargs)


# class ResumoSaldoList(LoginRequiredMixin, ListView):
#    template_name = 'campanha/resumo.html'
#    model = Anuncio
#    context_object_name = "resumos"

 #   def get_queryset(self):
#        nome = self.request.GET.get('nome')
#        camp = self.request.GET.get('nome_camp')
#        if self.request.user.is_superuser == True:
#            if nome is not None:
#                if nome == 'Ativas':
#                    qs = Campanha.objects.select_related('id_agencia', 'id_anunciante').filter(ativa='S')
#                if nome == 'Encerradas':
#                    qs = Campanha.objects.select_related('id_agencia', 'id_anunciante').filter(ativa='N')

#                if nome == 'Todas':
#                    qs = Campanha.objects.select_related('id_agencia', 'id_anunciante').all()

#                if camp != '':
#                    qs = Campanha.objects.filter(nome__icontains=camp)

#            else:
#                qs = Campanha.objects.select_related('id_agencia', 'id_anunciante').all()

#        else:
#            if nome is not None:
#                if nome == 'Ativas':
#                    qs = Campanha.objects.select_related('id_agencia', 'id_anunciante').filter(ativa='S',
#                                                                                               id_agencia=self.request.user)
#                if nome == 'Encerradas':
#                    qs = Campanha.objects.select_related('id_agencia', 'id_anunciante').filter(ativa='N',
#                                                                                               id_agencia=self.request.user)

 #               if nome == 'Todas':
 #                   qs = Campanha.objects.select_related('id_agencia', 'id_anunciante').filter(
 #                       id_agencia=self.request.user)

#                if camp != '':
#                    qs = Campanha.objects.filter(nome__icontains=camp, id_agencia=self.request.user)

#            else:
#                qs = Campanha.objects.select_related('id_agencia', 'id_anunciante').filter(id_agencia=self.request.user,
#                                                                                           ativa='S')

#        return qs

#    def get_context_data(self, **kwargs):
#        context = super(ResumoSaldoList, self).get_context_data(**kwargs)
#        form = BuscaResumoForm()
#        context['form'] = form
#        return context


# class CampanhaPlace(LoginRequiredMixin, ListView):
#    template_name = 'campanha/listar_camp_placer.html'
#    model = Anuncio
#    context_object_name = "camp_placers"

#    def get_queryset(self):
#        qs = Anuncio.objects.prefetch_related('id_campanha', 'id_placer').all()

#        return qs
