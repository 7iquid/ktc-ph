from django.shortcuts import render

# Create your views here.
from django.shortcuts import  render, redirect
# from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

#tokem requirement
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        # token['photo'] = user.photo
        token['is_staff'] = user.is_staff
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# Create your views here.


class  MainApiView(APIView):
	"""
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
	authentication_classes = [SessionAuthentication, BasicAuthentication]
	permission_classes = [IsAuthenticated]

	# renderer_classes = [JSONRenderer]
	# renderer_classes = [TemplateHTMLRenderer]
	# item = Photo.objects.all()
	# serializer = PhotoSerializer(item, many=True)
	# return Response(serializer.data) 

	def get(self, request, format=None):
		content = {
		'user': str(request.user),  # `django.contrib.auth.User` instance.
		'auth': str(request.auth),  # None
		}
		# serializer = PhotoSerializer(item, many=True)
		return Response({'name':'tamina'})






# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			# login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("MainApp:")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="Accounts/register.html", context={"register_form":form})

