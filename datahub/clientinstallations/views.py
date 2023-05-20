from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, ApplicationInstance, ServerGroup, Server
from django.views import View

def home(request):
    return render(request, 'home.html')

def test(request):
    return render(request, 'test.html')

def base(request):
    return render(request, 'base.html')

def clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})

class client_detail(View):
    template_name = 'client.html'

    def get(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        context = {'client': client}
        return render(request, self.template_name, context)
    

class app_detail(View):
    template_name = 'app.html'

    def get(self, request, pk):
        app = get_object_or_404(ApplicationInstance, pk=pk)
        context = {'app': app}
        return render(request, self.template_name, context)
    
class server_detail(View):
    template_name = 'server.html'

    def get(self, request, pk):
        server = get_object_or_404(Server, pk=pk)
        context = {'server': server}
        return render(request, self.template_name, context)
    
class servergroup_detail(View):
    template_name = 'servergroup.html'

    def get(self, request, pk):
        servergroup = get_object_or_404(ServerGroup, pk=pk)
        context = {'group': servergroup}
        return render(request, self.template_name, context)
    
def servers(request):
    servers = Server.objects.all()
    return render(request, 'servers.html', {'servers': servers})

def servergroups(request):
    groups = ServerGroup.objects.all()
    return render(request, 'servergroups.html', {'groups': groups})

def update_app(request, app_id):
    app = get_object_or_404(ApplicationInstance, id=app_id)

    if request.method == 'POST':
        # Process the form data and update the application object
        app.product = request.POST.get('product')
        app.environment = request.POST.get('environment')
        app.version = request.POST.get('version')
        app.url = request.POST.get('url')
        app.relationshipmanager = request.POST.get('relationshipmanager')
        app.live = bool(request.POST.get('live'))
        app.save()

        # Redirect to a success page or perform any other desired actions
        return redirect('app', pk=app.id)

    context = {'app': app}
    return render(request, 'update_app.html', context)
