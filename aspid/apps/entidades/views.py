from django.shortcuts import render
from .models import Empresa
from .tables import EmpresasTable
# Create your views here.

from django_tables2 import SingleTableView, RequestConfig
from django.contrib.auth.decorators import login_required


class EmpresaSingleTableView(SingleTableView):
    template_name='base/generic_list.html'
    model = Empresa
    table_class = EmpresasTable
    def get_queryset(self):
        table = super(EmpresaSingleTableView, self).get_queryset()
        q=self.request.GET.get("q")
        if q: return table.using(self.request.session['db']).filter(nombre__icontains=q)#.order_by(sort)
        else: return table.using(self.request.session['db'])

    def get_context_data(self, **kwargs):
        context = super(EmpresaSingleTableView, self).get_context_data(**kwargs)
        context['sort']= self.request.GET.get("sort")
        return context

    def post(self, request, *args, **kwargs):
        checks = request.POST.getlist('checks')
        if not checks:
            mensaje = msg_render("<strong>Favor seleccione por lo menos un item</strong>")
            messages.add_message(request, messages.INFO, mensaje)
            url = request.META['HTTP_REFERER']
            return HttpResponseRedirect(url)


        sort=request.POST.get('sort')
        ids = map(int, checks)
        paises=pais.objects.filter(pk__in=ids)
        accion=request.POST.get('accion')
        
        table = paisesTablePDF(paises)
        if sort!='None':
            table.order_by = sort 

        if accion=='A csv':
            RequestConfig(request).configure(table)
            return export_table_to_csv(pais, request, table)

        elif accion=='A pdf':
            table.model=pais
            RequestConfig(request).configure(table)            
            pdf_name = 'base/generic_pdf_list.html'
            return PDFTemplateResponse(request, pdf_name, {'table':table})

        elif accion=='Eliminar':
            perm = 'pais.delete_pais'
            if request.user.has_perm(perm):
                if request.POST.get("confirmar")=='True':
                    return eliminar_bulk(request, paises)
                else:
                    dic={'object_list':paises}
                    template_name='base/generic_delete.html'
                    return render_to_response(template_name, dic, context_instance=RequestContext(request, locals()))
            else:
                mensaje = "ACCESO RESTRINGIDO | Permiso Requerido: "+str(perm)
                messages.add_message(request, messages.ERROR, mensaje, extra_tags='danger')
                url = request.META['HTTP_REFERER']
                return HttpResponseRedirect(url)                
