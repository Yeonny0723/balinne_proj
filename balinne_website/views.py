from django.shortcuts import render, redirect
from django.http import HttpResponse
from category.models import Category, Collection
from shop.models import Product, NewArrival, NewArrivalContent
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from django.template.loader import render_to_string
from balinne_website.sendEmail import custom_send_email
from django.contrib import messages
from django.core.paginator import Paginator
from pageDesign.models import HomeCarousel, InstaImg
# Create your views here.

def to_home(req):
    return redirect('index')

def index(req):
    # email sending section
    if req.method == 'POST':
        inquirer_email = req.POST['email']
        inquirer = req.POST['inquirer']
        inquiry_topic = req.POST['inquiry_topic']
        inquiry_content = req.POST['inquiry_content']

        # direct inquiry mail to Balinne mail server
        mail_subject = f'(발송 성공){inquirer}님께서 보내신 {inquiry_topic} 관련 문의'
        message = render_to_string('email/direct_inquiry.html', { 
            'inquirer': inquirer,
            'inquirer_email': inquirer_email, 
            'inquiry_topic': inquiry_topic,
            'inquiry_content': inquiry_content,
        })

        send_to = settings.BUSINESS_EMAIL
        custom_send_email(send_to, mail_subject, message)

        # 이메일 전송이 성공했다는 이메일
        current_site = get_current_site(req)
        mail_subject_to_user = f'{inquirer}님께서 보내신 {inquiry_topic} 관련 문의가 성공적으로 발송되었습니다.'
        message_to_user = render_to_string('email/email_sent_verification.html', { 
            'current_site': current_site, 
            'inquirer': inquirer,
            'inquiry_topic': inquiry_topic,
            'inquiry_content': inquiry_content,
        })
        send_to_inquirer = inquirer_email
        custom_send_email(send_to_inquirer, mail_subject_to_user, message_to_user)

        messages.success(req, '질문이 성공적으로 제출되었습니다. 이메일을 확인해주세요.') 
        # messages.success(req, 'Thank you for inquirying us. We have sent you a success email to your email. Please have a look.') 

    is_newItem = NewArrival.objects.filter(product__is_active=True).exists()
    newItem = None
    if is_newItem:
        newItem = NewArrival.objects.filter(product__is_active=True).latest('created_at')

    collections = Collection.objects.all().order_by('category__num')
    home_carousel = HomeCarousel.objects.all().order_by('num')
    instaImgs = InstaImg.objects.all().order_by('num')

    context = {
        'newItem': newItem, 
        'collections': collections, 
        'home_carousel': home_carousel, 
        'instaImgs': instaImgs, 
    }
    return render(req, 'main/home.html', context)


def set_currency(req):
    currency = req.POST['currency']
    settings.CURRENCY = currency # set user selected currency
    return redirect(req.META.get('HTTP_REFERER'))



def aboutUs(req):
    return render(req, 'main/aboutUs.html')


def newArrival(req):
    is_item = NewArrival.objects.filter(product__is_active=True).exists()
    req.session['visited_newarrival'] = True
    if is_item: 
        try:
            recent_products = NewArrival.objects.filter(product__is_active=True).order_by('-num')
            product_count = recent_products.count()
            paginator = Paginator(recent_products, 1) # 3 items per page
            page = req.GET.get('page') if req.GET.get('page') else 1
            page_out_of = paginator.get_page(page)
            recently_arrived_product = recent_products[int(page)-1].product
            newArrival_contents = NewArrivalContent.objects.filter(product=recently_arrived_product)

            context = {
                'page_out_of': page_out_of,
                'product_count': product_count, 
                'product': recently_arrived_product, 
                'contents': newArrival_contents, 
            }
            return render(req, 'main/newArrival.html', context)
            
        except NewArrival.DoesNotExist:
            messages.error(req, '아직 업로드된 신제품이 없습니다.')
            # messages.error(req, 'Sorry, New arrival item is yet appended.')
            return render(req, 'main/newArrival.html')
    else:
        return render(req, 'main/newArrival.html')


def bad_request(req, *args, **argv):
    status_code = 400
    message = "Sorry. Your request is invalid."
    context = {
        'status_code': status_code,
        'message': message,
    }
    return render(req, 'errorHandler/error_page.html', context)

def page_not_found(req, *args, **argv):
    status_code = 404
    message = "Sorry. Page not found."
    context = {
        'status_code': status_code,
        'message': message,
    }
    return render(req, 'errorHandler/error_page.html', context)


def server_error(req, *args, **argv):
    status_code = 500
    message = "서버에 일시적인 장애로, 몇 분 뒤 다시 시도해주세요."
    # message = "Sorry. Something went wrong with server. Please try again in few minutes."
    context = {
        'status_code': status_code,
        'message': message,
    }
    return render(req, 'errorHandler/error_page.html', context)


def termsNConditions(req):
    return render(req, 'legalNotice/termsNConditions.html')

def privacyPolicy(req):
    return render(req, 'legalNotice/privacyPolicy.html')

def refundPolicy(req):
    return render(req, 'legalNotice/refundPolicy.html')


def contact(req):
    return render(req, 'main/contact.html')

def visit(req):
    return render(req, 'main/visit.html')