#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from webblog.models import User
def home(request):
	return render_to_response('uliweb.html')
def login(request):
	return render_to_response('login.html')
def logout(request):
	return render_to_response('uliweb.html')
def register(request):
	print '--> on 1st return'
	# return render_to_response('register.html',context_instance=RequestContext(request))
	name = request.POST["username"]
	print name
	password = request.POST['password']
	password1 = request.POST['password1']
	try :
		name == User.objects.get(user_name=name)
	except User.DoesNotExist:
		print 'Does not exist'
		if name != '':
			if password != "":
				if password == password1:
					user = User()
					user.user_name=name
					user.user_pass=password
					user.save()
					return render_to_response('forum.html',{'username':name},context_instance=RequestContext(request))
				else:
					message = "两次输入密码不一致"
					return render_to_response('register.html',{'error1':message,'username':name},context_instance=RequestContext(request))
			else:
				message = "密码不能为空"
				return render_to_response('register.html',{'error2':message},context_instance=RequestContext(request))
		else:
			message="用户名不能为空"
			return render_to_response('register.html',{'error3':message},context_instance=RequestContext(request))
	else:
		message ="用户名已存在"
		return render_to_response('register.html',{'error3':message},context_instance=RequestContext(request))
def register_index(request):
		return render_to_response('register.html',context_instance=RequestContext(request))
