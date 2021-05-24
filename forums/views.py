from django.views import View

# Placeholder
class Home(View):
    def get(self, request):
        from django.http import HttpResponse
        return HttpResponse('<h1>Hit forums/ path</h1>')
